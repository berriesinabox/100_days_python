def add(a,b):
    c= a+b
    print(f"sum is {c} ")
add(5,7)

print("FOR DEFAULT ARGUMENT")

def greet(name,subject,dept= "EE"):
    print(f"hi {name}")
    print(f"do you teach {subject}")
    print(f"are you from {dept} department")

greet("shivangi", "python")

print("SINGLE * IS USED TO ACCEPT ARBITRARY POSITIONAL ARGUMENTS")

def add(*num):
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")
add(5,6)
add(9,8,3,4)
