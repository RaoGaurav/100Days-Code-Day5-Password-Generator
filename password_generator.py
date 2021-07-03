import random
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

#user inputs for password size
user_size = int(input("Please tell me the size for the password :-"))

# password character and symbol deciding algorithem
user_digit = random.randint(1,round(user_size/2))
user_symbol = random.randint(1,round(user_size/2))

password =[]

# creating password list
for digit in range(1, user_digit+1):
  password.append(random.choice(digits))

for symbol in range(1, user_symbol+1):
  password.append(random.choice(symbols))

user_letter = user_size - (user_digit + user_symbol)
for letter in range(1, user_letter + 1):
  password.append(random.choice(letters))

# creation a password string to print the password
strong_password = ""

# using random.shuffle to shuffle the password list for more complex password 
random.shuffle(password) 

# adding the passwordlist variables to the password string
for letter in password:
  strong_password += letter

# printing the final password result
print(f"Your password will be :-       {strong_password}")

input()