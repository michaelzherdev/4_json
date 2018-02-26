import json
import os
from sys import argv


def load_data(filepath):
    with open(os.path.abspath(filepath), encoding="utf8") as f:
        text = f.read()
    return text


def pretty_print_json(data):
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        json_data = load_data(argv[1])
        pretty_print_json(json_data)
    except IndexError:
        print("Please, enter path to text file. See README.md.")
    except FileNotFoundError:
        print("No such file or directory. Please provide a valid file path.")
