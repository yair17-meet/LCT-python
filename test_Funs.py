import os
import sys
import random


def unique_id(file_to_save, dict_id_to_name):
    t = 5
    while t > 2:
        t = 5
        a = random.randint(0, 99999999)
        for i in dict_id_to_name:
            if i != a:
                t = 0
    dict_id_to_name[str(a)] = file_to_save
    return dict_id_to_name


dictidtoname = {'1': 'name1', '2': 'name2'}
filetosave = 'name3'
dictidtoname = unique_id(filetosave, dictidtoname)
# print (dictidtoname)

#######################################


# Eilon's suggestion
from uuid import uuid4
from hashlib import sha256
from base64 import b64encode as b64


def get_hash(name):
    return b64(sha256((names[i].encode())).digest())  # shorter by len
    # or
    # return sha256((names[i].encode())).hexdigest()

dictidtoname = {}
number_of_ids = 5

names = ['name' + str(i) for i in range(number_of_ids)]

for i in range(number_of_ids):
    # for same id for same value
    dictidtoname[get_hash(names[i])] = names[i]
    # for random id
    # dictidtoname[uuid4()]=names[i]

print(dictidtoname)
print(len(str(dictidtoname)))
