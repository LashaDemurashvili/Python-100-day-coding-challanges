# using module to receive colors from image format rgb
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

# print(colors)
print(rgb_colors)

