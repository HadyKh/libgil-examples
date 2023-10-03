# %%
import igl
from meshplot import plot
# %%
v, f = igl.read_triangle_mesh('bunny.off')
plot(v, f)

# %%
igl.write_triangle_mesh('bunny.obj')
