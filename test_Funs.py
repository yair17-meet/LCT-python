import os
import sys
import random

def unique_id (file_to_save, dict_id_to_name):
    t=5
    while t>2:
        t= 5
        a = random.randint(0,99999999)
        for i in dict_id_to_name:
            if i != a:
                t=0
    dict_id_to_name[str(a)] = file_to_save
    return dict_id_to_name
    

dictidtoname = {'1':'name1', '2':'name2'}
filetosave = 'name3'
dictidtoname = unique_id(dictidtoname, filetosave)
print (dictidtoname)
