import re
import subprocess
import os

checkOldUserName = 'jane'
setNewUserName = 'jdoe'

oldToNew = {}
referenceFile = 'oldUserdataFileNames.txt'
referenceDirectory = 'userdata/'

def filloldToNew():
  with open(referenceFile, 'r') as oldUserdataFileNames:
    for i in oldUserdataFileNames:
      oldFileName = re.search(re.escape(checkOldUserName) + r'(_.+)', i)
      if oldFileName:
        newFileName = setNewUserName + oldFileName[1]
        oldToNew[oldFileName[0]] = newFileName
      else:
        print("Search failed.")
  #print('This output is for testing purposes. \n{}'.format(oldToNew))

def replaceNames():
  for key, value in oldToNew.items(): 
    oldFullPath = referenceDirectory + key
    newFullPath = referenceDirectory + value
    if os.path.isfile(oldFullPath):

      #print('This statement is for testing purposes. \nOld file path: {} \nNew file name: {}'.format(oldFullPath, newFullPath))
      #break

      subprocess.run(['mv', oldFullPath, newFullPath])
    else:
      print("Old path not found.")

filloldToNew()
replaceNames()
