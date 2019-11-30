from typing import List, Tuple


def tuplize_char(char_data: List[str], width: int = 6, height:int = 7) -> Tuple[Tuple[bool]]:
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


