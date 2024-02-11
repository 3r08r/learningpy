#Password Generator
#Author: Err0r
#Date: 2020-07-20
#Version: 1.0
import random
import string
length = int(input("Enter the length of the password: "))
def password_generator():
    password =  string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password) for i in range(length))
    print(password)
password_generator()