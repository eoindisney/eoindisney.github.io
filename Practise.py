#Practise

import matplotlib.pyplot as plt

# Sample data for backscatter and interferometer information
range_gate = [1, 2, 3, 4, 5]
intensity = [10, 20, 15, 25, 30]
x_interferometer = [0.1, 0.2, 0.3, 0.4, 0.5]
y_interferometer = [0.5, 0.4, 0.3, 0.2, 0.1]
z_interferometer = [0.3, 0.2, 0.4, 0.1, 0.5]

# Plotting the backscatter and interferometer information
plt.plot(range_gate, intensity, label='Backscatter')
plt.plot(range_gate, x_interferometer, label='X Interferometer')
plt.plot(range_gate, y_interferometer, label='Y Interferometer')
plt.plot(range_gate, z_interferometer, label='Z Interferometer')

plt.xlabel('Range Gate')
plt.ylabel('Intensity')
plt.title('Backscatter and Interferometer Data')
plt.legend()
plt.grid(True)
plt.show()
