#!/usr/bin/python3
def no_c(my_string: str) -> str:
    """ function that removes all characters c and C from a string.

        :my_string: a string with c and C characters
    """
    if (my_string):
        new_string = list(my_string)
        for character in new_string:
            if character in "cC":
                new_string.remove(character)
        return "".join(new_string)
