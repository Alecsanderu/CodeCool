def palindrome(str):
    str = str.lower()
    get_rid_white_space = str.replace(" ", "")
    str_list = list(get_rid_white_space)
    print(str_list)
    reversedl = str_list[::-1]
    print(reversedl)
    print(type(str_list))
    print(type(reversedl))
    if str_list == reversedl:
        return True
    else:
        return False
    return


def main():
    user_input = input("enter word/phrase: ").lower()
    palindrome(user_input)
    return


if __name__ == '__main__':
    main()
