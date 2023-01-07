#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character

        :sentence: a string
    """
    string_length = len(sentence)
    if string_length == 0:
        return (string_length, None)
    return (string_length, sentence[0])
