

num = int(input("Enter a number between 0 and 4000 (not included!): "))
if not(num in range(1, 4000)):
    print("Invalid number, not in range!")
    exit()

ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

result = []

for i in range(len(ints)):
    count = int(nums[i] == ints[i])
    result.append(num[i] * count)
    nums += ints[i] * count

print("".joint(result))


# Number = int(input("What's your number?"))
# RomanNumber = ""
# Arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# Symbols = ["M", "CM", "D", "CD", "C", "XC",
#            "L", "XL", "X", "IX", "V", "IV", "I"]
# a = 0
# while Number != 0:
#     while (Number) >= Arabic[a]:
#         RomanNumber = RomanNumber+Symbols[a]
#         Number = Number - Arabic[a]
#     a = a+1
# print(RomanNumber)
