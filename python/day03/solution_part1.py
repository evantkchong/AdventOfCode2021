#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def get_binary_rates(report_ls: list):
    ones_count = [0] * len(report_ls[0])
    for item in report_ls:
        for i, bit in enumerate(item):
            if bit == "1":
                ones_count[i] += 1

    gamma = ""
    epsilon = ""
    for i, bit_count in enumerate(ones_count):
        if bit_count > (len(report_ls) - bit_count):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    diagnostic_report = file_to_list(filepath)
    report_ls = [line.strip() for line in diagnostic_report]
    gamma_bin, epsilon_bin = get_binary_rates(report_ls)
    gamma, epsilon = int(gamma_bin, 2), int(epsilon_bin, 2)
    power_consumption = gamma * epsilon
    print(power_consumption)
