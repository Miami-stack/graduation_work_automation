import random


class RandomData:
    def __init__(self, randomly):
        self.randomly = randomly

    @staticmethod
    def random(listing: list):
        return RandomData(randomly=random.choices(listing, k=2))
