#Practise

import matplotlib.pyplot as plt

# Sample data for backscatter
range_gate = [1, 2, 3, 4, 5]
intensity = [10, 20, 15, 25, 30]

# Plotting the backscatter information
plt.plot(range_gate, intensity)
plt.xlabel('Range Gate')
plt.ylabel('Intensity')
plt.title('Backscatter')
plt.grid(True)
plt.show()