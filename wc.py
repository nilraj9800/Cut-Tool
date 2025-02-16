import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="file to process")
parser.add_argument("-c", "--file", type=str, default="0")
parser.add_argument("-l", "--line", type=str, default="t")
parser.add_argument("-w", "--word", type=str, default="t")
parser.add_argument("-m", "--character", type=str, default="t")
args = parser.parse_args()
#print(os.path.getsize(args.file))
with open(args.filename, "r", encoding="utf8") as fp:
    data = fp.read()
    data_list = data.split()
    character = 0
    lines = len(fp.readlines())
    if args.line == "T" or args.line == "t" :
        print(lines)
    if args.word == "T" or args.word == "t":
        print(len(data_list))
    if args.character == "T" or args.character == "t":
        print(len(list(data)))
        
        
        
    