numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2,  44], None, 105, -43]
newList = []
max = numbers[0]
min = numbers[0]
sum = 0
av = 0
for i in numbers:
    if type(i) == int:
        newList.append(i)
    if type(i) == list:
        for j in i:
            newList.append(j)
n = len(newList)
for i in range(0, n):
    if max < newList[i]:
        max = newList[i]
    if min > newList[i]:
        min = newList[i]
    sum = sum + newList[i]
    av = sum/n

print(max)
print(min)
print(av)
print(newList)
