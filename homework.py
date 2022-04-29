import hashlib
import string
import random

base_str = 'homework'
string_pool = string.ascii_letters
str_x = ''

# find a collision of SHA-256
length = 1

# while True:
for i in string_pool:
    str_x = i

enc_str = int(hashlib.sha256((base_str + str_x).encode()).hexdigest(), 16)
print(format(enc_str, 'b')[:2])
# print(format(enc_str, 'b')[:2], str_x, sep='\n')

    # if int(format(enc_str, 'b')[0]) == 0:
    #     break



# print(str_x)
