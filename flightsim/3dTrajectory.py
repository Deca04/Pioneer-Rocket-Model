import open3d as o3d
import numpy as np

N = 500  # Numero di campioni da visualizzare
dt = 0.05  # Intervallo di tempo

def integrate(prev_value, delta, dt):
    return prev_value + delta * dt

# Rotazione basata sui dati del giroscopio
def calculate_rotation(gyro, dt):    
    rotation_angles = gyro * dt
    rotation_matrix = o3d.geometry.get_rotation_matrix_from_xyz(rotation_angles)
    return rotation_matrix

# Applicare la rotazione al modello 3D
def apply_rotation(model, rotation_matrix):
    model.rotate(rotation_matrix, center=(0, 0, 0))

# Lettura dei dati dei sensori
with open('data.txt') as file:
    lines = file.readlines()
    sensor_data = np.array([list(map(float, line.strip().split(','))) for line in lines])

# Impostazione posizione e velocità iniziali
pos = np.array([0.0, 0.0, 0.0])
vel = np.array([0.0, 0.0, 0.0])
model = o3d.io.read_triangle_mesh('pioneer.stl')
mesh_coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=200, origin=[0, 0, 0])

# Inizializzazione della scia
tail_points = [pos.copy()]
tail = o3d.geometry.LineSet()
tail.points = o3d.utility.Vector3dVector(tail_points)
tail.lines = o3d.utility.Vector2iVector([])

# Inizializzazione visualizzazione
vis = o3d.visualization.Visualizer()
vis.create_window()
opt = vis.get_render_option()
opt.background_color = np.asarray([0.2, 0.3, 0.4])  # Imposta lo sfondo a un colore bluastro

vis.add_geometry(mesh_coord_frame)
vis.add_geometry(model)
vis.add_geometry(tail)

for i in range(0, N):
    acc = sensor_data[i][:3]
    gyro = sensor_data[i][3:6]  # Assumiamo che i dati del giroscopio siano nelle colonne 4-6
    posz = sensor_data[i][6]

    print(posz)

    delta_v = acc * dt
    vel = integrate(acc, delta_v, dt)

    delta_r = vel * dt
    pos = integrate(vel, delta_r, dt)
    pos = pos + [0,0,posz] # Aggiornamento della componente verticale della posizione
    print(pos)
    
    # Aggiornamento posizione del modello
    model.translate(delta_r)

    # Rotazione
    rotation_matrix = calculate_rotation(gyro, dt)
    apply_rotation(model, rotation_matrix)

    # Aggiornamento scia
    tail_points.append(pos.copy())
    if len(tail_points) > 100:  # Manteniamo solo le ultime 100 posizioni
        tail_points.pop(0)

    tail.points = o3d.utility.Vector3dVector(tail_points)
    lines = [[j, j + 1] for j in range(len(tail_points) - 1)]
    tail.lines = o3d.utility.Vector2iVector(lines)

    # Aggiornamento visualizzazione
    vis.update_geometry(model)
    vis.update_geometry(tail)
    vis.poll_events()
    vis.update_renderer()

vis.destroy_window()
