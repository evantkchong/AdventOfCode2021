#!/usr/bin/env python
import os
import sys
from typing import ItemsView

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def steer_submarine(command_ls: list):
    distance = 0
    aim = 0
    depth = 0
    for command in command_ls:
        match command.split():
            case ["forward", magnitude]:
                magnitude = int(magnitude)
                distance += magnitude
                depth += aim * magnitude
            case ["down", magnitude]:
                aim += int(magnitude)
            case ["up", magnitude]:
                aim -= int(magnitude)
    return distance, depth

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    commands = file_to_list(filepath)
    distance, depth = steer_submarine(commands)
    product = distance * depth
    print(product)