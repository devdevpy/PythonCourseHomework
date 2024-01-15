import string

list_ = {"a", "e", "i", "o", "u", "y"}
list_2 = ("b", "c", "d", "f", "g", "h")
alphabet = set(string.ascii_lowercase)
syllables = alphabet - list_
syllables2 = (letter for letter in alphabet if letter not in list_)

print(syllables)
print(tuple(syllables2))


def syllables_gen():
    for letter in alphabet:
        yield letter


print(tuple(syllables_gen()))


user_input = set(string.ascii_lowercase)


def syllables_gen(user_input):
    for letter in user_input:
        if letter in syllables:
            yield letter


def list_gen(user_input):
    for letter in user_input:
        if letter in syllables:
            yield letter


print(tuple(syllables_gen(user_input)))
print(tuple(list_gen(user_input)))

print(tuple(letter for letter in user_input if letter in syllables))
print(tuple(letter for letter in user_input if letter in list_))