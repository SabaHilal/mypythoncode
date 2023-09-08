#Find what is wrong in this program
#Is the function correct?

import math

given_value = 0

def sincostanfunc(x):
    print("sin ","%.1f" %x , math.sin(math.pi/3))
    print("cos ", "%.1f" %x, math.cos(math.pi/6))
    print("tan ", "%.1f" % x, math.tan(math.pi/3))
    
while given_value <= 10:
    print('given value is: ', "%.1f" % given_value)
    sincostanfunc(given_value)
    given_value = given_value + 0.2