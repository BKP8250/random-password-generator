#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
s=[]
z=[]
y=[]
for i in range(nr_letters):
  k=random.randint(0,51)
  s.append(letters[k])
  print(letters[k],end='')
for i in range(nr_numbers):
  l=random.randint(0,9)
  s.append(numbers[l])
  print(numbers[l],end='')
for i in range(nr_symbols):
  m=random.randint(0,8)
  s.append(symbols[m])
  print(symbols[m],end='')
print("\n your random password is")
total=nr_letters+nr_symbols+nr_numbers;
random.shuffle(s)
password=""
for char in s:
  password+=char
print(password)





  
  
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
