# %%
import igl
import meshplot as mp

# %%
v, f = igl.read_triangle_mesh('D:/Medsoft/test/libigl/libgil-examples/bumpy.off')
mp.plot(v, f)

# %%
# Gaussian curvature on a continuous surface is defined as the product of the principal curvatures
k = igl.gaussian_curvature(v, f)
mp.plot(v, f, k)
