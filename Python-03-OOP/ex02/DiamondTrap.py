from S1E7 import Baratheon, Lannister

class King(Baratheon,Lannister):
    """Representing the King family."""
    def __init__(self, first_name, is_alive=True) -> None:
        """constructor of the King class."""
        super().__init__(first_name, is_alive)
        
    def set_eyes(self, value):
        """set the eyes of the king."""
        self.eyes = value
        
    def set_hairs(self, value):
        """set the hairs of the king."""
        self.hairs = value
        
    def get_eyes(self):
        """get the eyes of the king."""
        return self.eyes

    def get_hairs(self):
        """get the hairs of the king."""
        return self.hairs