data={
    1:'ram',
    2:'Shaam',
    0:'Me'
}
print(data[1])
print()



phone_no={
    'Ram':1234,
    'Shyam':3456,
    'Mohan':6789,
    'Ram':4456
}
print(phone_no)
# phone_2=phone_no.copy()
# print(phone_2)
# print()
print(len(phone_no))


# for i in phone_no:
#     print(i)
#     print(phone_no[i])

print()
for i in phone_no.items():
    print(i)