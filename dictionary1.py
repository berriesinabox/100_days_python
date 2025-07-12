phone_no={
    'Ram':1234,
    'Shyam':3456,
    'Mohan':6789,
    'Ram':4456
}

#another method
# phone_no=dict({
#     'Ram':1234,
#     'Shyam':3456,
#     'Mohan':6789,
#     'Ram':4456
# })

print(phone_no)

#print(phone_no['Shyam'])  #gives phone number of shyam

phone_no['Mohan']={1111,123,234}
phone_no['Shyam']={'Shyam_Home':5555 , 'Shyam_Work':4567}

print(phone_no['Shyam']['Shyam_Work'])
print(phone_no.get('ram'))
print(phone_no.get('Ram'))

#del phone_no['Ram']
#print(phone_no)

#phone_no.pop('Shyam')

print(phone_no.popitem())
print(phone_no)

phone_no.clear()
print(phone_no)
print()

print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())


# data={
#     1:'ram',
#     2:'Shaam',
#     0:'Me'
# }
# print(data[1])
# print()