# def add(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum

# print(add(2, 3, 4, 5, 6, 7, 9, 10, 4))

# def calculate(**kwargs):
#     print(kwargs)
#     for key,val in kwargs.items():
#         print(key)
#         print(val)


# calculate(add=2, multiple=4)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)