class vehicle:
    def __init__(self) -> None:
        pass


class aeroplane(vehicle):
    distance = 0

    def __init__(self, destination, dis) -> None:
        self.going_to = destination
        self.distance = dis
        super().__init__()

    def fair(self):
        print(f"Your flight costs around: {self.distance * 100}")


class bus(vehicle):
    distance = 0

    def __init__(self, destination, dis) -> None:
        self.going_to = destination
        self.distance = dis
        super().__init__()

    def fair(self):
        print(f"Your bus fare costs around: {self.distance * 30}")


class taxi(vehicle):
    distance = 0

    def __init__(self, destination, dis) -> None:
        self.going_to = destination
        self.distance = dis
        super().__init__()

    def fair(self):
        print(f"Your taxi fare costs around: {self.distance * 10}")


person_rich = aeroplane("Cox's Bazar", 150)
person_middle_class = bus("Cox's Bazar", 150)
person_poor_me = taxi("Cox's Bazar", 150)


person_rich.fair()
person_middle_class.fair()
person_poor_me.fair()
