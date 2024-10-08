from typing import Any, Optional


class Animal:
    def __init__(self, 
                 animal_id: int, 
                 habitat: str, 
                 species:str, 
                 age: Optional[int], 
                 health_status = Optional[str]) -> None:
        self.animal_id: int = animal_id
        self.age: Optional[int] = age
        self.health_status: Optional[str] = health_status
        self.species:str = species

    
