class Grandpa:
    def __init__(self, grandpa_name):
        self.grandfather_name = grandpa_name


class Father(Grandpa):
    def __init__(self, father_name, grandpa_name):
        self.father_name = father_name
        super().__init__(grandpa_name)


class Son(Father):
    def __init__(self, name, father_name, grandfather_name):
        self.name = name
        super().__init__(father_name, grandfather_name)

    def show_details(self):
        print(f"I am {self.name}, son of Mr. {
              self.father_name}. My grandfather's name is: {self.grandfather_name}")


good_son = Son("Mohammad", "Kamal", "Jamal")
good_son.show_details()
