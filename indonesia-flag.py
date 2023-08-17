import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

# Plotting the merah-putih colours in national flag
merah = patch.Rectangle(
    (0, 3), width=6, height=2, facecolor="#FF0000", edgecolor="grey"
)
putih = patch.Rectangle(
    (0, 1), width=6, height=2, facecolor="#FFFFFF", edgecolor="grey"
)
a, b = py.subplots()

b.add_patch(merah)
b.add_patch(putih)

py.axis("equal")
py.show()
