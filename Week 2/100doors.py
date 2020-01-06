
# gasit pe net

# usile = [x * 0 for x in range(101)]

# print(usile)

# print("The following doors are open:")
# for i in range(1, 101):
#     for j in range(1, 101):
#         if i % j == 0:
#             if usile[i] == 0:
#                 usile[i] = 1
#             else:
#                 usile[i] = 0
# for x in range(100):
#     if usile[x] == 1:
#         print(x)


# explicat de mihai

usi = [0] * 100

pas = 1

while pas <= 100:
    for i in range(pas-1, len(usi), pas):
        if usi[i] == 0:
            usi[i] = 1
        elif usi[i] == 1:
            usi[i] = 0
    pas = pas + 1

for x in range(100):
    if usi[x] == 1:
        print(x+1)
