import os

def get_portable_filepath(filename: str):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dirpath, filename)
    print(filepath)
    assert os.path.isfile(filepath), f"File {filename} could not be found in directory {dirpath}"
    return filepath

def file_to_list(filepath: str):
    with open(filepath) as f:
        lines = f.readlines()
    return [int(line) for line in lines]