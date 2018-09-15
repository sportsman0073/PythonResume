# CS 177 - labprep1.py
# Nicholas Koontz
# Following Coding Standards and Guidelines
# This program accepts three values and outputs 2 values
import math

# Prompt the user for edge length of a tetrahedron and the base radius and height of a cone

print("Input an edge length for a tetrahedron")
edge = eval(input())
print("Input a radius of your cone")
radius = eval(input())
print("Input a height of your cone")
height = eval(input())

# Calculate the volume of the tetrahedron: Based on edge length, calculate the volume of the tetrahedron

Vt = ((edge**3)*(2**.5))/12

# Calculate the volume of a cone: Based on its base radius and height, calculate the volume of the cone

Vc = (3.14*(radius**2)*height)/3

# Output (print) the results of the calculations

print("The volume of your tetrahedron is",Vt)
print("The volume of your cone is",Vc)
