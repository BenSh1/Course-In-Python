
def add(*args):
    # print(args[0])
    sum = 0
    for n in args:
        sum += n
    
    return sum

# print(add(3,5,6,2,1,7,4,3))


# kwargs is a dicitinory
def calculate(n,**kwargs):
    #print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add= 3 , multiply= 5)



class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        #self.modle = kw["modle"]
        self.modle = kw.get("modle")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan" ) #, modle="GT-R")
print(my_car.modle)




