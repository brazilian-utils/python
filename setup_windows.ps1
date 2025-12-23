Write-Host "Verificando Python disponivel..." -ForegroundColor Cyan

# - Procura todos os executáveis python no PATH
$pythonPaths = Get-Command python* -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source

# - Filtra versões >= 3.9
$pythonPaths = $pythonPaths | ForEach-Object {
    $versionOutput = & $_ --version 2>&1
    if ($versionOutput -match "Python (\d+)\.(\d+)\.(\d+)") {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        if ($major -eq 3 -and $minor -ge 9) { $_ }
    }
}

# Pega a versão mais alta disponível
$pythonPath = $pythonPaths | Sort-Object -Descending | Select-Object -First 1

if (-not $pythonPath) {
    Write-Host " Nenhum Python 3.9+ encontrado. Instale o Python e tente novamente." -ForegroundColor Red
    exit 1
}

Write-Host " Python encontrado em $pythonPath" -ForegroundColor Green

# - Verifica se o Poetry já está instalado
$possiblePoetryPaths = @(
    "$env:APPDATA\Python\Scripts\poetry.exe",
    "$env:APPDATA\Roaming\Python\Scripts\poetry.exe",
    "$env:LOCALAPPDATA\pypoetry\venv\Scripts\poetry.exe"
)

$poetryPath = $possiblePoetryPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

# - Instala o Poetry se não encontrado
if (-not $poetryPath) {
    Write-Host " Poetry nao encontrado. Instalando..." -ForegroundColor Yellow
    try {
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | & $pythonPath -
        Start-Sleep -Seconds 5

        # tenta localizar após instalação
        $poetryPath = $possiblePoetryPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

        if ($poetryPath) {
            Write-Host " Poetry instalado com sucesso em $poetryPath" -ForegroundColor Green
        } else {
            Write-Host " Erro: instalacao do Poetry parece ter falhado." -ForegroundColor Red
            exit 1
        }
    } catch {
        Write-Host " Erro durante a instalacao do Poetry: $_" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host " Poetry ja esta instalado em $poetryPath" -ForegroundColor Green
}

# - Adiciona ao PATH temporariamente
$env:PATH += ";" + (Split-Path $poetryPath)

# - Instala dependências e roda projeto
Write-Host " Instalando dependencias do projeto..." -ForegroundColor Cyan
& $poetryPath install

Write-Host " instalacao finalizada!" -ForegroundColor Green
