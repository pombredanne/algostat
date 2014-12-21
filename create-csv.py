#!/usr/bin/env python
"""
Create a CSV file from the output generated by algostat.py
"""
import sys
import fileinput
from operator import itemgetter

from algorithm import ALGORITHMS

DELIMITER = ","


def write_header():
    sys.stdout.write(DELIMITER.join(["repository"] + [algo for algo in sorted(ALGORITHMS)]) + "\n")


def write_line(line):
    algorithms = {key: 0 for key in ALGORITHMS}
    columns = line.split(" ")
    repo = columns[0]

    for algo in columns[1:]:
        values = algo.split(":")
        algorithms[values[0]] += int(values[1])

    sorted_results = sorted(algorithms.items(), key=itemgetter(0))
    sys.stdout.write(DELIMITER.join([repo] + [str(count) for algo, count in sorted_results]) + "\n")


if __name__ == '__main__':
    write_header()
    for line in fileinput.input():
        write_line(line)
