class calculator:
    """This class contains methods for vector operations."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float])-> None:
        """Dot product of two vectors."""
        result = [V1[index] * V2[index] for index in range(len(V1))]
        print(f"Dot product is: {sum(result)}")
        
    def add_vec(V1: list[float], V2: list[float])-> None:
        """add two vectors"""
        result = [sum(item) for item in zip(V1,V2)] 
        print(f"Add Vector is : {result}")
        
    def sous_vec(V1: list[float], V2: list[float])-> None:
        """sous two vectors"""
        result = [float(item[0]) - float(item[1]) for item in zip(V1,V2)]
        print(f"Sous Vector is : {result}")
        
        