import random


def encrypt_text(text, seed):
    encrypted = ""
    random.seed(seed)

    for i in range(0, len(text)):
        num = random.randrange(32, 126, 1)
        temp = ord(text[i]) + num
        if temp >= 126:
            temp = ord(text[i]) - num
        if temp < 32:
            temp = num
        encrypted += chr(temp)
    return encrypted

def decrypt_text(text, seed):
    decrypted = ""
    for i in range(0, len(text)):

    return text


def main():
    string = "Chase is morbidly Overweight, Violet is a whore! Nobody loves Jacob. I am crying tonight maybe?"
    print(string)
    string = encrypt_text(string, 21)
    print(string)

main()