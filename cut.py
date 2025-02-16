import sys
import argparse
import csv
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--row", type=str, default=1)
parser.add_argument("-d", "--delimiter", type=str, default='\t')
parser.add_argument("-n", "--filename", type=str)
parser.add_argument("-f", "--range", type=str)
args = parser.parse_args()

range_num = args.range.split()
range_n = int(range_num[-1])

if args.filename == "-":
    file_name = "fourchords.csv"
else:
    file_name = args.filename
    
row_list = ["f0", "f1", "f2", "f3", "f4"]
row_name = row_list.index(args.row)
with open(file_name) as fd:
    rd = csv.reader(fd, delimiter=args.delimiter, quotechar='"')
    for row in rd:
        print(row[:range_n])