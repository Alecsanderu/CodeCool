# Algorithms are one of the most important things for programmers - t
# hey are the foundations on which we build our programs.
# No matter which language you (will) use, the algorithms are always involved.

# So, no more talking, let's practice some of them - calculating minimum, maximum and average from numbers in a list.

# PLEASE DO NOT USE BUILT-IN PYTHON FUNCTIONS TO CALCULATE MIN, MAX, AND AVG! Those forbidden functions are: min(), max(), sum(), sort(), sorted() etc.

# The exercise
# Let's assume we've got a list:

# numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
# Please create three flowcharts for calculating the maximum, minimum and average number for above list (you can use draw.io).

# After this, please create a python script that will implement above flowcharts.

# (optional) Now, the list looks a bit different:

# numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]
# Update your python script to maintain its previous functionality - please ignore non-numbers and search for numbers inside nested list!


# numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

# minim = numbers[0]
# maxim = numbers[0]
# list_sum = 0


# for number in numbers:
#     list_sum = list_sum + number
#     if number < minim:
#         minim = number
#     elif number > maxim:
#         maxim = number

# print("The minimum number of the list is: ", minim)
# print("The maximum number of the list is: ", maxim)
# print("The avarage of the list is: ", list_sum / len(numbers))


numbers = [-5, 23, 0,  -9, 12, 99, [2, 44],  105, -43, 2.85]
numbers2 = []

for i in numbers:
    if type(i) == list:
        for a in i:
            numbers2.append(a)


numbers = [x for x in numbers if type(x) == int or type(x) == float]


new_no_list = numbers + numbers2

minim = numbers[0]
maxim = numbers[0]
list_sum = 0


for number in new_no_list:
    list_sum = list_sum + number
    if number < minim:
        minim = number
    elif number > maxim:
        maxim = number

print("The minimum number of the list is: ", minim)
print("The maximum number of the list is: ", maxim)
print("The avarage of the list is: ", float(list_sum / len(new_no_list)))
