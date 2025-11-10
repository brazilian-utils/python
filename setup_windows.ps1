Write-Host "Verificando Python disponível..." -ForegroundColor Cyan

# 1️⃣ - Verifica Python (Microsoft Store ou instalação normal)
$pythonPaths = @(
    "$env:LOCALAPPDATA\Microsoft\WindowsApps\python3.11.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:ProgramFiles\Python311\python.exe",
    "$env:ProgramFiles(x86)\Python311\python.exe"
)

$pythonPath = $pythonPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $pythonPath) {
    Write-Host " Nenhum Python encontrado. Instale o Python 3.11+ e tente novamente." -ForegroundColor Red
    exit 1
}

Write-Host " Python encontrado em $pythonPath" -ForegroundColor Green


# 2️⃣ - Verifica se o Poetry já está instalado
$possiblePoetryPaths = @(
    "$env:APPDATA\Python\Scripts\poetry.exe",
    "$env:APPDATA\Roaming\Python\Scripts\poetry.exe",
    "$env:LOCALAPPDATA\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming\pypoetry\venv\Scripts\poetry.exe",
    "$env:LOCALAPPDATA\pypoetry\venv\Scripts\poetry.exe"
)

$poetryPath = $possiblePoetryPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

# 3️⃣ - Instala o Poetry se não encontrado
if (-not $poetryPath) {
    Write-Host "⚙️  Poetry não encontrado. Instalando..." -ForegroundColor Yellow
    try {
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | & $pythonPath -
        Start-Sleep -Seconds 5

        # tenta localizar após instalação
        $poetryPath = $possiblePoetryPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

        if ($poetryPath) {
            Write-Host " Poetry instalado com sucesso em $poetryPath" -ForegroundColor Green
        } else {
            Write-Host " Erro: instalação do Poetry parece ter falhado." -ForegroundColor Red
            exit 1
        }
    } catch {
        Write-Host " Erro durante a instalação do Poetry: $_" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host " Poetry já está instalado em $poetryPath" -ForegroundColor Green
}

# 4️⃣ - Adiciona ao PATH temporariamente
$env:PATH += ";" + (Split-Path $poetryPath)

# 5️⃣ - Instala dependências e roda projeto
Write-Host " Instalando dependências do projeto..." -ForegroundColor Cyan
& $poetryPath install

Write-Host " Rodando o projeto..." -ForegroundColor Cyan
& $poetryPath run python main.py

Write-Host " Projeto finalizado!" -ForegroundColor Green
