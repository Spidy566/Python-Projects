import random
import string

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()
random.shuffle(key)


def encrypt(message):
    encode = ""
    for char in message:
        encode += key[chars.index(char)]
    return encode


def decrypt(message):
    decode = ""
    for char in message:
        decode += chars[key.index(char)]
    return decode


text = input("Enter a message: ")
encrypted = encrypt(text)
decrypted = decrypt(encrypted)
print("Encrypted:", encrypted)
cipher = input("Enter the cipher: ")
if cipher == encrypted:
    print("Decrypted:", decrypted)
else:
    print("Invalid cipher")
