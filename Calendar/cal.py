import ui
import storage as st

file = '/media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/CALENDAR/Calendar/meeting.txt'


def main():
    while True:
        schedule_for_day()
        handle_menu()
        choose()



def handle_menu():
    options = ["schedule a new meeting",
               "cancel an existing meeting",
               "quit"]
    ui.print_menu("Main Menu", options)


def choose():
    input = ui.get_inputs(["Please choose the letter : "], "")
    option = input[0]

    if option == "s":
        table = st.get_table_from_file(file)
        schedule(table)
    elif option == "c":
        table = st.get_table_from_file(file)
        cancel_meeting(table)
    elif option == "q":
        ui.print_text("Thank you for using our calendar!")
        exit()
    else:
        ui.print_text("No Valid Input!Please try again \n")


def schedule(table):
    table = st.get_table_from_file(file)
    ui.print_text("Schedule a new meeting:\n")
    title_list = ['Enter a meeting title: ',
                  'Enter duration in hours (1 or 2): ', 'Enter start time: ']
    inputs = ui.get_inputs(title_list, "Please enter info")

    if not check_if_input_is_float_or_int(inputs[0], 'int', "Duration and Start Time"):
        anwser = check_if_input_is_float_or_int(inputs[0], 'int', "Duration and Start Time")
        return ui.print_text(anwser)

    for line in table:
        if int(line[2]) == int(inputs[2]):
            return ui.print_text("ERROR: Meeting overlaps with existing meeting!")

        elif (int(inputs[2]) + int(inputs[1])) > 18 or int(inputs[2]) < 8:
            return ui.print_text("ERROR: Meeting is outside of your working hours (8 to 18)!")


    table.append(inputs)
    st.write_table_to_file(file, table)
    ui.print_text("Meeting added")

    return table


def cancel_meeting(table):
    table = st.get_table_from_file(file)
    ui.print_text("Canceling a meeting.\n")
    title_list = ["Enter Start Time: "]
    inputs = ui.get_inputs(title_list, "")
    for line in table:
        if int(line[2]) == int(inputs[0]):
            table.remove(line)
            ui.print_text("Meeting canceled")
        else:
            ui.print_text("No Meeting at that hour")
    st.write_table_to_file(file, table)
    return table


def sort_meetings(table):
    sorted_list = sorted(table, key=lambda x: x[2])
    return sorted_list


def schedule_for_day():
    table = st.get_table_from_file(file)
    ui.print_text("Your Schedule For Today:")
    if len(table) == 0:
        ui.print_text("   (empty)")
    else:
        ui.print_schedule_for_day(table)

def check_if_input_is_float_or_int(_input, _type, name_of_input):
    if _type == "float":
        try:
            float(_input)
            if float(_input) < 0:
                return "{0} must be bigger than or equal to 0!".format(name_of_input)
            else:
                return True
        except ValueError:
            return " {0} must be a number!".format(name_of_input)
    elif _type == "int":
        try:
            int(_input)
            if int(_input) < 0:
                return "{0} must be bigger than or equal to 0!".format(name_of_input)
            else:
                return True
        except ValueError:
            return "{0} must be an integer!".format(name_of_input)


def check_hours (table,inputs):
    for line in table:
            if int(line[2]) == int(inputs[2]):
                return "ERROR: Meeting overlaps with existing meeting!"

            elif (int(inputs[2]) + int(inputs[1])) > 18 or int(inputs[2]) < 8:
                return "ERROR: Meeting is outside of your working hours (8 to 18)!"


if __name__ == "__main__":
    main()
