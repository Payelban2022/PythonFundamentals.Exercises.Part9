import json
import os
import pickle
def read_json(filepath):
    f = open(filepath)

    return json.loads(f.read())
path = "/Users/payel/Python/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"
# /Users/payel/Python/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json
data = "Payel"



# define a function
# path to the directory is a string and is given
# return a list containing json objects
def read_all_json_files(filepath):
    list = []
    for path, directories, files in os.walk(filepath):
        for file in files:
            if '.json' in file:
                jsonobject = read_json(filepath + file)
                list.append(jsonobject)
    return list
print(read_all_json_files(path))

# define function
# take file path (given) and data(given)
# write the contents of the json files to a file called **super_smash_characters.pickle**.
# with open create a file at the given path with **super_smash_characters.pickle** name
def write_pickle(filepath, data):
    with open("super_smash_characters.pickle","wb") as f:
        pickle.dumps(path,data,f)
    with open("super_smash_characters.pickle","rb") as rf:
        a = pickle.load(rf)
        b = pickle.load(rf)
    print(a)
    print(b)

# write_pickle("/Users/payel/Python/PythonFundamentals.Exercises.Part9/data/super_smash_bros/")


def load_pickle(filepath):
    with open("super_smash_characters.pickle","rb")as f:
        a = pickle.load(f)
    print(a)
