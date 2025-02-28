def add(*args):
    print(sum(args))


add(3, 6, 8)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # .get fills the property with None if not provided at initialization
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
