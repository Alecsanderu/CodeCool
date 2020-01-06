# Present participle form
# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.

# A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add -ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, replace ie with y and add -ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding -ing
# By default just add -ing
# Write the script which takes infinitive verbs separated by one space as the
# command line arguments and displays their present participle form in separated lines.


def ending(i):
    one = i[-3:-2]
    two = i[-2:-1]
    three = i[-1:0]
    consonant = "qwrtzpsdfghjklyxcvbnm"
    vowel = "aeiuo"
    if one in consonant and two in vowel and three in consonant:
        return True
    else:
        return False


def make_ing_form(i):
    new_verb = ""
    exception = ['be', 'see', 'flee', 'knee']
    if i.endswith("ie"):
        new_verb = i[0:len(i)-2] + "ying"
    elif i.endswith("e") and i not in exception:
        new_verb = i[0:len(i)-1] + "ing"
    elif ending(i):
        new_verb = i[0:len(i)-1] + i[-1:0] + "ing"
    else:
        new_verb = i + "ing"
    return new_verb


print(make_ing_form("see"))
print(make_ing_form("hug"))
