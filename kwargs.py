def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value )
info_person(name="shivi", roll=123 ,branch="ee")
print("--------")
info_person(name="raj", roll=122)

print(" \n <--x-->\n ")

def info(*num,**data):
    for key,value in data.items():
        print(key, value )
    print(num)
info(1,2,name="shivi", roll=123 ,branch="ee")
print("---------")
info(5,4,3,name="raj", roll=122)