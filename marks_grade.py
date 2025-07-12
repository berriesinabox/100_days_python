student_marks={
    'shivi':93,
    'swati':89,
    'priya':77,
    'riya':45,
    'rahul':87,
    'aman':90
}
student_grade={}

for i in student_marks:
    marks = student_marks[i]
    if marks > 90:
        grade= 'A+'
    elif marks > 80:
        grade= 'A'
    elif marks > 70:
        grade= 'B'
    elif marks > 60:
        grade= 'C'
    elif marks > 50:
        grade= 'D'
    elif marks > 40:
        grade= 'E'
    else:
        grade= 'F' 

    student_grade[i]=grade
    print(f"grade of the student {i} is {grade}")
    print(f"marks of student {i} is {student_marks[i]}")     
