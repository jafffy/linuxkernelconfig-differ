#!/usr/bin/python3

import sys

def process(Aconfig_file, Bconfig_file):
    pass

def main():
    Aconfig_path = sys.argv[1]
    Bconfig_path = sys.argv[2]

    with open(Aconfig_file, 'r') as Aconfig_file:
        with open(Bconfig_file, 'r') as Bconfig_path:
            process(Aconfig_file, Bconfig_file)

main()
