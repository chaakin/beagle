import time
import os, sys
from random import shuffle

### Read ~/mp3/ listing and play list of files

path = '/root/mp3/'
dirs = os.listdir(path)
shuffle(dirs)

for song in dirs:
    print('Playing song: %s' % song)
    os.system('mpg321 %s"%s"' % (path,song))
