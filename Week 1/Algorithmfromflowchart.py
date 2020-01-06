# numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]


# temp num swap

def temporary(j):
    temp = numbers[j+1]
    numbers[j+1] = numbers[j]
    numbers[j] = temp


# sorting
def sorting(numbers):
    i = 1
    while i < n:
        j = 0
        while j <= n - 2:
            if numbers[j] > numbers[j+1]:
                temporary(j)
        j += 1
    i += 1


numbers = []
n = len(numbers)
length = int(input("Type in the length of the list: "))

for i in range(length):
    numbers.append(int(input("Enter a number: ")))

print("Initial order of numbers: ", numbers)
sorting(numbers)
print("Sorted Numbers", numbers)
