import os
import tempfile
import argparse
import json


def print_data(path, key):
    data = read_data(path)
    if data == {}:
        print(None)
    else:
        try:
            print(*data[key], sep=", ")
        except KeyError:
            print(None)

def read_data(path):
    if os.path.getsize(path) > 0:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    else:
        return {}


def write_data(path, key, value):
    if os.path.exists(path):
        data = read_data(path)
        if key in data and value not in data.values():
            data[key].append(value)
            with open(path, 'w') as file:
                json.dump(data, file)
        if key in data and value in data.values():
            return
        if key not in data:
            data[key] = [value]
            with open(path, 'w') as file:
                json.dump(data, file)

    else:
        with open(path, 'w') as file:
            data = {key: [value]}
            json.dump(data, file)


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="enter key")
    parser.add_argument("--val", help="enter value")
    args = parser.parse_args()
    return args


def main(path):
    args = arguments()
    try:
        if args.key and args.val:
            write_data(path, args.key, args.val)
        elif args.key:
            print_data(path, args.key)
        else:
            print()
    except FileNotFoundError:
        print(None)

if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
