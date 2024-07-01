import random
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '#', '$', '%', '&', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = ""

print("PASSWORD GENERATOR")
length = int(input("Preferred length of password: "))
password_list = []

for char in range(1, length + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
for char in password_list:
    password += char

print(f"Your password is: {password} \n")