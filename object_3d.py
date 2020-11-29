import math
from stl import mesh
import numpy as np
import stl

# rotate along Y
# main_body.rotate([0.0, 0.5, 0.0], math.radians(90))


class Object:

    def __init__(self, mesh: mesh.Mesh):
        self.x = 0
        self.y = 0
        self.z = 0
        self.mesh = mesh
        self.width = self.mesh.x.max() - self.mesh.x.min()
        self.length = self.mesh.y.max() - self.mesh.y.min()
        self.height = self.mesh.z.max() - self.mesh.z.min()

    def pos(self):
        return self.x, self.y, self.z

    def distance(self, obj):
        return math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 + (obj.z - self.z) ** 2)

    def distance_x(self, obj):
        return obj.x - self.x

    def distance_y(self, obj):
        return obj.y - self.y

    def distance_z(self, obj):
        return obj.z - self.z

    def combine_n_save(self, obj, output_f='result.stl'):
        combined = mesh.Mesh(np.concatenate([self.mesh.data, obj.mesh.data]))

        combined.save(output_f, mode=stl.Mode.BINARY)

    def copy(self):
        return Object(mesh.Mesh(self.mesh.data.copy()))

    def translate(self, distance, axis):
        if 'x' == axis:
            items = 0, 3, 6
            self.x += distance
        elif 'y' == axis:
            items = 1, 4, 7
            self.y += distance
        elif 'z' == axis:
            items = 2, 5, 8
            self.z += distance
        else:
            raise RuntimeError('Unknown axis %r, expected x, y or z' % axis)

        # _solid.points.shape == [:, ((x, y, z), (x, y, z), (x, y, z))]
        self.mesh.points[:, items] += distance

    def intersects_with(self, obj):
        return (self.x <= obj.x and self.x + self.width >= obj.x + obj.width) and \
               (self.y <= obj.y and self.y + self.length >= obj.y + obj.length) and \
               (self.z <= obj.z and self.z + self.height >= obj.z + obj.height)

    def move_to(self, position: (float, float, float)):
        for point, axis in zip(position, ('x', 'y', 'z')):
            if 'x' == axis:
                self.translate(point - self.x, axis)
            if 'y' == axis:
                self.translate(point - self.y, axis)
            if 'z' == axis:
                self.translate(point - self.z, axis)

    def move(self, variations: (float, float, float)):
        for variation, axis in zip(variations, ('x', 'y', 'z')):
            if 'x' == axis:
                self.translate(variation, axis)
            if 'y' == axis:
                self.translate(variation, axis)
            if 'z' == axis:
                self.translate(variation, axis)


