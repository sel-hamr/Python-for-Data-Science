import numpy as np
from PIL import Image

def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received"""
    inverted_array = np.copy(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            inverted_array[i][j] = 255 - array[i][j]
    PIL_image = Image.fromarray(np.uint8(inverted_array)).convert('RGB')
    PIL_image.save("ft_inverted.jpg")

def ft_red(array) -> np.ndarray:
    """Reduces the image to only the red color"""
    red_array = np.copy(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            red_array[i][j][1] = 0
            red_array[i][j][2] = 0
    PIL_image = Image.fromarray(np.uint8(red_array)).convert('RGB')
    PIL_image.save("ft_red.jpg")
    
def ft_green(array) -> np.ndarray:
    """Reduces the image to only the green color"""
    green_array = np.copy(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            green_array[i][j][0] = 0
            green_array[i][j][2] = 0
    PIL_image = Image.fromarray(np.uint8(green_array)).convert('RGB')
    PIL_image.save("ft_green.jpg")
    
def ft_blue(array) -> np.ndarray:
    """Reduces the image to only the blue color"""
    blue_array = np.copy(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            blue_array[i][j][0] = 0
            blue_array[i][j][1] = 0
    PIL_image = Image.fromarray(np.uint8(blue_array)).convert('RGB')
    PIL_image.save("ft_blue.jpg")

def ft_grey(array) -> np.ndarray:
    """Reduces the image to only the gray color"""
    gray_array = np.copy(array)
    weights = [0.2989, 0.5870, 0.1140]
    grayscale_image = np.dot(gray_array, weights)
    PIL_image = Image.fromarray(np.uint8(grayscale_image)).convert('RGB')
    PIL_image.save("ft_gray.jpg")