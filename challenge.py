import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic seabed terrain with hydrothermal vents
np.random.seed(42)
x = np.linspace(-50, 50, 100)
y = np.linspace(-50, 50, 100)
x, y = np.meshgrid(x, y)

# Create a seabed terrain with valleys and vent peaks
z = -np.sqrt(x**2 + y**2) + np.random.normal(0, 1, size=x.shape)
vent_coords = [(-20, -20), (10, 15), (25, -10), (-30, 25)]

# Add simulated vent plumes
for vx, vy in vent_coords:
    z += np.exp(-((x - vx)**2 + (y - vy)**2) / 20) * 10

# Plotting the 3D terrain
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
terrain = ax.plot_surface(x, y, z, cmap='inferno', edgecolor='none', alpha=0.9)

# Mark hydrothermal vents
for i, (vx, vy) in enumerate(vent_coords):
    vz = -np.sqrt(vx**2 + vy**2) + 5
    ax.scatter(vx, vy, vz, color='cyan', s=80, label='Vent' if i == 0 else "")

# Label and customize
ax.set_title('3D Terrain of Thalasson Ocean World with Hydrothermal Vents', pad=20)
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Depth (km)')
ax.view_init(elev=45, azim=45)
fig.colorbar(terrain, shrink=0.5, aspect=10, label='Elevation')

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
