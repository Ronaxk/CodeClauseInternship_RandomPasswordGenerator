import string 
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

while True:
    pass_length = int(input("Enter the length of your password"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # print(s)
    random.shuffle(s)

    print("".join(s[0:pass_length]))

