import math
import numpy
import obj_actions
from stl import mesh
import stl
objects_path = 'tests/stl_binary/'


done = mesh.Mesh.from_file(objects_path + 'cube.stl')
body = mesh.Mesh.from_file(objects_path + 'polyhedron.stl')
obj_actions.combine_objects(done, body, 'pre_move.stl')
obj_actions.arrange_cubes(done, body)
obj_actions.combine_objects(done, body, 'post_move.stl')
