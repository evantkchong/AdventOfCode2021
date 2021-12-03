#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


# def construct_binary_tree(report_ls: list):
#     tree = {}
#     item_length = len(report_ls[0])
#     for item in report_ls:
#         tree_access = tree
#         for i, bit in enumerate(item):
#             if i == item_length - 1:
#                 if bit not in tree_access:
#                     tree_access[bit] = 1
#                 else:
#                     tree_access[bit] += 1
#                 break
#             else:
#                 if bit not in tree_access:
#                     tree_access[bit] = {}
#             tree_access = tree_access[bit]
#     return item_length, tree


# def construct_count_map(report_ls: list):
#     count_map = {}
#     item_length = len(report_ls[0])
#     for item in report_ls:
#         for i in range(1, item_length):
#             key = item[:i]
#             if key in count_map:
#                 count_map[key] += 1
#             else:
#                 count_map[key] = 1
#     return count_map


def get_ratings(report_ls: list, most_common: bool = True):
    cur_pos = 0
    while len(report_ls) != 1:
        zeros = []
        ones = []
        for item in report_ls:
            if item[cur_pos] == "0":
                zeros.append(item)
            else:
                ones.append(item)
        cur_pos += 1
        if most_common:
            report_ls = ones if len(ones) >= len(zeros) else zeros
        else:
            report_ls = zeros if len(zeros) <= len(ones) else ones
    assert len(report_ls) == 1
    return report_ls[0]


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    diagnostic_report = file_to_list(filepath)
    report_ls = [line.strip() for line in diagnostic_report]
    oxygen_generator_bin = get_ratings(report_ls, True)
    co2_scrubber_bin = get_ratings(report_ls, False)
    oxygen_generator_rating, co2_scrubber_rating = int(oxygen_generator_bin, 2), int(
        co2_scrubber_bin, 2
    )
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(life_support_rating)
