from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class Character"""
    def __init__(self,first_name,is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die():
        """Your docstring for method Character die"""
        pass
    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return self.__str__()
    
class Stark(Character):
    """Your docstring for Class Stark"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Your docstring for init Class Stack"""
        super().__init__(first_name, is_alive)
        
    def die(self):
        """Your docstring for method  Stark die"""
        self.is_alive = False
        