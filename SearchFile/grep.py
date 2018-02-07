import re
import argparse

bold = "\033[1m"
reset = "\033[0;0m"
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The word to search for")
parser.add_argument("-w", "--word", help="The word to search for")
args = parser.parse_args()

n = 0
with open(args.file, "r") as file:
    for line in file.readlines():
        result = re.match(args.word, line, re.IGNORECASE)
        if result:
            indexes = result.span(0)
            print(str(n) + ": " + line[0:indexes[0]]
                  + bold + line[indexes[0]:indexes[1]]
                  + reset + line[indexes[1]:-1])
        n += 1
