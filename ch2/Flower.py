class Flower:
    """A flower class.

        name: str, the name of the flower
        num_petals: int, the number of petals
        price: float, the price of the flower. """

    def __init__(self, name, num_petals, price):
        self.name = name
        self.num_petals = num_petals
        self.price = price

    def change_name(self, name):
        self.name = name

    def change_num_petals(self, num_petals):
        self.num_petals = num_petals

    def change_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_num_petals(self):
        return self.num_petals

    def get_price(self):
        return self.price

if __name__ == '__main__':
    tulip = Flower("Tulip", 4, 130)
    print(tulip.get_name())
    tulip.change_name("Petulia")
    print(tulip.get_name())
