import numpy as np
def slice_me(family: list, start: int, end: int) -> list:
    """slice_me slices a 2D array given a start and end index.""" 
    try:
        if not isinstance(family, list) or not all(isinstance(i, list) for i in family):
            raise ValueError("Input must be a list")
        array_family = np.array(family)
        print(f"My shape is :{array_family.shape}")
        array_slice = array_family[start:end]
        print(f"my new shape is :{array_slice.shape}")
        return array_slice.tolist()
    except ValueError as e:
        print(e)
    