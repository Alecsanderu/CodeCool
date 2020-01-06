
# Write the anagram recogniser that accepts a file name from the user provided as the command line argument of the
#  script,
# reads each line of that file, and displays those pairs of words which are anagrams in separated lines.
import sys


def check_anagram(line1, line2):
    letters_in_word = sorted(line1)
    letters_in_word2 = sorted(line2)
    if letters_in_word == letters_in_word2:
        return True
    else:
        return False


def print_result(w1, w2):

    word1 = w1.rstrip()
    word2 = w2.rstrip()
    print("{}    {}".format(word1, word2))


try:
    file_name = sys.argv[1]

except Exception:
    print("\nTry this: /usr/bin/python3.8 /media/alex/e920e2ae-74d4-4835-8814-02915252ed46/Projects/CodeCool/anagrams.py anagrams.csv  \n")
    sys.exit(1)

print(file_name)

anagram_file = open(file_name, "r")
for line in anagram_file:

    anagram_file2 = open(file_name, "r")
    for line2 in anagram_file2:

        if check_anagram(line, line2) and line != line2:
            print_result(line, line2)
    anagram_file2.close()


anagram_file.close()
