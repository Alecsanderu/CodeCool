import string
import random


def passwordgen():
    all_possible_chars = list(string.printable[:-6])

    len_passw = 0
    passw = ""

    while len_passw <= 20:
        passw += all_possible_chars[random.randint(
            0, len(all_possible_chars)-1)]
        len_passw += 1
    return passw


def main():
    userask = input("Password Strenght w for weak, s for strong:")
    if userask == 'w':
        weak_passwd = ['passwd', 'user', 'admin', 'root']
        print(weak_passwd[random.randint(0, len(weak_passwd)-1)])
    elif userask == 's':
        print(passwordgen())
    return
    return


if __name__ == '__main__':
    main()
