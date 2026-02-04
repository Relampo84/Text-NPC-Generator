from values_file import name_pool, surname_pool, gender_pool
import json, csv
import random
import os

def loadID():
    with open("data.json", "r") as f:
        id = json.load(f)
        return id

def updateId(id):
    with open("data.json", "w") as f:
        json.dump(id, f,indent=4)
        return id

def fill_digits(num):
    return f"{num:03}"

def getId():
    latestID = loadID()["npc_ID"]
    newestId = latestID +1
    newValue = {"npc_ID":newestId}
    updateId(newValue)
    return latestID


def negateId():
    ID = loadID()["npc_ID"]
    newestId = ID - 1
    newValue = {"npc_ID":newestId}
    updateId(newValue)

def generate_attributes():
    gender = random.choice(list(gender_pool))
    gender_ID = gender_pool[gender]

    name = random.choice(list(name_pool[gender]))
    name_id = fill_digits(name_pool[gender][name])

    surname = random.choice(list(surname_pool))
    surname_id = fill_digits(surname_pool[surname])

    age = random.randint(10,60)
    age_map = fill_digits(age)

    identifier = getId()

    seed = f"""{name_id}{surname_id}{age_map}{gender_ID}{identifier}"""
    return name, surname, gender, age, identifier, seed

def netejar():
    os.system("cls" if os.name == "nt" else "clear")

def get_attribute(IDname,IDmiddle_name,gender):
    name = list(name_pool[gender])[IDname]
    middle_name = list(surname_pool)[IDmiddle_name-1]
    return name, middle_name

def check_npc_storage(seed):
    IDname = int("".join(list((seed[0],seed[1],seed[2]))))
    IDmiddle_name = int("".join(list((seed[3],seed[4],seed[5]))))
    age = int("".join(list((seed[6],seed[7],seed[8]))))
    gender = "male" if seed[9] == "M" else "female"
    id = "".join(["".join(seed[i]) for i in range(10,len(seed))])
    name, middle_name = get_attribute(IDname,IDmiddle_name,gender)
    return name, middle_name, gender, age, id, seed

def show_npc(name, middle_name, gender, age, id, seed):
    print(f"""\
Name = {name} {middle_name}
Gender = {gender}
Age = {age}
ID = {id}
seed = {seed}
""")

def check_seed_in_storage(seed): 
    with open("npc_storage.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["seed"] == seed:
                return True
        return False