import numpy as np

# Numero di frame
N = 300

# Genera dati casuali di accelerazione e giroscopio
acceleration_data = np.random.rand(N, 3)  # Genera valori casuali per l'accelerazione
gyro_data = np.random.rand(N, 3)           # Genera valori casuali per il giroscopio

# Combinare i dati di accelerazione e giroscopio in un unico array
sensor_data = np.concatenate((acceleration_data, gyro_data), axis=1)

# Salva i dati nel file
with open('prova.txt', 'w') as file:
    for frame_data in sensor_data:
        line = ' '.join(map(str, frame_data)) + '\n'
        file.write(line)
