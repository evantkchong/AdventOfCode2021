#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def parse_input(filepath):
    lines = file_to_list(filepath)
    boards = []
    numbers = [int(i) for i in lines[0].split(",")]
    board = None
    for line in lines[1:]:
        if line.isspace():
            if board:
                boards.append(board)
            board = []
        else:
            board.append([int(i) for i in line.split()])
    boards.append(board)
    return numbers, boards


class BingoBoard:
    def __init__(self, board: list):
        self.board = board
        self.marked_board = self.__get_marking_board(self.board)
        self.t_board = self.__transpose_board(self.board)
        self.t_marked_board = self.__get_marking_board(self.t_board)

    def __get_marking_board(self, board: list):
        marked_board = []
        for row in board:
            marked_row = []
            for _ in row:
                marked_row.append(False)
            marked_board.append(marked_row)
        return marked_board

    def __transpose_board(self, board: list):
        num_rows = len(board)
        num_cols = len(board[0])
        t_board = [[0] * num_rows for _ in range(num_cols)]
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                t_board[j][i] = num
        return t_board

    def p_print_board(self, board):
        rep = ""
        for row in board:
            for num in row:
                rep += f"{num:2}  "
            rep = rep[:-2]
            rep += "\n"
        print(rep)
        return rep

    def draw_number(self, drawn_number: int):
        match = False
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                if num == drawn_number:
                    match = True
                    break
            if match:
                break

        if match:
            self.marked_board[i][j] = True
            self.t_marked_board[j][i] = True

    def check_win(self):
        for row, col in zip(self.marked_board, self.t_marked_board):
            if all(row) or all(col):
                return True
        return False

    def get_unmarked_sum(self):
        running_sum = 0
        for i, j in zip(self.marked_board, self.board):
            for marked, number in zip(i, j):
                if not marked:
                    running_sum += number
        return running_sum


def find_first_winning_board(numbers, boards):
    boards = [BingoBoard(board) for board in boards]
    for number in numbers:
        for board in boards:
            board.draw_number(number)
            if board.check_win():
                return number, board


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    numbers, boards = parse_input(filepath)
    winning_number, winning_board = find_first_winning_board(numbers, boards)
    unmarked_sum = winning_board.get_unmarked_sum()
    final_score = unmarked_sum * winning_number
    print(final_score)
    # 2305 - 0051
