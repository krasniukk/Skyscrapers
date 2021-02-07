"""The module checks if board has a winning combination or not.
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    board = []
    with open(path, 'r') as file:

        for line in file:

            if '\n' in line:
                board.append(line[:-1])

            else:
                board.append(line)

    return board


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    visibility = 0
    prev_house = 0

    for house in range(1, 6):

        if int(input_line[house]) > prev_house:
            visibility += 1
            prev_house = int(input_line[house])

    if visibility == pivot:
        return True

    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*',\
    '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*',\
    '*41532*', '*2*1***'])
    False
    """
    for line in range(1, 6):

        for row in range(1, 6):

            if board[line][row] == '?':
                return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*',\
    '*41532*', '*2*1***'])
    False
    """
    for line in range(1, 6):
        buildings = {}

        for row in range(1, 6):
            buildings[board[line][row]] = buildings.setdefault(
                board[line][row], 0) + 1

        if len(buildings.keys()) != 5:
            return False

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa) and
    buildings of unique height.

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """

    for line in range(1, 6):

        if board[line][0] != '*':

            if not left_to_right_check(board[line], int(board[line][0])):
                return False

        if board[line][-1] != '*':

            if not left_to_right_check(board[line][::-1], int(board[line][-1])):
                return False

    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and
    visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    reversed_board = []

    for row in range(7):
        new_line = ''

        for line in range(7):
            new_line += board[line][row]

        reversed_board.append(new_line)

    if not check_uniqueness_in_rows(reversed_board) or \
        not check_horizontal_visibility(reversed_board):
        return False

    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)

    if not check_not_finished_board(board):
        return False

    if not check_uniqueness_in_rows(board):
        return False

    if not check_horizontal_visibility(board) or not check_columns(board):
        return False

    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))

