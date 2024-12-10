import random
import string

pass_len=12
charvalue=string.ascii_letters+string.digits+string.punctuation


#using list compression
'''password=''.join([random.choice(charvalue) for i in range(pass_len)])'''

#using for loop
password=''
for i in range(pass_len):
    password+=random.choice(charvalue)
print("your password is :",password)
