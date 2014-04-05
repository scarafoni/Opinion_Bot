#!/usr/bin/python
import sys
import argparse
#args gramsize from_file -pt print_text -pcsv printcsv
#gramsize-int
#from_file- file we're pulling from, must end in .txt or .csv
#-pt print_text- prints output in text, to file if specified (default option if no arg is specified)
#-ptcsv- prints mtable to csv, to stdio if not specified
init_args = argparse.ArgumentParser()
init_args.add_argument('input', help='the input file to be read, must be either .csv (probability table) or .txt (plain text)',
                       type=argparse.FileType('r')) 
init_args.add_argument('output', help='specify the output of the file, must be either .txt (plain text) or .csv (markov table), if non specified, will print plain text to stdio',
                       type=argparse.FileType('r'),
                       default=sys.stdout)
init_args.parse_args()
