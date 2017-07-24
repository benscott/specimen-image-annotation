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


def get_image(images):
    """
    Loop through images and try and regex match a barcode
    :param images:
    :return:
    """
    for image in images:
        result = re_title.match(image['title'])
        try:
            barcode = result.group(1)
        except AttributeError:
            continue
        else:
            # Successfully matched barcode - so return image
            return {
                'barcode': barcode,
                'url': image['identifier']
            }

def main():
    dir = os.path.dirname(os.path.realpath(__file__))

    count = 0

    with open(os.path.join(dir, 'src', 'phthiraptera.csv'), 'rU') as csvfile:
        for row in csv.reader(csvfile):
            irn = row[0]
            try:
                images = json.loads(row[1])
            except ValueError:
                # Could not parse json
                continue

            image = get_image(images)
            if image:
                # Save image to fuse
                req = requests.post('http://127.0.0.1:5000/api/transcription/', json=image)


if __name__ == "__main__":
    main()