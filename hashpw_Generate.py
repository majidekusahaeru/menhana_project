import hashlib
import random
    
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
salt = ''.join([random.choice(chars) for _ in range(20)])

# id = ''.join([random.choice(chars) for _ in range(8)])
# pw = ''.join([random.choice(chars) for _ in range(8)])
# print("PW：" + pw)

# coding用
id = input("id>")
pw = input("pw>")


b_pw = bytes(pw,"utf-8")
b_salt = bytes(salt,"utf-8")
hashed_pw = hashlib.pbkdf2_hmac("sha256",b_pw,b_salt,2560).hex()

print("ID：" + id)
print("hashedPW：" + hashed_pw)
print("salt：" + salt)
