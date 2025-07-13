# def add(a,b):
#     c=a+b
#     return c
# p=add(5,4)
# print(p)

def format_name(f_name, l_name):
    f = []
    l = []
    for i in f_name:
        f.append(i.lower())

    if f:
        f[0] = f[0].upper()  

    for i in l_name:
        l.append(i.lower())

    if l:
        l[0] = l[0].upper()

    name1 = f + [" "] + l  
    name = ''.join(name1)
   # print(name)
    return name

i=format_name("sHIvanGI", "shEKHar")
print(i)

# BUT THIS ONE IS BETTER

def format_name(f_name, l_name):
    f = f_name.lower().capitalize()
    l = l_name.lower().capitalize()
    name = f + " " + l
    print(name)

format_name("sHIvanGI", "shEKHar")

# .lower() converts everything to lowercase.

#.capitalize() makes the first letter uppercase, rest lowercase.

       

        
