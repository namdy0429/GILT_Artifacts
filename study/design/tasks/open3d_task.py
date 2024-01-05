import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    pcd_point_cloud = o3d.data.DemoCropPointCloud()
    pcd = o3d.io.read_point_cloud(pcd_point_cloud.point_cloud_path)

    with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(
            pcd.cluster_dbscan(eps=0.1, min_points=10, print_progress=True)
        )

    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("Accent")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

    bunny = o3d.data.BunnyMesh()
    bunny_mesh = o3d.io.read_triangle_mesh(bunny.path)
    bunny_mesh.compute_vertex_normals()
    bunny_mesh.transform([[-1, 0, 0, 0], 
                          [0, 1, 0, 0], 
                          [0, 0, 1, 0], 
                          [0, 0, 0, 1]])
    bunny_mesh.translate([2.5, 2.1, 1.2])

    vol = o3d.visualization.read_selection_polygon_volume(
                                pcd_point_cloud.cropped_json_path
                            )
    chair = vol.crop_point_cloud(pcd)
    chair.paint_uniform_color([1, 1, 1])

    dists = pcd.compute_point_cloud_distance(chair)
    dists = np.asarray(dists)
    ind = np.where(dists > 0.01)[0]
    pcd_without_chair = pcd.select_by_index(ind, invert=True)

    o3d.visualization.draw_plotly([pcd_without_chair, bunny_mesh],
                                    window_name="Open3D",
                                    width=1200,
                                    height=800,
                                    mesh_show_wireframe=True,
                                    zoom=0.3412,
                                    front=[0.5, -0.2, -0.8],
                                    up=[-0.1, -1.0, 0.2])
