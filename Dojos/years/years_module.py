import datetime


def years(age):
    now = datetime.datetime.now()
    celebrate = (now.year - age) + 100
    return celebrate


def main():
    user_name = input("What is your name: ")
    user_age = int(input("What si you age?:"))
    print("{} you will be 100 YO in {}.".format(user_name, years(user_age)))
    return


if __name__ == '__main__':
    main()
