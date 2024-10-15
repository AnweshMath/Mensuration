import math
s1=float(input("First side = "))
s2=float(input("Second side = "))
s3=float(input("Third side = "))
s=1/2*(s1+s2+s3)
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("Area =",a,"unit²")