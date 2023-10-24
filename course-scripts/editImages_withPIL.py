from PIL import Image
import os
import re

received_images = '~/images'
dest_dir = '/opt/icons/'

def convert_images():
  #checking if the directories exists or if I made a typo above
  if os.path.isdir(received_images) and os.path.isdir(dest_dir):
    
    for x in os.listdir(received_images):
      #test line to check contents# print(‘Current file: ’, x)
      #next 2 lines exclude a .DS_store file that caused issues
      file_name = re.search(r'^(\w+)', x)
      if file_name is not None:
        new_file_name = dest_dir + file_name[1]
        #testline: print(‘New file name: ’, new_file_name)
        
        #rewrite ‘x’ as a full file path for Image.open()
        x = received_images + '/' + file_name[1]
        new_x = Image.open(x)
        
        #file needed to convert to RGB first
        new_x = new_x.convert(‘RGB’)
        new_x.rotate(90).resize((128,128)).save(new_file_name, format=‘JPEG’)
        
  else:
    print('Either the directory with received images or destination directory does not exist.')

convert_images()
