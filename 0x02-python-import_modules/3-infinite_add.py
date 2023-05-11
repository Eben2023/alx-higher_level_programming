#!/usr/bin/python3
if __name__ == "__main__":

    args = list(map(int, sys.argv[1:]))

    sum = 0
    for arg in args:
        sum += arg

    print(sum)
