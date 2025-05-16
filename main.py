import numpy as np
from PIL import Image

def main():
    path = input("Enter the absolute image path (no quotations): ")
    image = Image.open(path)
    image_array = np.array(image)
    print(f'Shape: {image_array.shape}')

if __name__ == '__main__':
    main()