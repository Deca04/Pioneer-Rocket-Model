import open3d as o3d
import numpy as np

# Read 3D model from STL file
body = 'pioneer.stl'

def import_stl(filename):
    mesh = o3d.io.read_triangle_mesh(filename)
    return mesh

model = import_stl(body)

pos = np.array((0.0, 0.0, 0.0))
vel = np.array((2.0, 2.0, 0.0))

mesh_coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=200, origin=[0, 0, 0])

tail = o3d.geometry.PointCloud()
tail.points = o3d.utility.Vector3dVector([pos])

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh_coord_frame)
vis.add_geometry(model)
vis.add_geometry(tail)

N = 3000  # number of frames in the movie
dt = 0.01

# Read acceleration and gyro information from file
with open('provaDati.txt') as file:
    lines = file.readlines()
    sensor_data = np.array([list(map(float, line.strip().split())) for line in lines])

num_frames = min(N, len(sensor_data))  # Adjust num_frames if file has fewer lines
 
for i in range(num_frames):
    acc = sensor_data[i][:3] 
    gyro = sensor_data[i][3:] 

    dv = acc * dt
    vel = vel + dv

    dr = vel * dt
    pos = pos + dr

    model.translate(dr)

    tail.points.extend([pos])

    vis.update_geometry(model)
    vis.update_geometry(tail)
    vis.poll_events()
    vis.update_renderer()

vis.destroy_window()
