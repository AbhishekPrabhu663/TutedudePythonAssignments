import math

n=int(input("Enter a Number : "))

def calc(n):
    return "Square Root :",math.sqrt(n),"Logarithm :",math.log(n),"Sine :", math.sin(n)

result=calc(n)
print(result)


import math

n = int(input("Enter a Number : "))

def calc(n):
    print("Square Root :", math.sqrt(n))
    print("Logarithm   :", math.log(n))
    print("Sine        :", math.sin(n))

calc(n)