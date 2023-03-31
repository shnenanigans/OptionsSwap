import os
import json
from tkinter import messagebox

#finds all your multimc instances in case they are not grouped
def find_instances(multi):
    #mylist = os.listdir("".join(multi) + "\\instances")
    mylist = os.listdir(multi + "\\instances")
    try:
        mylist.remove("instgroups.json")
        mylist.remove("_LAUNCHER_TEMP")
    except:
        pass
    mylist.sort()
    return mylist

#find group names from instgroups.json file
def find_groups(multi):
    groups = []
    try:
        #f = open("".join(multi) + "\\instances\\instgroups.json", "r")
        with open(multi + "\\instances\\instgroups.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError or OSError:
        return groups
    
    for k, v in data.items():
        if k=="groups":
            for k, v in v.items():
                groups.append(k)
    return groups

#find instances in a particular group from instgroups.json file
def find_instances_from_groups(group, multi):
    instances = []
    try:
        f = open("".join(multi) + "\\instances\\instgroups.json", "r")
        data = json.load(f)
    except FileNotFoundError or OSError:
        return instances
    finally:
        f.close()
    for k, v in data.items():
        if k=="groups":
            for k, v in v.items():
                if k==group:
                    instances = v["instances"]
    instances.sort()
    return instances
