def num_swap(j):
    tmp = numbers[j+1]
    numbers[j+1] = numbers[j]
    numbers[j] = tmp


def sort_list(numbers):
    i = 1
    while i < len(numbers):
        j = 0
        while j <= (len(numbers) - 2):
            if numbers[j] > numbers[j+1]:
                num_swap(j)
            j += 1
        i += 1


numbers = []
length = int(input("Type in the length of the list: "))

for i in range(length):
    numbers.append(int(input("Enter a number: ")))

print("Initial order of numbers: ", numbers)

sort_list(numbers)
print("Sorted order of numbers: ", numbers)
