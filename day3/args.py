# denoted as *args and **kwargs
# Lets you pass any number of positional arguments to a function. Inside the function, args is treated as a tuple.
# Lets you pass any number of keyword arguments (key=value). Inside the function, kwargs is a dictionary.

def add(*num):
    c=0
    print(num[0])
    #num[0]=4  # this doesnt work cauuse tuples cant be changed
    for i in num:
        c+=i
    print(f"sum is {c}")
add(1,2)


def adds(*nums , name):
    c=0
    print()
    print(nums)
    print(name)
    for i in nums:
        c=c+i
    print(f"sum is {c}")
adds(3,4,name="shivi")
