import sys


def display_ideas():
    with open("ideas.txt", "r") as ideabank:
        for i, line in enumerate(ideabank):
            print('{}.{}'.format(i+1, line.strip()))
        ideabank.close()
        exit()


def deleteLine(index):
    # print(index)
    with open('ideas.txt', 'r') as ideabank:
        data = ideabank.read().splitlines(True)
        data.pop(index-1)
    with open('ideas.txt', 'w') as ideabank:
        ideabank.writelines(data)


if len(sys.argv) == 2 and sys.argv[1] == "--list":
    display_ideas()

elif len(sys.argv) == 3 and sys.argv[1] == "--delete":
    deleteLine(int(sys.argv[2]))
    print("After deletion: ")
    display_ideas()


else:
    with open("ideas.txt", "a") as ideabank:
        idea = input("what is your new idea?")
        ideabank.write(idea + "\n")
        ideabank.close()
    display_ideas()
