import os
import sys
import random

def save_new_file (finalfolderpath, filetosave):
    i=1
    locationdata = list()
    with open(filetosave, 'r') as rf:
    
        for line in rf:
            s = 'aaa',i,'.txt'
            with open(str(finalfolderpath)+str(i)+'.txt', 'w') as wf:
                wf.write(line)
                locationdata.append(finalfolderpath+str(i)+'.txt')
                i=i+1           
    return locationdata




data = list()
data = save_new_file('Newf1\FileItem', 'testFILE.txt')


#--------------------------------------------------------
# the function takes the future location for the parts
# and the name of the original file (who must be in the same folder as
# the code) and returns a list of the locations of the parts.
