class calculator:
    """calculator class that performs operations on a list."""
    def __init__(self,list) -> None:
        """
        Initializes the calculator with the provided list.

        Args:
            list (list): The list on which operations will be performed.
        """
        self.list = list
        
    def __add__(self, object)-> None:
        """
        Returns:
            The resulting list after addition.
        """
        print([item + object for item in self.list])
        
    def __mul__(self, object)-> None:
        """
        Returns:
            The resulting list after multiplication.
        """
        print([item * object for item in self.list])
        
    def __sub__(self, object)-> None:
        """
        Returns:
            The resulting list after subtraction.
        """
        print([item - object for item in self.list])
        
    def __truediv__(self, object)-> None:
        """
        Returns:
            The resulting list after division.

        Raises:
            ZeroDivisionError: If the object value is 0.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            print([item / object for item in self.list])
        except ZeroDivisionError as msj:
            print(msj)