import random
from random import choice
import string
import re

def create_pass():
    alphabet_string = string.ascii_uppercase
    alphabet_capital = list(alphabet_string)
    alphabet_string = string.ascii_lowercase
    alphabet_lower = list(alphabet_string)
    numbers_string = string.digits
    numbers = list(numbers_string)
    punctuation_string = string.punctuation
    punctuation = list(punctuation_string)
    #print(punctuation)

    password1 = []
    for i in range(1):
        password1.append(list(map(choice, (alphabet_capital,alphabet_lower,numbers, punctuation, alphabet_lower,alphabet_capital,numbers, punctuation,alphabet_capital,numbers,alphabet_lower, punctuation))))
    #print(password1)

    generated = []
    for s in password1:
        generated.append(s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]+s[9]+s[10]+s[11])
    #print("This is your strong password", generated)
    password = generated
    #print(password)
    password = str(password[0])
    #print(password)
    return(password)
password = create_pass()
print("This is your strong password", password)
