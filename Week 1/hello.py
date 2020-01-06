
import sys

# define the name


def hello():
    global name
    name = "World"

    # just  first name
    if len(sys.argv) == 2:
        name = sys.argv[1]

    #  first and last name
    elif len(sys.argv) > 2:
        name = sys.argv[1] + " " + sys.argv[2]


# print on the screen
def screen():
    print("Hello " + name + "!")


hello()
screen()

# if len(sys.argv) == 1:
#     print("Hello world!")
# else:
#     print("Hello %s!" % sys.argv[1])
