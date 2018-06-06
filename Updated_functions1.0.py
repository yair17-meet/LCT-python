import io

# Constants

# Part name
GENERAL_ITEM_NAME = "item"
# number of users
NUMBER_OF_USERS = 5
# Where all files will be split up to (minus the user number)
GENERAL_FOLDER_PATH = "home"
RECOVER_FOLDER_PATH = "homes"

# All Locations
LOCATIONS = dict()

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


def new_file(file_to_save):
    """
    Reads in a new file, splits it up and returns locations
    @param file_to_save (string): Path to original file
    @return items_locations (list<string>): list of location for each item
    """
    # TODO add copies
    lines = get_file_lines(file_to_save)
    
    item_paths = generate_locations(len(lines))
    for i in range(len(item_paths)):
        item_path = item_paths[i]
        with open(item_path, 'w') as ip:
            ip.write(lines[i])

        file_key = get_file_key(file_to_save)
        if file_key in LOCATIONS:
            LOCATIONS[file_key].append(item_path)
        else:
            LOCATIONS[file_key] = [item_path]

# def maintenance(locations):
#     """
#     """
#     missingitems = list ()
#     for i in locations:
#         my_file = Path(i)
#         if my_file.is_file() == False:
#             missingitems.append(i)
    
#     if len(missingitems) == 0:
#         pass
#     pass

def recover_file(file_to_recover):
    """
    @param file_to_recover: the file needed to be recovered
    """
    # Get the file items locations
    recovery_file_path = "%s-%s" % (RECOVER_FOLDER_PATH, file_to_recover)
    with open(recovery_file_path, 'w') as wf:
        for item in LOCATIONS[file_to_recover]:
            with open (item, 'r') as rf:
                wf.write(rf.read())
    return recovery_file_path
        

class InMemoryFile(object):
    def __init__(self, name, content):
        self.name = name
        self.file = io.StringIO(content)
    
    def readlines(self):
        return self.file.readlines()

test_file = InMemoryFile("test_name", """some initial text data
adgas
sagsag
asdga
asgda
sgsasg

blaablaa""")

new_file(test_file)
print(recover_file(test_file.name))

with open(recover_file(test_file.name)) as f:
    print(f.read())
