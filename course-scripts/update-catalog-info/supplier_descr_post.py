#!/usr/bin/env python3

import requests
import os
import re

supplier_descr = 'supplier-data/descriptions'
# lab provided website IP
web_server_url = 'http://<lab external ip>/fruits/'

def upload_descriptions():
  for x in os.listdir(supplier_descr):

    # expecting 003.txt
    file_name = re.search(r'(\d+)(\.txt)', x)
    if file_name is not None:

      file_path = supplier_descr + '/' + x
      with open (file_path, 'r') as f:
        contents = f.read()
        lines = contents.split('\n')

        weight = re.search(r'(\d+)', lines[1])
        weight = int(weight[0])
        ass_ima = file_name[1] + '.jpeg'
        descr_dict = {"name": lines[0], "weight": weight, "description": lines[2], "image_name": ass_ima}

        upload_descr = requests.post(web_server_url, json=descr_dict)
        upload_descr.raise_for_status()

def main():
  upload_descriptions()
if __name__ == '__main__':
  main()
