## a=input("type E for encrypting and D for decrypting the message: ")
# text=input("enter your text here: ")
# shift=int(input("enter the shift value: "))
# word=""

# if a=="E" or a=="e" :
#     for char in text:
#         if char.isalpha():
#             start=(ord("A")) if char.isupper() else (ord("a"))
#             n=(ord(char)-start+shift)%26
#             word += chr(n+start)
#         else:
#             word+=char
# if a=="d" or a=="D":
#     for char in text:
#         if char.isalpha():
#             start=(ord("A")) if char.isupper() else (ord("a"))
#             n=(ord(char)-start-shift)%26
#             word += chr(n+start)
#         else:
#             word +=char
# print("result:",word)


while True:
    a = input("Type E for encrypting and D for decrypting the message: ")
    text = input("Enter your text here: ")
    shift = int(input("Enter the shift value: "))
    word = ""

    if a == "E" or a == "e":
        for char in text:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")
                n = (ord(char) - start + shift) % 26
                word += chr(n + start)
            else:
                word += char

    elif a == "D" or a == "d":
        for char in text:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")
                n = (ord(char) - start - shift) % 26
                word += chr(n + start)
            else:
                word += char

    else:
        print("Invalid option. Please type E or D.")
        continue  

    print("Result:", word)

    again = input("\nDo you want to go again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye! 👋")
        break


