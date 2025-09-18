def factorial(n):
    if n==0 or n==1:
        return n
    else:
        n=n*factorial(n-1)
        return n
result=factorial(5)
print(result)
