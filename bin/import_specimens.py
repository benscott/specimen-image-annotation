#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '22/07/2017'.
"""

import re
import os
import csv
import json
import requests

# Match image titles - 010660092_816406_1430512
re_title = re.compile('([0-9]+)_[0-9]+_[0-9]+')


def main():
    dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    count = 0

    path = os.path.join(dir, 'src', 'assets', 'slides')
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            barcode = f.split('_')[0]
            specimen = {
                'barcode': barcode,
                'file_name': f
            }
            r = requests.post('http://74.50.49.136:5000/api/specimen/', json=specimen)
            r.raise_for_status()

if __name__ == "__main__":
    main()
