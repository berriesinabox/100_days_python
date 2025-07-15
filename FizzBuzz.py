#on input div by 3 fizz on div by 5 buzz and on div by both 3 and 5 fizzbuzz
n=int(input("enter the number till you want to print: "))
for i in range(1,(n+1)):
    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")    
    else:
       print(i)    
