# %%
import igl
import scipy as sp
import meshplot as mp

# %%
v, f = igl.read_triangle_mesh('D:/Medsoft/test/libigl/libgil-examples/bumpy.off')
mp.plot(v, f)

# %%
# Gaussian curvature on a continuous surface is defined as the product of the principal curvatures
k = igl.gaussian_curvature(v, f)
mp.plot(v, f, k)

# %%
# To calculate integral average, we to get the massmatrix first
# The Voronoi mass matrix is a matrix used in numerical simulations, particularly finite element methods,
# to describe the distribution of mass in a mesh.
# The Voronoi mass matrix is a matrix used in numerical simulations, particularly finite element methods,
# to describe the distribution of mass in a mesh
m = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_VORONOI)

# %%
# m is the mass matrix computed in the previous step.
# m.diagonal() extracts the diagonal of the mass matrix m.
# 1 / m.diagonal() computes the reciprocal of each element in the diagonal.
# sp.sparse.diags(...) creates a sparse diagonal matrix with these reciprocals,
# This matrix is used for operations related to the inverse of the mass matrix.
minv = sp.sparse.diags(1 / m.diagonal())

# %%
# minv is the sparse diagonal matrix containing the reciprocals of the diagonal elements of the mass matrix.
# minv.dot(k) performs a matrix-vector multiplication, effectively applying the inverse of the mass matrix 
# to the matrix or vector k.
kn = minv.dot(k)

mp.plot(v, f, kn)
