import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    return json.dumps(json.loads(string), sort_keys=sort_keys, indent=indent)

def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as f:
        string = f.read()
    print(formatter(string, sort_keys=sort_keys))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a JSON formatter.')
    parser.add_argument('--sort', action='store_true', help='sort keys')
    args = parser.parse_args()
    main(sys.argv[-1], no_sort=False)
