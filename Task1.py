def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n- 1)

n = int(input("enter a number:"))
fact = factorial(n)
print("factorial of",n,"is",fact)


