def add(*args):
    total = 0
    for n in args:
        total+=n
    return total

#print(add(1,2,3,4,5,6,7,8,9))

def add2(*args):
    print(args)

#add2(3,4,5,5)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        
my_car = Car(make = "Nissan", model = "GTR")
print(my_car.make)