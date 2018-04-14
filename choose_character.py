from random import randint
import copy
from random import choice

CHARACTERS = ["elf", "dork", "fork", "superwoman", "man", "last"]

DEPTH = 0

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
        # print character_a_list[0], character_b_list[0]
        return

    full_a = copy.copy(character_a_list)
    full_b = copy.copy(character_b_list)

    while 1:
        character_a = choice(character_a_list) if len(character_a_list) > 1 else character_a_list[0]
        # character_b_list.remove(character_aa)
        character_b = choice(character_b_list) if len(character_b_list) > 1 else character_b_list[0]
        if character_a != character_b:
            break

    character_a_list.remove(character_a)
    character_b_list.remove(character_b)
    # print "debug", full_a, full_b, character_a_list, character_b_list
    print character_a, character_b
    # print
    return choose_characters(full_a, character_b_list), choose_characters(character_a_list, full_b)


if __name__ == "__main__":
    choose_characters(CHARACTERS, copy.copy(CHARACTERS))