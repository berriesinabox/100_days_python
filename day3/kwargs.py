def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value )
info_person(name="shivi", roll=123 ,branch="ee")
print()
info_person(name="raj", roll=122)
