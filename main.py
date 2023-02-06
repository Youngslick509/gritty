#tutorial
def yellow(adjective):
    print("hello", adjective)
yellow('amoamogus')


#tutorial 2
Pi = 3.1415927
def Area(radius):
    return Pi * radius**2
print( Area(2) )


#tutorial 3
import math
def LengthOfHyp(x, y):
    return math.sqrt(x**2 + y**2)
print( LengthOfHyp(3, 4) )


#tutorial 4
def MyFunction(x):
    i = 0
    while i < x:
        print(i)
        i += 1
i = 4
MyFunction(i)
print("Origanal i:", i)


#real deal
def amung(parameter):
    print('howdy', parameter)
amung('partner')