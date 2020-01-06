word = input("What is your word?: ")
word = word.lower()
print(word)
vowel = 'aeiouy'
word_consonants = []
word_vowels = []
for letter in word:
    if letter in vowel:
        word_vowels.append(letter)
    if letter not in vowel:
        word_consonants.append(letter)
print("".join(word_vowels))
print("".join(word_consonants))
