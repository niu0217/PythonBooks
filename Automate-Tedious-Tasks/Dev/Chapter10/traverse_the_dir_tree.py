import os

for folderName, subfolders, filenames in os.walk('/Users/niu0217/test'):
    print('The current folder is:  ' + folderName)

    for subfolder in subfolders:
        print('subfolder of ' + folderName + ':  ' + subfolder)

    for filename in filenames:
        print('filename of ' + folderName + ':  ' + filename)

    print('')
