# Q2
def is_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


def user_input_word():
    word = input("Input a word need to count characters")
    if is_number(word) == True:
        return print("word need be in (a - z):")

    else:
        print("Character counter:", count_character(word))


def count_character(word):
    word = word.lower()
    character_count = {}
    for character in word:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


user_input_word()
