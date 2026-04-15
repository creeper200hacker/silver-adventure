class EmailAccount:
    def __init__(self):
        self.__email = ""

    def set_email(self, email):
        if '@' in email:
            self.__email = email

    def get_email(self):
        return self.__email


# Пример 1
account = EmailAccount()
account.set_email("user@example.com")
print(account.get_email())  # user@example.com
account.set_email("wrongemail.com")
print(account.get_email())  # user@example.com
