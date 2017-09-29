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

from PIL import Image

from resizeimage import resizeimage


def main():
    dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    count = 0

    path = os.path.join(dir, 'src', 'assets', 'slides')

    out_path = os.path.join(dir, 'src', 'assets', 'resized_slides')

    size = 1300, 522

    for f in os.listdir(path):
        fp = os.path.join(path, f)
        if os.path.isfile(os.path.join(path, f)):
            with open(fp, 'r+b') as f:
                with Image.open(f) as image:
                    # im = image.convert("RGB")
                    fn = os.path.basename(fp)
                    image.thumbnail(size, Image.ANTIALIAS)
                    image.save(os.path.join(out_path, fn), "JPEG")

                    # print(image.size)
                    # return

                    # slides

                    # print(im)
                    # rs = resizeimage.resize_contain(im, [800, 800])
                    # fn = os.path.basename(fp)
                    # print(im.format)
                    # rs.save(os.path.join(out_path, fn), im.format)
                    # # out_path
                    #
                    # print(fn)
                    # return

            # barcode = f.split('_')[0]
            # specimen = {
            #     'barcode': barcode,
            #     'file_name': f
            # }
            # r = requests.post('http://127.0.0.1:5000/api/specimen/', json=specimen)
            # r.raise_for_status()

if __name__ == "__main__":
    main()
