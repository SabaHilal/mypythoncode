# Import math Library
import math

x = 0
while x <= 10:
  print("x is equal to ", round(x,1))
  print("sin x is ", round(math.sin(x),4))
  print("cos x is ",round(math.cos(x),4))
  print("tan x is ",round(math.tan(x),4))
  print()
  x = x + 0.2
