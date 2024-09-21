import numpy as np
from PIL import Image
from load_image import ft_load


def main():
    """main function to load image and rotate it"""
    image = ft_load("../ex03/result.jpg")
    print(image)
    PIL_image = Image.fromarray(np.uint8(image)).convert('L')
    rotate_image = PIL_image.rotate(90)
    rotate_image.save("rotate.jpg")
    image_array = np.array(rotate_image)
    print(f"New shape after Transpose: {image_array.shape}")
    print(image_array)

if __name__ == '__main__':
    main()