from faker import Faker

fake = Faker()


class ShopData:
    def __init__(self, first_name, last_name, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code

    @staticmethod
    def random():
        return ShopData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            postal_code=fake.postcode(),
        )
