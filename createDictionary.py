
from stl import mesh
import stl
import os
from collections import OrderedDict
from operator import getitem

class objectDictionary():

    def __init__(self):
        objects_path = 'tests/stl_binary/'
        self.objects = {}
        for filename in os.listdir(objects_path):
            if filename.endswith(".stl"):
                curr_obj={}
                obj = mesh.Mesh.from_file(objects_path + filename)
                curr_obj["X"] = obj.mesh.x.max() - obj.mesh.x.min()
                curr_obj["Y"] = obj.mesh.y.max() - obj.mesh.y.min()
                curr_obj["Z"] = obj.mesh.z.max() - obj.mesh.z.min()
                curr_obj["Volume"]=list[0]*list[1]*list[2]
                self.objects[filename]=curr_obj


    def sortByVolume(self):
        return OrderedDict(sorted(self.objects.items(), key=lambda x: getitem(x[1], 'X')))

    def sortByX(self):
        return OrderedDict(sorted(self.objects.items(), key=lambda x: getitem(x[1], 'Y')))

    def sortByY(self):
        return OrderedDict(sorted(self.objects.items(), key=lambda x: getitem(x[1], 'Z')))

    def sortByZ(self):
        return OrderedDict(sorted(self.objects.items(), key=lambda x: getitem(x[1], 'Volume')))

    def getMaxZ(self):
        max["Z"]=0
        for obj in self.objects:
            if self.objects[obj]["Z"] > max["Z"]:
                max=self.objects[obj]
        return max

"""    def pairByZ(self):
        max = self.objects.getMaxZ()
        for obj in reversed(self.objects):
            if obj == self.objects[obj]:
               break
            else:
                for ppair in self.objects:
                    if self.objects[obj]["Z"]+self.objects[ppair]["Z"] < max["Z"]:
                        return {obj, ppair}"""