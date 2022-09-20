import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("/home/klc/PU-GAN/data/test/ImageToStl.com_13770_tiger_v1.xyz")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])

downpcd = pcd.voxel_down_sample(voxel_size=0.03)
o3d.visualization.draw_geometries([downpcd])

print(downpcd)
##########################

o3d.io.write_point_cloud("downsampling.xyz", downpcd)
