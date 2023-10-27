#!/usr/bin/env python3

import requests
import os
import re

# lab provided website IP
web_server_url = 'http://<lab external IP>/upload/'
supplier_images = 'supplier-data/images'

def upload_images():
  for x in os.listdir(supplier_images):
    
    # search for .jpeg files since the folder has .tiff files too
    file_name = re.search(r'(\d+\.jpeg)', x)
    if file_name is not None:
      
      file_path = supplier_images + '/' + x
      with open(file_path, 'rb') as opened_file:
        post_image = requests.post(web_server_url, files={'file':opened_file})
        post_image.raise_for_status()

def main():
  upload_images()

if __name__ == '__main__':
  main()
