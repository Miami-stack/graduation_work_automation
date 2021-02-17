import faker


class UserData:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        fake = faker.Faker()
        return UserData(login=fake.email(), password=fake.password())
