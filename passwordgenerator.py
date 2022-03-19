import random
import string

letters = string.ascii_letters
numbers = string.digits

special_chars = string.punctuation


password_length = int(input("Please enter the length of your password "))

n = 0
password = ''
while n !=password_length:
    password+=random.choice(letters)
    n+=1
    if n == password_length:
        break;
    password+=random.choice(numbers)
    n+=1
    if n == password_length:
        break;
    password+=random.choice(special_chars)
    n+=1
    if n == password_length:
        break;


password = ''.join(random.sample(password,len(password)))
print("Password: " +password)
