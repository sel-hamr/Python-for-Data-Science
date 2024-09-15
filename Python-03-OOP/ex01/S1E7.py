from S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive = True) -> None:
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        
    def die(self):
        self.is_alive = False
    
class Lannister(Character):
    def __init__(self, first_name, is_alive = True) -> None:
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "dark"
        
    def die(self):
        self.is_alive = False
        
    @classmethod
    def create_lannister(cls,first_name,is_alive):
        return cls(first_name,is_alive)
    