import re


def abbreviate(words):

    words_list = re.split("[^A-Z']+", words.upper())
    letters = [word[0] for word in words_list]
    return "".join(letters)


print(abbreviate("ce faci ma"))
