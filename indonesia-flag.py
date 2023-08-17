import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Plotting the merah-putih colours in national flag
merah = patches.Rectangle(
    (0, 3), width=6, height=2, facecolor="#FF0000", edgecolor="grey"
)
putih = patches.Rectangle(
    (0, 1), width=6, height=2, facecolor="#FFFFFF", edgecolor="grey"
)

fig, ax = plt.subplots()

ax.add_patch(merah)
ax.add_patch(putih)

plt.axis("equal")
plt.show()
