from unittest import TestCase, main

from brutils import is_valid_email


class TestEmailValidation(TestCase):
    def test_valid_email(self):
        # Valid email addresses
        valid_emails = [
            "joao.ninguem@gmail.com",
            "user123@gmail.com",
            "test.email@mydomain.co.uk",
            "johndoe@sub.domain.example",
            "f99999999@place.university-campus.ac.in",
        ]
        for email in valid_emails:
            try:
                self.assertTrue(is_valid_email(email))
            except Exception:
                print(f"AssertionError for email: {email}")
                raise AssertionError

    def test_invalid_email(self):
        # Invalid email addresses
        invalid_emails = [
            ".joao.ninguem@gmail.com",
            "joao ninguem@gmail.com",
            "not_an_email",
            "@missing_username.com",
            "user@incomplete.",
            "user@.incomplete",
            "user@inva!id.com",
            "user@missing-tld.",
        ]
        for email in invalid_emails:
            try:
                self.assertFalse(is_valid_email(email))
            except Exception:
                print(f"AssertionError for email: {email}")
                raise AssertionError

    def test_non_string_input(self):
        # Non-string input should return False
        non_strings = [None, 123, True, ["test@example.com"]]
        for value in non_strings:
            self.assertFalse(is_valid_email(value))

    def test_empty_string(self):
        # Empty string should return False
        self.assertFalse(is_valid_email(""))


if __name__ == "__main__":
    main()
