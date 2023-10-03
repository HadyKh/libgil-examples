# %%
import igl
import scipy as sp
import numpy as np
from meshplot import plot, subplot, interact

# %%
# N by 3 matrix which stores the coordinates of the vertices
# Each row represents the coordinates of a vertex in 3D space
# The columns of the V matrix represent the x, y, and z coordinates of each vertex.
# Column 1 (first column) represents the x-coordinates of all vertices.
# Column 2 (second column) represents the y-coordinates of all vertices.
# Column 3 (third column) represents the z-coordinates of all vertices.
V = np.array([
    [0., 0, 0],
    [1, 0, 0],
    [1, 1, 1],
    [2, 1, 0]
])

# Triangle Connectivity Matrix
# Stores information about how the vertices are connected to form triangles.
# Each row represents a triangle & values within each row are indices that point to rows of the V matrix.
# These indices indicate which vertices from the V matrix are used to define each triangle.

F = np.array([
    [0, 1, 2],
    [1, 3, 2]
])

# %%
plot(V, F)
# %%
