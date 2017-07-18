#!/usr/bin/python3

import sys

def process(Aconfig_file, Bconfig_file):
    # TODO: Put the code to set file pointer to initial position.
    A = { line.strip(' \n') for line in Aconfig_file if not line.startswith('#') }
    B = { line.strip(' \n') for line in Bconfig_file if not line.startswith('#') }

    with open('A_and_B.txt', 'w') as f:
        for d in A & B:
            if d != '':
                f.write(d + '\n')
    with open('A_minus_B.txt', 'w') as f:
        for d in A - B:
            if d != '':
                f.write(d + '\n')
    with open('B_minus_B.txt', 'w') as f:
        for d in B - A:
            if d != '':
                f.write(d + '\n')

def main():
    Aconfig_path = sys.argv[1]
    Bconfig_path = sys.argv[2]

    with open(Aconfig_path, 'r') as Aconfig_file:
        with open(Bconfig_path, 'r') as Bconfig_file:
            process(Aconfig_file, Bconfig_file)

main()
