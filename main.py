import numpy as np
from PIL import Image
import colorsys
from math import sqrt

def main():
    path = "sample1080.jpg"  #temporarily load the image
    image_array : np.array
    color_val = [0, 0, 0]
    desired_colors = [[0,0,0], [255,255,255], [0,255,193], [255,150,0], [100,0,255], [0, 150, 150], [255, 255, 0]]
    try:
        # path = input('Enter the absolute image path (no quotations): ')     #get image path
        color_count = int(input('How many colors would you like the picture to have? '
                                '(White and black are always included): '))
        for i in range(color_count):
            print('Enter your next color')
            color_val[0] = int(input('Red Value: '))
            color_val[1] = int(input('Green Value: '))
            color_val[2] = int(input('Blue Value: '))
            desired_colors.append([color_val[0], color_val[1], color_val[2]])
            print('Color has been added')

        for color in desired_colors:
            print(color)

        image = Image.open(path)
        image_array = np.array(image)       #convert the image to a numpy array

        if image_array.shape != 0:
            for i in range(image_array.shape[0]):
                for j in range(image_array.shape[1]):
                    color_val = compare_color(image_array[i,j], desired_colors)
                    # image_array[i,j] = recolor(image_array[i,j], color_val)
                    image_array[i,j] = color_val

        Image.fromarray(image_array).show()

    except Exception as e:
        print("Error loading image")

def recolor(pixel, target_rgb):
    # Convert both the pixel and target color to HSV
    r, g, b = [x / 255.0 for x in pixel]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    tr, tg, tb = [x / 255.0 for x in target_rgb]
    th, ts, _ = colorsys.rgb_to_hsv(tr, tg, tb)
    # Replace H and S with target, keep V from original
    new_r, new_g, new_b = colorsys.hsv_to_rgb(th, ts, v)
    return int(new_r * 255), int(new_g * 255), int(new_b * 255)

def compare_color(current_color, color_options):
    best_distance = 0
    color_choice = color_options[0]
    for color in color_options:
        distance = sqrt(abs(color[0] - current_color[0])
                             + abs(color[1] - current_color[1])
                             + abs(color[2] - current_color[2]))
        if color == color_options[0]:
            best_distance = distance
        elif distance < best_distance:
            best_distance = distance
            color_choice = color
    return color_choice

if __name__ == '__main__':
    main()