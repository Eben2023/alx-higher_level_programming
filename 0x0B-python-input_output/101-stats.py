#!/usr/bin/python3
"""Module for print_metrics"""


import sys

def print_metrics(file_sizes, status_codes):
    """
    Prints the computed metrics.

    Args:
        file_sizes (list): List of file sizes.
        status_codes (dict): Dictionary of status codes and their counts.

    Returns:
        None
    """

    total_size = sum(file_sizes)
    print(f"File size: {total_size}")

    for status_code in sorted(status_codes):
        count = status_codes[status_code]
        print(f"{status_code}: {count}")

def compute_metrics():
    """
    Reads stdin line by line and computes metrics.

    Returns:
        None
    """

    file_sizes = []
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            parts = line.strip().split()
            file_size = int(parts[-1])
            status_code = parts[-2]

            file_sizes.append(file_size)
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(file_sizes, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_sizes, status_codes)
        raise
