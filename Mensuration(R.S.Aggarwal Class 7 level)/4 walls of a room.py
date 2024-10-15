import math
l=float(input("Length = "))
b=float(input("Breadth = "))
h=float(input("Height = "))
d=math.sqrt(l*l+b*b+h*h)
a=2*(l+b)*h
print("Diagonal =",d,"unit")
print("Area =",a,"unit²")