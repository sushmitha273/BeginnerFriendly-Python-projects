#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# easy solution
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# str=""
# for i in range(1,nr_letters+1):
#     a=random.randint(0,len(letters)-1)
#     str+=letters[a]
# for i in range(1,nr_symbols+1):
#     a=random.randint(0,len(symbols)-1)
#     str+=symbols[a]
# for i in range(1,nr_numbers+1):
#     a=random.randint(0,len(numbers)-1)
#     str+=numbers[a]
# print(str)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# str=""
# sum=nr_letters+nr_numbers+nr_symbols
# while sum>0:
#     b=random.randint(1,3)
#     if b==1 and(nr_letters)>0:
#         a=random.choice(letters)
#         str+=a
#         sum-=1
#         nr_letters-=1
#     elif b==2 and (nr_numbers)>0:
#         a=random.choice(numbers)
#         str+=a
#         sum-=1
#         nr_numbers-=1
#     elif b==3 and nr_symbols>0:
#         a=random.choice(symbols)
#         str+=a
#         nr_symbols-=1
#         sum-=1
# print(str)

        # str+=nr_letters???/


pw_list=[]
for i in range(1,nr_letters+1):
    pw_list.append(random.choice(letters))
for i in range(1,nr_symbols+1):
    pw_list.append(random.choice(symbols))
for i in range(1,nr_numbers+1):
   pw_list.append(random.choice(numbers))
random.shuffle(pw_list)
pw=""
for char in pw_list:
    pw+=char
print(pw)

