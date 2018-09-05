from itertools import product

valid_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

invalid_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                  [6, 7, 2, 1, 9, 0, 3, 4, 8],
                  [1, 0, 0, 3, 4, 2, 5, 6, 0],
                  [8, 5, 9, 7, 6, 1, 0, 2, 0],
                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                  [9, 0, 1, 5, 3, 7, 2, 1, 4],
                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                  [3, 0, 0, 4, 8, 1, 1, 7, 9]]


class Validator:
    SUDOKU_SIZE = 9
    SQUARES_CENTERS = ([1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7])

    def __init__(self, board):
        self.board = board

    def get_neighbors(self, pos):
        """
        Get all 8 neighbors of a cell
        :param pos: row, column separated by comma
        :return (list): is valid or not
        """
        neighbors = []
        for i in list(product([-1, 0, 1], [-1, 0, 1])):
            neighbors.append(self.board[pos[0] + i[0]][pos[1] + i[1]])

        return neighbors

    def get_row(self, i):
        """
        Get a row at index i
        :param i: row's index
        :return (list): sorted integers that are in the row
        """
        return sorted([self.board[i][j] for j in range(self.SUDOKU_SIZE)])

    def get_column(self, i):
        """
        Get a column at index i
        :param i: column's index
        :return (list): sorted integers that are in the column
        """
        return sorted([self.board[i][j] for j in range(self.SUDOKU_SIZE)])

    def get_square(self, square_center):
        """
        Get a unit square with center at square_center
        :param square_center: square center as a list or tuple
        :return (list): sorted integers that are in the square
        """
        return sorted(self.get_neighbors(square_center))

    def validate_unit(self, sudoku_part):
        """
        Validate a fundamental unit of sudoku
        :param sudoku_part: row, column or unit square as a list
        :return (bool): is valid or not
        """
        return True if sudoku_part == list(range(1, self.SUDOKU_SIZE + 1)) else False

    def validate_solution(self):
        """
        Validate a whole sudoku, row by row, column by column and unit square by unit square
        :return (bool): is valid or not
        """
        # Validation of rows and columns
        for i in range(self.SUDOKU_SIZE):
            if self.validate_unit(self.get_row(i)) and self.validate_unit(self.get_column(i)):
                pass
            else:
                return False

        # Validation of squares
        for c in self.SQUARES_CENTERS:
            if self.validate_unit(self.get_square(c)):
                pass
            else:
                return False

        return True


def main():
    validator = Validator(invalid_sudoku)
    if validator.validate_solution():
        print('Great job! You have just solved this sudoku!')
    else:
        print('Something is wrong. Check your solution again.')


if __name__ == '__main__':
    main()
