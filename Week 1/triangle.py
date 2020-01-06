print("Write numbers between -100 and 100 to calculate the area of your triangle!" + "\n")
a = input("a = ")
b = input("b = ")
c = input("c = ")
d = input("d = ")
e = input("e = ")
f = input("f = ")

print("\n")
A = "A = (" + str(a) + "," + str(b) + ")"
B = "B = (" + str(c) + "," + str(d) + ")"
C = "C = (" + str(e) + "," + str(f) + ")"

print(A + "\n" + B + "\n" + C + "\n")

area = abs((int(a)*(int(d)-int(f))+int(c) *
            (int(f)-int(b))+int(e)*(int(b)-int(d)))/2)
print("Area of your triangle:" + "\n")
print(area)
