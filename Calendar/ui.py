
def print_schedule_for_day(table):
    for meeting in table:
        meeting_title = meeting[0]
        meeting_duration = int(meeting[1])
        meeting_start_time = int(meeting[2])
        meeting_end_hour = meeting_start_time + meeting_duration
        # print("Your Schedule for Today:")
        print(meeting_start_time, "-", meeting_end_hour, meeting_title)
    pass


def print_menu(title, list_options):
    print("{0}:".format(title))
    option_character = 0
    element_for_character = 0
    for option in list_options:
        print("    ({0}) {1}".format(
            list_options[element_for_character][option_character], option))
        element_for_character += 1


def get_inputs(title_list, title):
    print(title)
    inputs = [input(label) for label in title_list]
    return inputs


def print_text(string):
    print(string)
