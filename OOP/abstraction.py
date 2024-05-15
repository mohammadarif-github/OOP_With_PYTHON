class example:
    def __init__(self):
        self._data = 0

    def set_data(self, value):
        self._data = value

    def get_data(self):
        print("Data:", self._data)


obj = example()
obj.set_data(42)
obj.get_data()
