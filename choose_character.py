from random import randint
import copy
from random import choice

CHARACTERS = ["elf", "dork", "fork", "superwoman", "rick", "42"]

DEPTH = 0

CHOSEN_A = set()
CHOSEN_B = set()


def randomize_character_pointer(character_list, restriction=None):
    if len(character_list) == 1:
        return 0
    possible_pointers = range(0, len(character_list)-1)
    if restriction:
        possible_pointers.remove(restriction)
    return choice(possible_pointers)


def choose_characters(character_a_list, character_b_list):
    if not character_a_list or not character_b_list:
        return

    if len(character_a_list) == len(character_b_list) == 1:
        return

    full_a = copy.copy(character_a_list)
    full_b = copy.copy(character_b_list)

    character_a = choice(character_a_list) if len(character_a_list) > 1 else character_a_list[0]
    character_b = choice(character_b_list) if len(character_b_list) > 1 else character_b_list[0]
    if character_a == character_b:
        return choose_characters(full_a, full_b)

    character_a_list.remove(character_a)
    character_b_list.remove(character_b)
    # if not (character_a in CHOSEN_A and character_b in CHOSEN_B):
    print character_a, character_b

    return choose_characters(full_a, character_b_list), choose_characters(character_a_list, full_b)


def get_characters(characters):
    counter = int()
    characters_a = characters
    characters_b = copy.copy(characters)
    while characters_a:
        chosen_a = choice(characters_a)
        while characters_b:
            chosen_b = choice(characters_b)
            if chosen_a != chosen_b:
                print chosen_a, chosen_b
            characters_b = filter(lambda x: x != chosen_b, characters_b)
            counter += 1
        characters_a = filter(lambda x: x != chosen_a, copy.copy(characters_a))
        characters_b = copy.copy(characters_a)
    print
    print "# of steps {}".format(counter)


if __name__ == "__main__":
    # print len(set(CHARACTERS))
    get_characters(CHARACTERS)
    quit()
    choose_characters(CHARACTERS, copy.copy(CHARACTERS))