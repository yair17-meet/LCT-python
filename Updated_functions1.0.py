import io
import os
import random
import shutil

# Constants

# Part name
GENERAL_ITEM_NAME = "item"
# number of users
 
MISSING_USERS = list()
NUMBER_OF_USERS = 5
AVAILABLE_USER_IDS = set(range(NUMBER_OF_USERS))
# Where all files will be split up to (minus the user number)
GENERAL_FOLDER_PATH = "home"
RECOVER_FOLDER_PATH = "homes"

# All Locations
LOCATIONS = dict()
USERS = dict()
for i in range(NUMBER_OF_USERS):
    USERS[i] = True
print(USERS)
# Number of copies
NUMBER_OF_COPIES = 3

def get_user_path(user_id):
    return "%s_%s" % (GENERAL_FOLDER_PATH, user_id)

def generate_locations(num_of_items):
    paths = []
    for i in range(num_of_items):
        paths.append("%s-%d.%d" % (GENERAL_FOLDER_PATH, i % NUMBER_OF_USERS, i))
    return paths


def get_file_key(file):
    if isinstance(file, str):
        return file
    elif isinstance(file, InMemoryFile):
        return file.name


def get_file_lines(file):
    lines = []
    if isinstance(file, str):
        with open(file_to_save) as f:
            lines = f.readlines()
    elif isinstance(file, InMemoryFile):
        lines = file.readlines()
    return lines


def get_file_items(file):
    return get_file_lines(file)


def write_items(item, item_path_template, user_ids):
    for user_id in user_ids:
        item_path = item_path_template % user_id
        with open(item_path, 'w') as item_file:
            item_file.write(item)


def distribute_items(file, items):
    # TODO figure out file versioning
    # Raise an exception if file key alread exists
    file_dict = dict()

    for item_id in range(len(items)):
        file_dict[item_id] = random.sample(AVAILABLE_USER_IDS, NUMBER_OF_COPIES)
        item_path_template = get_item_path_template(file, item_id)
        # send/write items
       # print (item_path_template)
        write_items(items[item_id], item_path_template, file_dict[item_id])
    
    return file_dict


def get_item_path_template(file, item_id):
    file_key = get_file_key(file)
    return "%s_%%d/%s.%d" % (GENERAL_FOLDER_PATH, file_key, item_id)


def get_item_path(file, item_id, user_id):
    return get_item_path_template(file, item_id) % user_id


def find_item(file, item_id):
    file_key = get_file_key(file)
    first_user = LOCATIONS[file_key][item_id][0]
    pass
    

def new_file(file_to_save):
    """
    Reads in a new file, splits it up and returns locations
    @param file_to_save (string): Path to original file
    @return items_locations (list<string>): list of location for each item
    """
    # TODO add copies
    items = get_file_items(file_to_save)
    file_dict = distribute_items(file_to_save, items)
    
    file_key = get_file_key(file_to_save)
    LOCATIONS[file_key] = file_dict


def recover_file(file_to_recover):
    """
    @param file_to_recover: the file needed to be recovered
    """
    recovery_file_path = "%s-%s" % (RECOVER_FOLDER_PATH, file_to_recover)
    with open(recovery_file_path, 'w') as wf:
        for i in range(len(LOCATIONS[file_to_recover])):
            user_id = LOCATIONS[file_to_recover][i][0]
            with open(get_item_path(file_to_recover, i, user_id), 'r') as rf:
                wf.write(rf.read())
    
    return recovery_file_path


def maintain(file_to_check):
    missingitems = dict()
    file_dict = LOCATIONS[file_to_check]
    for item_id in range(len(file_dict)): 
        user_ids = file_dict[item_id]
        missing_user_ids = list()
        for user_id in user_ids:
            if not os.path.isfile(get_item_path(file_to_check, item_id, user_id)):
                missing_user_ids.append(user_id)
        if len(missing_user_ids) > 0:
            missingitems[item_id] = missing_user_ids
    return missingitems

def maintain_detect_user():
    missing_users = list()
    for i in range(NUMBER_OF_USERS):
        if not os.path.isdir(get_user_path(i)):
            missing_users.append(i)
            
    for i in missing_users:
        MISSING_USERS.append(i)
    return missing_users

def maintain_detect_items_on_user(missing_users):
    items_on_missing_user = dict()
    for file_name in LOCATIONS:
        user_with_items = int()
        items = list()
        for item in range(len(LOCATIONS[file_name])):
            
            for user in LOCATIONS[file_name][item]:
                for i in missing_users:
                    if user==i:
                            items.append(item)
                            #del LOCATIONS[file_name][item][user]
                            user_with_items = user
        items_on_missing_user[user_with_items] = items
    for missing_user in missing_users:
        for file_name in LOCATIONS:
            for item in LOCATIONS[file_name]:
                try:
                    LOCATIONS[file_name][item].remove(missing_user)
                except:
                    pass
                    
                
    return items_on_missing_user
                        
def maintain_recover(user_to_item_list, file_name):
    for user in list(user_to_item_list.keys()):
        for item in user_to_item_list[user]:
            a = 1
            rnd = int()
            while a < 3:
                rnd = random.randint(0,(NUMBER_OF_USERS-1))
                a = 5
                for i in MISSING_USERS:
                    if rnd == i:
                        a = 1
                    elif rnd in LOCATIONS[file_name][item]:
                        a = 1
                        
            
            
            ref_user = LOCATIONS[file_name][item][0]
            ref_item_path_template = get_item_path_template(file_name, item)
            ref_item_path = ref_item_path_template % ref_user
            #print(ref_item_path)
            with open(ref_item_path) as ref_item_file:
                
        
                item_path_template = get_item_path_template(file_name, item)
                item_path = item_path_template % rnd
                with open(item_path, 'w') as item_file:
                    item_file.write(str(ref_item_file))
           
            LOCATIONS[file_name][item].append(rnd)
    

class InMemoryFile(object):
    def __init__(self, name, content):
        self.name = name
        self.file = io.StringIO(content)
    
    def readlines(self):
        return self.file.readlines()


test_file = InMemoryFile(u"test_name", u"""some initial text data
adgas
sagsag
asdga
asgda
sgsasg

blaablaa""")

for i in range(NUMBER_OF_USERS):
    if not os.path.exists(get_user_path(i)):
        os.makedirs(get_user_path(i))
        
        
new_file(test_file)
with open(recover_file(test_file.name)) as f:
    print(f.read())

# del LOCATIONS['test_name'][1][1]
#item_id = 3
#user_id = LOCATIONS[test_file.name][item_id][0]
#print("user id: %d" % user_id)
#item_path = get_item_path(test_file.name, item_id, user_id)
#print("exists: %s" % os.path.exists(item_path))
#print("remove result: %s" % os.remove(item_path))
#print("maintain result: %s" % maintain(test_file.name))

#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
print()
print()
print()
list1 = os.listdir(get_user_path(1))# dir is your directory path
number_files1 = len(list1)
print ("number of items on disconnected user: "+str(number_files1))
print("list1 : "+str(list1))
shutil.rmtree(get_user_path(1))
disconnected_users = maintain_detect_user()
print ('disconnected users: '+str(disconnected_users))
#print(LOCATIONS)
disconnected_users_to_items= maintain_detect_items_on_user(disconnected_users)
print ("dict of missing user to items on it: " + str(disconnected_users_to_items))
print(LOCATIONS)
maintain_recover(disconnected_users_to_items,'test_name')
print(LOCATIONS)



















# with open(recover_file(test_file.name)) as f:
#     print(f.read())


# TODO June 13th
# 1. Handle users going offline
# 2. Handle file versioning

# TODO June 20th
# 1. rename recover_file to get_file
# 2. Split maintain into detect & recover, detect will update LOCATIONS and recover will scan LOCATIONS to recover missing copies. Start with implementing recover.
