import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Plotting the merah-putih colors in national flag
merah = patches.Rectangle(
    (0, 3), width=6, height=2, facecolor="#FF0000", edgecolor="gray"
)
putih = patches.Rectangle(
    (0, 1), width=6, height=2, facecolor="#FFFFFF", edgecolor="gray"
)

fig, ax = plt.subplots()

ax.add_patch(merah)
ax.add_patch(putih)

plt.axis("equal")
plt.show()
