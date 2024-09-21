import numpy as np
from PIL import Image
from  load_image import ft_load


def main():
    """main function to load image and zoom it"""
    image = ft_load("animal.jpeg")
    print(image)
    PIL_image = Image.fromarray(np.uint8(image)).convert('L')
    zoomed_image = PIL_image.crop((450,100,850,500))
    zoomed_image.save("result.jpg")
    image_array = np.array(zoomed_image)
    print(f"New shape after slicing: {image_array.shape}")
    print(image_array)

if __name__ == '__main__':
    main()