import os
import json
import argparse
import click

def formatter(string, sort_keys=True, indent=4):
    return json.dumps(json.loads(string), sort_keys=sort_keys, indent=indent)

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--sort', '-s', is_flag=True, help='Sort keys alphabetically')
def main(path, sort):
    with open(path, 'r') as f:
        string = f.read()
    print(formatter(string, sort_keys=sort))
    
if __name__ == '__main__':
    main()
