#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def count_depth_increase(report_ls: list):
    count = 0
    prev_depth = report_ls[0]
    for cur_depth in report_ls[1:]:
        if prev_depth < cur_depth:
            count += 1
        prev_depth = cur_depth
    return count


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    report_ls = file_to_list(filepath)
    print(count_depth_increase(report_ls))
