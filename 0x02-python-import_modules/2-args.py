#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num = len(args)
    print("{} argument{}:".format(num, 's' if num != 1 else ''))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
