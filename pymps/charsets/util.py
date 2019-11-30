from typing import List, Tuple


def tuplize_char(char_data: List[str], width: int = 6, height: int = 7) -> Tuple[Tuple[bool]]:
    """ Create tuples defining lines of a bitmap character.

    Given a list of strings which represent a bitmap character, return a list of tuples which contain the full
    character definition.

    Input form: a list of strings, where each character in the string is either a space or a non-space. Each string is
    a line in the character, and each character represent a pixel in the character. If are less lines in `char_data`
    than the specified height then the remaining lines are considered empty. If there are less characters in a line
    then the specified width then the rest of the line is considered empty.

    :param char_data:
    :param width: Width of the output character
    :param height: Height of the output character
    :return: A tuple of size `height` containing tuples of size `width` containing True for each set pixel
    """
    assert len(char_data) <= height, 'character height too long'

    def line_to_tuple(line: str) -> Tuple[bool]:
        assert len(line) <= width, 'character line too long'

        # pad line to desired width if too short
        line = line + (' ' * (width - len(line)))
        return tuple([False if pixel == ' ' else True for pixel in line])

    line_tuples = []
    for i in range(height):
        try:
            line_tuple = line_to_tuple(char_data[i])
        except IndexError:
            line_tuple = line_to_tuple('')

        line_tuples.append(line_tuple)

    return tuple(line_tuples)


def tuplize_col(char_line_data: List[List[str]], line_len=16, char_width=6, char_height=7) -> Tuple[Tuple[Tuple[bool]]]:
    """ Tuplize a list of character data.

    If the provided list is shorter than `line_len` then the remaining characters in the output Tuple will all be blank.

    :param char_line_data:
    :param int line_len:
    :param int char_width: output width of each character
    :param int char_height: output height of each character
    :return: A Tuple containing tuplized characters
    """
    assert len(char_line_data) <= line_len

    line_char_tuples = []
    for i in range(line_len):
        try:
            char_tuple = tuplize_char(char_line_data[i], char_width, char_height)
        except IndexError:
            char_tuple = tuplize_char([], char_width, char_height)

        line_char_tuples.append(char_tuple)

    return tuple(line_char_tuples)


def tuplize_charset(char_lines: List[List[List[str]]], line_len=16, char_width=6, char_height=7) -> Tuple[Tuple[Tuple[bool]]]:
    """ Given a list of lists of character data, tuplize it into an entire character set.

    The output of this function is intended to be an entire character set, usually 256 characters long.

    :param char_lines: List-of-lists of character data, generally one list per 16 character row in the character set diagram
    :param int line_len: Length of each column of character data, generally 16 characters
    :param int char_width: output width of each character
    :param int char_height: output height of each character
    :return: Tuple containing the entire character set for a printer, generally 256 characters.
    """
    char_data = tuple()

    for char_line in char_lines:
        char_data += tuplize_col(char_line, line_len, char_width, char_height)

    return char_data

