#!/usr/bin/python3
"""Module for print_metrics"""
import sys


def print_metrics(status_codes, total_size):
    """
    Print the computed metrics based on the provided statistics.

    Args:
        status_codes (dict): A dictionary containing the status codes and their counts.
        total_size (int): The total file size.

    Returns:
        None
    """

    print("File size: {}".format(total_size))

    for status_code in sorted(status_codes):
        count = status_codes[status_code]
        print("{}: {}".format(status_code, count))


def compute_metrics():
    """
    Read stdin line by line and compute metrics based on the input.

    Returns:
        None
    """

    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            try:
                parts = line.split()
                status_code = parts[-2]
                file_size = int(parts[-1])

                if status_code in status_codes:
                    status_codes[status_code] += 1

                total_size += file_size

                if count % 10 == 0:
                    print_metrics(status_codes, total_size)

            except Exception:
                pass

    except KeyboardInterrupt:
        print_metrics(status_codes, total_size)
        raise


if __name__ == '__main__':
    compute_metrics()
