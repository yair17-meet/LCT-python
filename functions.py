import os
import sys
import random

generalfolderpath = 'Newf1\\user'
filetosave = 'testFILE.txt'
numberofusers = 5
numberofcopies = 3
dictidtoname = dict()
generalitemname = 'fileitem'


def save_new_file (general_folder_path, file_to_save, number_of_users,
                   general_item_name):
    location_data = list()
    with open(file_to_save, 'r') as rf:
        i=1
        for line in rf:
            a = 4
            folder = 4
            while a>2:
                a=0
                folder = random.randint(1,number_of_users)
                
                try:
                    with open(general_folder_path+str(folder)+"\\"+
                              general_item_name+str(i)+'.txt'):
                        a=4
                except:
                    y=7
            with open(general_folder_path+str(folder)+'\\'+general_item_name+
                      str(i)+'.txt', 'w') as wf:
                wf.write(line)
                location_data.append(general_folder_path+str(folder)+
                                    '\\'+general_item_name+str(i)+'.txt')
                i=i+1
    return location_data        



def recover_file (data_):
    with open('recovered_file.txt', 'w') as wf:
        for dataitem in data_:
            with open(str(dataitem), 'r') as rf:
                for line in rf:
                    wf.write(line)
    return 'all done!'





data = list()
temp_data = list()
for i in range(numberofcopies):
    temp_data = save_new_file(generalfolderpath, filetosave,
                         numberofusers, generalitemname)
    for dataitem in temp_data:
        data.append(dataitem)
print(data)
#recover_file(data)

