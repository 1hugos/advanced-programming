class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property located at {self.address} with area: {self.area} sqm, {self.rooms} rooms, priced at {self.price}."


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House located at {self.address} with area: {self.area} sqm, {self.rooms} rooms, priced at {self.price}. "
                f"Plot size: {self.plot} sqm.")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat located at {self.address} with area: {self.area} sqm, {self.rooms} rooms, priced at {self.price}. "
                f"Located on floor: {self.floor}.")


house = House(150, 6, 800000, "Monkey Street 11", plot=1000)
flat = Flat(75, 8, 150000, "Oak Avenue 22", floor=2)

print(house)
print(flat)
