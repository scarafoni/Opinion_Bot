#!/usr/bin/python
import sys
import argparse
#args gramsize from_file -pt print_text -pcsv printcsv
#gramsize-int
#from_file- file we're pulling from, must end in .txt or .csv
#-pt print_text- prints output in text, to file if specified (default option if no arg is specified)
#-ptcsv- prints mtable to csv, to stdio if not specified
parser = argparse.ArgumentParser()
parser.add_argument('-i','--infile'
parser.parse_args()
