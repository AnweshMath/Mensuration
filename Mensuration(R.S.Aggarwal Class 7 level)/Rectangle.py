import math
l=float(input("Length = "))
b=float(input("Breadth = "))
d=math.sqrt((l*l)+(b*b))
p=2*(l+b)
a=l*b
print("Diagonal =",d,"unit")
print("Perimeter =",p,"unit")
print("Area =",a,"unit²")