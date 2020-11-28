import math
import numpy
from stl import mesh
import stl


"""cube = mesh.Mesh.from_file(str(objects_path) + "cube.stl")
volume, cog, inertia = cube.get_mass_properties()
print(volume)

print(cube.x.min())"""


# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...




def copy_obj(obj, dims, num_rows, num_cols, num_layers):
    w, l, h = dims
    copies = []
    for layer in range(num_layers):
        for row in range(num_rows):
            for col in range(num_cols):
                # skip the position where original being copied is
                if row == 0 and col == 0 and layer == 0:
                    continue
                _copy = mesh.Mesh(obj.data.copy())
                # pad the space between objects by 10% of the dimension being
                # translated
                if col != 0:
                    translate(_copy, w, 0.1, col, 'x')
                if row != 0:
                    translate(_copy, l, 0.1, row, 'y')
                if layer != 0:
                    translate(_copy, h, 0.1, layer, 'z')
                copies.append(_copy)
    return copies








def distance_x(obj1, obj2):
    return math.fabs(obj2.x.min() - obj1.x.min())


def arrange_cubes(obj1, obj2):
    # obj2 will be stacked around obj1
    cube1 = get_outer_cube(obj1)
    cube2 = get_outer_cube(obj2)
    d = distance(obj1, obj2)
    obj2.x += d


# Using an existing stl file:
main_body = mesh.Mesh.from_file(objects_path + 'oriented.stl')

# rotate along Y
main_body.rotate([0.0, 0.5, 0.0], math.radians(90))

copies = copy_obj(main_body, get_outer_cube(main_body), 2, 2, 2)
