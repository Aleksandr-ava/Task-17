class House:
    def __init__(self):
        self.numberOfFloors = 0

    def set_new_number_of_floors(self):
        self.numberOfFloors += 5
        print(self.numberOfFloors)


floors = House()
floors.set_new_number_of_floors()
