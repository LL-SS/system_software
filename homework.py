import hashlib
import time

# find a collision of SHA-256
def find_collision(zero_length):
    concat = 0
    start = time.time()

    while True:
        enc_str = hashlib.sha256(('homework' + str(concat)).encode()).hexdigest()[:5]
        bin_bit = bin(int(enc_str, 16))[2:].zfill(20)

        if int(bin_bit[:zero_length], 10) == 0:
            end = time.time()
            print('binary output:', bin_bit)
            print('nonce x:', concat)
            print('execution time:', end - start)
            break

        concat = int(concat) + 1

def find_collision_double(zero_length):
    concat = 0
    start = time.time()

    while True:
        enc_str = hashlib.sha256(('homework' + str(concat)).encode()).digest()
        enc_str_double = hashlib.sha256(enc_str).hexdigest()[:5]
        bin_bit = bin(int(enc_str_double, 16))[2:].zfill(20)

        if int(bin_bit[:zero_length], 10) == 0:
            end = time.time()
            print('binary output:', bin_bit)
            print('nonce x:', concat)
            print('execution time:', end - start)
            break

        concat = int(concat) + 1

# Increase the number of 0’s from 1 to 20 bits and plots the execution time
for i in range(1, 21):
    find_collision(i)

for i in range(1, 21):
    find_collision_double(i)