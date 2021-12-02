#!/usr/bin/env python
import os
import sys
from typing import ItemsView

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from utils import file_to_list


def move_submarine(command_ls: list):
    distance = 0
    depth = 0
    for command in command_ls:
        match command.split():
            case ["forward", magnitude]:
                distance += int(magnitude)
            case ["down", magnitude]:
                depth += int(magnitude)
            case ["up", magnitude]:
                depth -= int(magnitude)
    return distance, depth

# def clean_instructions(commands: list):
#     command_ls = []
#     for command in commands:
#         direction, magnitude = command.split()
#         command_ls.append((direction, int(magnitude)))
#     return command_ls

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    commands = file_to_list(filepath)
    # command_ls = clean_instructions(commands)
    distance, depth = move_submarine(commands)
    product = distance * depth
    print(product)