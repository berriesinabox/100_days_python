#nesting dict in a dict

# student_data={
#     'Ram':{'roll_no':123 , 'age':18, 'course':'EE'},
#     'Shyam':{'roll_no':145 , 'age':18, 'course':'EE'}
# }
# print(student_data['Ram'])
# print(student_data['Ram']['roll_no'])
# student_data['Shyam']['phone_no']=98765
# print(student_data['Shyam'])
# del student_data['Shyam']['phone_no']
# print(student_data['Shyam'])

#nesting list in a dict

# travel_data={
#     'Bihar':["Patna","Gaya","Rajgir","Nalanda"],
#     'Assam':["Guwhati","Dispur","Silchar"]
# }
# print(travel_data['Assam'])


# nesting dict in a list

student_data=[
    {
          'Name':'Ram',
          'roll_no': 123 ,
          'age':18,
          'course':'EE'
    },
    {
          'Name':'Mohan',
          'roll_no':145 ,
          'age':18,
          'course':'ECE'
    }
]      
#print(student_data[0])

def add_new_student(Name,roll_no,age,course):
    new_student={}
    new_student["Name"]=Name
    new_student["roll_no"]=roll_no
    new_student["age"]=age
    new_student["course"]=course
    student_data.append(new_student)


add_new_student("Shyam",122,18,"ME")
print(student_data)

