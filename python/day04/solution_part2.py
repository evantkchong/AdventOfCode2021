#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from day04.solution_part1 import BingoBoard, parse_input


def find_last_winning_board(numbers, boards):
    boards = [BingoBoard(board) for board in boards]
    last_winning_number = None
    winning_board_idxes = []
    for number in numbers:
        for board_idx, board in enumerate(boards):
            if board_idx in winning_board_idxes:
                continue
            board.draw_number(number)
            if board.check_win():
                last_winning_number = number
                last_winning_board = board
                winning_board_idxes.append(board_idx)
    return last_winning_number, last_winning_board


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    numbers, boards = parse_input(filepath)
    last_winning_number, last_winning_board = find_last_winning_board(numbers, boards)
    unmarked_sum = last_winning_board.get_unmarked_sum()
    final_score = unmarked_sum * last_winning_number
    print(final_score)
    # 0052 - 0110
