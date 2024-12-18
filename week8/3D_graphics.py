from MyPackage.main_pack.rectangle import rect_area, rect_perimeter
from MyPackage.main_pack.circle import area_circle, perimeter

from MyPackage.main_pack.sub_pack.cuboid import  cuboid_surface_area,  cuboid_volume
from MyPackage.main_pack.sub_pack.sphere import sphere_surface_area, sphere_volume


print("Rectangle Area:", rect_area(5, 3))
print("Rectangle Perimeter:", rect_perimeter(5, 3))

print("Circle Area:", area_circle(7))
print("Circle Perimeter:", perimeter(7))

print("Cuboid Surface Area:", cuboid_surface_area(5, 3, 4))
print("Cuboid Volume:", cuboid_volume(5, 3, 4))

print("Sphere Surface Area:", sphere_surface_area(7))
print("Sphere Volume:", sphere_volume(7))


