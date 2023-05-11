#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Ignore the first argument (the script name)
    result = sum(int(arg) for arg in args)
    print(result)
