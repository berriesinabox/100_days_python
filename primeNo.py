# import math

# n=int(input("enter the integer you want to check is prime or not: "))
# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#         return True
# if is_prime(n):
#     print(f"{n} is a prime integer")
# else:
#     print(f"{n} is not a prime integer")

import math

n = int(input("Enter the integer you want to check is prime or not: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print(f"{n} is a prime integer.")
else:
    print(f"{n} is not a prime integer.")
