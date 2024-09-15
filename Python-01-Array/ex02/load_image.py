import numpy as np
from PIL import Image
import os

def ft_load(path: str):
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        layeredimg = img.convert('RGB')
        image_array = np.array(layeredimg)
        print(f"The shape of image is: {image_array.shape}")
        return np.array(image_array)
    except AssertionError as e:
        print(e)