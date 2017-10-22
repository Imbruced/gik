
def decorator(func):
    def new_function(a, b):
        print('Wynik funckcji to {}'.format(func(a, b)))
    return new_function

@decorator
def function(a, b):
    return a+b


class Parrot:
    def __init__(self):
        self._voltage = 0


    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        if value == 0:
            print('voltage can\'t be {}'.format(0))
            raise AttributeError
        self._voltage = value

    @voltage.getter
    def voltage(self):
        print('getting_value')
        return self._voltage

    @voltage.deleter
    def voltage(self):
        print('deleting')
        del self._voltage

    def new(self):
        print('sth')

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

parr = Parrot()
parr.voltage = 10
d = parr.voltage
del(parr.voltage)