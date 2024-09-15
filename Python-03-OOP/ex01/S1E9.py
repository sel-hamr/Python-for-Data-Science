from abc import ABC, abstractmethod

class Character(ABC):
    """class Character is an abstract class"""
    def __init__(self,first_name,is_alive) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        """die method is an abstract method"""
        pass
    
    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Stark(Character):
    """class Stark inherits from class Character"""
    def __init__(self,first_name,is_alive=True) -> None:
        """init method of Stark class"""
        super().__init__(first_name,is_alive)
    
    def die(self):
        """die method changes is_alive to False"""
        self.is_alive = False