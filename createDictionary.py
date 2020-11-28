import obj_actions
from stl import mesh
import stl
import os
from collections import OrderedDict
from operator import getitem
objects_path = 'tests/stl_binary/'
objects = {}

def create_dictionary():
    for filename in os.listdir(objects_path):
        if filename.endswith(".stl"):
            curr_obj={}
            obj = mesh.Mesh.from_file(objects_path + filename)
            list = obj_actions.get_outer_cube(obj)
            curr_obj["X"]=list[0]
            curr_obj["Y"]=list[1]
            curr_obj["Z"]=list[2]
            curr_obj["Volume"]=list[0]*list[1]*list[2]
            objects[filename]=curr_obj

def sortByVolume(dict):
    return OrderedDict(sorted(dict.items(), key=lambda x: getitem(x[1], 'X')))

def sortByX(dict):
    return OrderedDict(sorted(dict.items(), key=lambda x: getitem(x[1], 'Y')))

def sortByY(dict):
    return OrderedDict(sorted(dict.items(), key=lambda x: getitem(x[1], 'Z')))

def sortByZ(dict):
    return OrderedDict(sorted(dict.items(), key=lambda x: getitem(x[1], 'Volume')))

create_dictionary()






