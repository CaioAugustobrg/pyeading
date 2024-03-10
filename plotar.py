import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

with open('lines3.json', 'r') as json_file:
    lines_data = json.load(json_file)

image_path = 'sentenca-tiradentes.webp'
image = Image.open(image_path)

fig, ax = plt.subplots(1)
ax.imshow(image)

lines_info = lines_data.get('lines', [])

for line_info in lines_info:
    boundary = line_info.get('boundary', [])
    
    x_coords, y_coords = zip(*boundary)

    rect = patches.Polygon(
        list(zip(x_coords, y_coords)),
        linewidth=0.5, edgecolor='lightblue', facecolor='none'
    )
    ax.add_patch(rect)

plt.show()
