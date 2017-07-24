#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '22/07/2017'.
"""

import os
import csv

def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir, 'src', 'country_irns.csv'), 'rU') as csvfile:
        for row in csv.reader(csvfile):
            print('{id: %s, name: "%s"},' % (row[1], row[0]))


if __name__ == "__main__":
    main()