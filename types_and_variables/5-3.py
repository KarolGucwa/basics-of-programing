###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
l = int(input('a='))
w = int(input('b='))
h = int(input('h='))
volume = l * w * h
surface_area = 2 * (l*w + w*h + l*h)
print(volume, surface_area)