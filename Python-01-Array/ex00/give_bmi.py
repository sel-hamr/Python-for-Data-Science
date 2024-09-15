def calculate_bmi(weight, height):
    """calculate_bmi calculates the BMI of a person given their weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi calculates the BMI of a list of people given their weight and height."""
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must have the same length")
    except ValueError as e:
        print(e)
    else:
        bmi_list = [calculate_bmi(weight[i], height[i]) for i in range(len(height))]
        return bmi_list
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit checks if the BMI of a person is above a certain limit."""
    return [bmi[i] > limit for i in range(len(bmi))]