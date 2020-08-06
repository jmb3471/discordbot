import random
import auth

def encrypt_text(text, seed):
    text = str(text)
    print(text)
    encrypted = ""
    random.seed(seed)

    for i in range(0, len(text)):
        num = random.randrange(40, 120, 1)
        temp = ord(text[i]) + num
        if temp > 120:
            temp -= 80
        encrypted += chr(temp)
    print(encrypted)
    return encrypted


def decrypt_text(text, seed):
    print(text)
    decrypted = ""
    random.seed(seed)

    for i in range(0, len(text)):
        num = random.randrange(40, 120, 1)

        temp = ord(text[i]) - num
        if temp < 40:
            temp += 80

        decrypted += chr(temp)
    print(decrypted)
    return decrypted
