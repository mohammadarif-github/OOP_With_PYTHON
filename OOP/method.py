class A:
    def __init__(self):
        self.value = None

    def set_value(self, v):
        self.value = v

    def show_value(self):
        print("The value is:", self.value)


obj = A()
obj.set_value(10)
obj.show_value()
