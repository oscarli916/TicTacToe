

class Box:

    def __init__(self, id: int, value: str = " ") -> None:
        self.id = id
        self.value = value
        self.occupied = False

    
    def set_value(self, value) -> None:
        self.value = value
        self.occupied = True

    
    def get_value(self) -> str:
        if self.value == "":
            return self.id
        return self.value