import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to the Password Generator")
n_letters=int(input("Enter how many letters do you want: "))
n_digits=int(input("Enter how many digits do you want: "))
n_symbols=int(input("Enter how many symbols do you want: "))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list.append(char)
for i in range(1,n_symbols+1):
    symbol=random.choice(symbols)
    password_list.append(symbol)
for i in range(1,n_digits+1):
    digit=random.choice(digits)
    password_list.append(digit)
print(password_list)
random.shuffle(password_list)
print("Shuffeled Password:",password_list)
password=""
for char in password_list:
    password=password+char
print("Password Generated:",password)    