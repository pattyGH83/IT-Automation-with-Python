#!/usr/bin/env python3

from PIL import Image
import os
import re   

supplier_images = 'supplier-data/images'
def convert_image():
  for x in os.listdir(supplier_images):
    # regex incase we have files that are not 003.tiff
    file_name = re.search(r'(\d+)(\.tiff)', x)
    if file_name is not None: 

      new_file = supplier_images + '/' + file_name[1] + '.jpeg'
      file_path = supplier_images + '/' + x
      convert_file = Image.open(file_path)
      
      # convert to RGB first
      convert_file = convert_file.convert('RGB')
      convert_file.resize((600,400)).save(new_file, format='JPEG')

def main():
  convert_image()

if __name__ == '__main__':
  main()
