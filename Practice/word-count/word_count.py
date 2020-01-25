import string
import re
import collections


def count_words(sentence):
    words = [word.strip(string.punctuation).lower() for word in
             re.split(f"[,_{string.whitespace}]", sentence)]
    word_counter = collections.Counter()
    for word in words:
        if word:
            word_counter[word] += 1

    return word_counter
