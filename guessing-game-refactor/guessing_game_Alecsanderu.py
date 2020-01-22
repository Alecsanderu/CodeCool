import random

list_to_99 = [random.randint(1, 99) for x in range(10)]
list_to_44 = [random.randint(1, 49) for x in range(10)]


def guess_game(list, to):
    for number in list:
        guess = 0
        while number != guess:
            guess = int(input("Enter an integer from 1 to 99: "))
            if guess < number:
                print("guess is low")
                # guess = int(input("Enter an integer from 1 to 99: "))
            elif guess > number:
                print("guess is high")
                # guess = int(input("Enter an integer from 1 to 99: "))
        print("you guessed it!")


def main():
    guess_game(list_to_99, 99)
    guess_game(list_to_44, 44)


if __name__ == "__main__":
    main()
