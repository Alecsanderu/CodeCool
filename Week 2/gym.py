# price_list = {
#     "sauna": 1500,
#     "gymwomen": 500,
#     "gymmen": 750,
#     "students": 300
# }

from termcolor import colored, cprint
prices = [1500, 500, 700, 300]

# age = 0


# def calc_price(price):
#     for i in price:
#         total = 0
#         total += price_list[i]
#     return total


question1 = input("'\033[31m' + Are you younger than 14 yrs old?:").upper()
if question1 == "N":
    question2 = input("Do you want to use sauna?:").upper()
    if question2 == "Y":
        print("You are rich as a Becali. The price is", prices[0])
        exit()
elif question1 == "Y":
    print("You are too young. Try again in 4 years")
    exit()
question3 = input("Are you a student?:").upper()
if question3 == "Y":
    print("Nice one.You get a big fat discount. The price is", prices[3])
elif question3 == "N":
    question4 = input('Are you a male?:').upper()
    if question4 == "Y":
        print("Get those muscles pumping. Price is ", prices[2])
    elif question4 == "N":
        print("Get that (‿ˠ‿) worked.Price is", prices[1])
