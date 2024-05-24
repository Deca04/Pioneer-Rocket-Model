import open3d as o3d
import numpy as np

N = 500
dt = 0.05

def integrate(prev_value, delta, dt):
    return prev_value + delta * dt

#rotation from gyro data
def calculate_rotation(gyro, dt):    
    rotation_angles = gyro * dt   
    rotation_matrix = o3d.geometry.get_rotation_matrix_from_xyz(rotation_angles)
    return rotation_matrix

#apply rotation to 3d model
def apply_rotation(model, rotation_matrix):
    model.rotate(rotation_matrix, center=(0, 0, 0))

#sensor data
with open('provaDati.txt') as file:
    lines = file.readlines()
    sensor_data = np.array([list(map(float, line.strip().split())) for line in lines])

#setting initial position and velocity - expamples, not the true simulaiton
pos = np.array((0.0, 0.0, 0.0))
vel = np.array((0.0, 0.0, 100.0))
model = o3d.io.read_triangle_mesh('pioneer.stl')
mesh_coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=200, origin=[0, 0, 0])

tail = o3d.geometry.PointCloud()
tail.points = o3d.utility.Vector3dVector([pos])

#initialize visualization
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh_coord_frame)
vis.add_geometry(model)
vis.add_geometry(tail)

for i in range(0, N):
    acc = sensor_data[i][:3]
    gyro = sensor_data[i][3:]

    delta_v = acc * dt
    vel = integrate(vel, delta_v, dt)

    delta_r = vel * dt
    pos = integrate(pos, delta_r, dt)

    #rotation
    rotation_matrix = calculate_rotation(gyro, dt)
    apply_rotation(model, rotation_matrix)

    #update visualization
    vis.update_geometry(model)
    vis.update_geometry(tail)
    vis.poll_events()
    vis.update_renderer()

vis.destroy_window()
