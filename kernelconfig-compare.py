#!/usr/bin/python3

import sys

def process(Aconfig_file, Bconfig_file, Aheader, Bheader):
    if Aheader == '':
        Aheader = 'A'
    if Bheader == '':
        Bheader = 'B'

    # TODO: Put the code to set file pointer to initial position.
    A = { line.strip(' \n') for line in Aconfig_file if not line.startswith('#') }
    B = { line.strip(' \n') for line in Bconfig_file if not line.startswith('#') }

    with open(Aheader + '_and_' + Bheader + '.txt', 'w') as f:
        for d in A & B:
            if d != '':
                f.write(d + '\n')
    with open(Aheader + '_minus_' + Bheader + '.txt', 'w') as f:
        for d in A - B:
            if d != '':
                f.write(d + '\n')
    with open(Bheader + '_minus_' + Aheader + '.txt', 'w') as f:
        for d in B - A:
            if d != '':
                f.write(d + '\n')

def main():
    Aconfig_path = sys.argv[1]
    Bconfig_path = sys.argv[2]

    Aheader = ''
    Bheader = ''

    if len(sys.argv) == 5:
        Aheader = sys.argv[3]
        Bheader = sys.argv[4]

    with open(Aconfig_path, 'r') as Aconfig_file:
        with open(Bconfig_path, 'r') as Bconfig_file:
            process(Aconfig_file, Bconfig_file, Aheader, Bheader)

main()
