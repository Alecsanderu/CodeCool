

while True:
    command = input("Please specify a command [list, add, mark, archive]:")
    if command == "add":
        add_comand = input("Add an item:")

        with open('todo.txt', "r+") as f:
            index = len(f.readlines())
            f.write("{0} {}".format(index + 1) + add_comand + "/n")

    elif command == "list":
        print("You saved the following to-do items:")
        with open('/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/todo.txt', 'r') as f:
            for line in f:
                print(line, end="")

    elif command == "mark":
        print("You saved the following to-do items:")
        with open('/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/todo.txt', 'r') as f:
            for line in f:
                print(line, end="")
        with open('/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/todo.txt', 'r') as f:
            saved_list = f.readlines()
        mark_index = int(input("Which one would you like to mark: "))
        with open('/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/todo.txt', 'w') as f:
            for i, line in enumerate(saved_list):
                if i == (mark_index - 1):
                    print("\n" + line[7:] + "completed ,\n")
                    f.write(line[:3] + "[x]" + line[6:])
    elif command == "archive":
        with open('/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/todo.txt', 'r') as f:
            data = f.read().splitlines(True)
            data.pop()
        print("All completed tasks got deleted.")
