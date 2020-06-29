import random


def encrypt_text(text, seed):
    text = str(text)
    encrypted = ""
    random.seed(seed)

    for i in range(0, len(text)):
        num = random.randrange(32, 126, 1)
        temp = ord(text[i]) + num
        if temp > 126:
            temp -= 95
        encrypted += chr(temp)
    return encrypted


def decrypt_text(text, seed):
    decrypted = ""
    random.seed(seed)

    for i in range(0, len(text)):
        num = random.randrange(32, 126, 1)

        temp = ord(text[i]) - num

        if temp < 32:
            temp += 95

        decrypted += chr(temp)

    return decrypted
