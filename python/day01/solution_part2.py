#!/usr/bin/env python
import os
import sys
from typing import ItemsView

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def sliding_window_count(report_ls: list, window_size: int = 3):
    count = 0
    num_windows = len(report_ls) - window_size + 1
    prev_sum = float('inf')
    for i in range(num_windows):
        cur_sum = sum(report_ls[i: window_size + i])
        if cur_sum > prev_sum:
            count += 1
        prev_sum = cur_sum
    return count


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    report_ls = file_to_list(filepath)
    report_ls = [int(i) for i in report_ls]
    print(sliding_window_count(report_ls, 3))
