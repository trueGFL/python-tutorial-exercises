# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.

number = int(input("n?"))
n = int(number)


def sum_to(n:int):
    p = sum(range(n+1))
    return (p)

print (sum_to(n))
