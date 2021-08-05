
# For any characters and phrase, checking if phrase is aa permutation of characters
characters = input('input a string for "characters"')
phrase = input('input another string for "phrase"')

def generate_phrase(characters, phrase):

    if len(characters) != len(phrase):
        return False

    for i in characters:
        if i in phrase:
            phrase = phrase.replace(i,"")
    return len(phrase) == 0

# checking the example case
print(generate_phrase(characters,phrase))

characters = "cbacba"
phrase = "aabbccc"

def generate_phrase(characters, phrase):

    if len(characters) != len(phrase):
        return False

    for i in characters:
        if i in phrase:
            phrase = phrase.replace(i,"")
    return len(phrase) == 0

print(generate_phrase(characters,phrase))






