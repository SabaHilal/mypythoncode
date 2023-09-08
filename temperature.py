# creating a function that converts the given celsius degree temperature to Fahrenheit degree temperature
def convertCelsiustoFahrenheit(c):
   # converting celsius degree temperature to Fahrenheit degree temperature
   f = (9/5)*c + 32
   # returning Fahrenheit degree temperature of given celsius temperature
   return (f)

for ctemp in range(1, 101):
    ftemp = convertCelsiustoFahrenheit(ctemp)
    #print("The Fahrenheit equivalent of ", ctemp , "is", ftemp)
    print("The Fahrenheit equivalent of ", ctemp , "celsius is", "%.2f" % ftemp)
