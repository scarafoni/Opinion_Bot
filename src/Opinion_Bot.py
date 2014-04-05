#!/usr/bin/python
import sys
import argparse
#args gramsize from_file -pt print_text -pcsv printcsv
args = argparse.ArgumentParser(usage='%(prog)s [options]')
args.add_argument('input', help='the input file to be read, must be either .csv (probability table) or .txt (plain text)',
                  type=argparse.FileType('r')) 
args.add_argument('gramsize',help='the gramsize to be used for the processing, default 1',
                  type=int)
args.add_argument('-o','--output', help='specify the output of the file, must be either .txt (plain text) or .csv (markov table), if non specified, will print plain text to stdio',
                  type=argparse.FileType('w'),
                  default=sys.stdout)
argv = args.parse_args()


argv.output.write(argv.input.read())
