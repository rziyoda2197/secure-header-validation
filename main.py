class HeaderValidator:
    def __init__(self, headers):
        self.headers = headers

    def validate_header(self):
        validation_checklist = {
            "Content-Type": self.validate_content_type(),
            "Authorization": self.validate_authorization(),
            "Accept": self.validate_accept(),
            "User-Agent": self.validate_user_agent(),
            "Accept-Language": self.validate_accept_language(),
            "Accept-Encoding": self.validate_accept_encoding(),
        }

        return validation_checklist

    def validate_content_type(self):
        return self.headers.get("Content-Type") in ["application/json", "application/xml"]

    def validate_authorization(self):
        return self.headers.get("Authorization") is not None

    def validate_accept(self):
        return self.headers.get("Accept") in ["application/json", "application/xml"]

    def validate_user_agent(self):
        return self.headers.get("User-Agent") is not None

    def validate_accept_language(self):
        return self.headers.get("Accept-Language") is not None

    def validate_accept_encoding(self):
        return self.headers.get("Accept-Encoding") in ["gzip", "deflate", "br"]


def create_secure_header_validation_checklist(headers):
    validator = HeaderValidator(headers)
    return validator.validate_header()


headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token",
    "Accept": "application/json",
    "User-Agent": "Mobile App",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip",
}

print(create_secure_header_validation_checklist(headers))
```

Kodda quyidagilar mavjud:

1. `HeaderValidator` klassi yaratildi, unda `headers` obyekti saqlanadi.
2. `validate_header` metodida, `validation_checklist` obyekti yaratildi, unda barcha sarlavhalarning valyatsiya qilinishi uchun metodlar mavjud.
3. `validate_content_type`, `validate_authorization`, `validate_accept`, `validate_user_agent`, `validate_accept_language`, `validate_accept_encoding` metodlarida, kiritilgan sarlavhalarning valyatsiya qilinishi tekshiriladi.
4. `create_secure_header_validation_checklist` funktsiyasi yaratildi, unda `HeaderValidator` klassi yaratilib, `validate_header` metodidan foydalaniladi.
5. `headers` obyekti yaratildi, unda sarlavhalarning valyatsiya qilinishi tekshiriladi.
6. `create_secure_header_validation_checklist` funktsiyasi chaqirilib, natija konsolga chiqariladi.
