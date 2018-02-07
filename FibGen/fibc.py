import argparse


def print_fib(length, verbose, print_to_file):
    a, b = 0, 1
    for i in range(length):
        a, b = b, a + b
        if verbose:
            print(a)
    if not verbose:
        print(a)
    if print_to_file:
        f = open("fib.txt", "w")
        f.write(str(a) + "\n")
        f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help="Creates fibonacci numbers this many times", type=int, required=True)
    parser.add_argument("-o", help="Save to file", action="store_true")
    parser.add_argument("-v", "--verbose", help="Print the process", action="store_true")
    args = parser.parse_args()
    print_fib(args.length, args.verbose, args.o)


if __name__ == '__main__':
    main()
