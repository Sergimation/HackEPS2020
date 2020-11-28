import math
from stl import mesh
import numpy as np
import stl


class Object:

    def __init__(self, mesh: mesh.Mesh):
        self.x = 0
        self.y = 0
        self.z = 0
        self.mesh = mesh

        def get_outer_cube(obj):
            width = obj.x.max() - obj.x.min()
            length = obj.y.max() - obj.y.min()
            height = obj.z.max() - obj.z.min()
            return width, length, height

        self.box = get_outer_cube(mesh)

    def distance(self, obj):
        return math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 + (obj.z - self.z) ** 2)

    def combine(self, obj, output_f='result.stl'):
        combined = mesh.Mesh(numpy.concatenate([self.mesh.data, obj.data]))

        combined.save(output_f, mode=stl.Mode.BINARY)

    def save(self, output_f='result.stl'):
        self.mesh.save(output_f, mode=stl.Mode.BINARY)

    def translate(self, step: np.float32, padding: np.float32, axis):
        if 'x' == axis:
            items = 0, 3, 6
            self.x += step + padding
        elif 'y' == axis:
            items = 1, 4, 7
            self.y += step + padding
        elif 'z' == axis:
            items = 2, 5, 8
            self.z += step + padding
        else:
            raise RuntimeError('Unknown axis %r, expected x, y or z' % axis)

        # _solid.points.shape == [:, ((x, y, z), (x, y, z), (x, y, z))]
        self.mesh.points[:, items] += step + padding

