import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =  ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
inp_letter=int(input("how many letters do you want to add in your password: \n"))
inp_num = int(input("how many numbers do you want to add in your password: \n"))
inp_symbol= int(input("how many symbols do you want to add in your password: \n"))

#random.shuffle(letters)
#random.shuffle(numbers)
#random.shuffle(symbols)

selected_num= random.sample(numbers , inp_num)
selected_letters=random.sample(letters, inp_letter)
selected_symbols=random.sample(symbols, inp_symbol)

password_list= selected_letters + selected_symbols + selected_num

random.shuffle(password_list)
password = ''.join(password_list)

print (f"your password is : {password}")