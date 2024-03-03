
# Unlimited Positioning or Variable arguments
def add(*args):
    print (type(args))
    sum = 0
    for n in args:
        sum += n

    return sum

def calculate(n, **kwargs):
    print (type(kwargs))
    print (kwargs["add"])

calculate(2, add=3, multiply=5)

print(add(1))
print(add(1, 2))
print (add(1, 2, 3))
print(add(1,2, add(2, 3, 4)))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # get returns none when no key found in map

my_car = Car(make="some-make", model="some-model")

print (my_car.model)