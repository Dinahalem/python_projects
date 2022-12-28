#This program is strong password generator from uppercase, lowercase, punctuation & digits
#The user enters number charaters for the password    EX:   How many characters for the password? 10
# The number of charaters should at least = 6 characters


import string
import random
s1=list(string.ascii_uppercase)
s2=list(string.ascii_lowercase)
s3= list(string.punctuation)
s4= list(string.digits)

character_number =input("How many characters for the password?  ")

while True:
    try: 
        character_number=int(character_number)
        if character_number < 6:
            print ("Please, You need at least 6 characters ")        # if the user entered less than 6 character 

            character_number + input ("please enter the number again: ") # if the user entered less than 6 character, the program will require enter again
        else:
                break
    except:
        print("please enter numbers only")
        character_number= input("How many characyters for the password: ")  # if the user entered anything other than numbers

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(character_number*(30/100))   #30% uppercase, 30% lowercase
part2=round(character_number*(20/100))   #20% digits,  20% punctuation

password=[]

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password= "".join(password[0:])   # print password in string
print(password)
