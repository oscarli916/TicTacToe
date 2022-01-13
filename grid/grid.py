from abc import ABC, abstractmethod

class Grid(ABC):

    def __init__(self) -> None:
        super().__init__()


    @abstractmethod
    def display(self) -> str:
        pass


    @abstractmethod
    def set_box_value(self, box_num: int, value: str) -> None:
        pass


    @abstractmethod
    def grid_full(self) -> bool:
        pass


    @abstractmethod
    def grid_win(self) -> bool:
        pass


    @abstractmethod
    def vertical_win(self) -> bool:
        pass


    @abstractmethod
    def horizontal_win(self) -> bool:
        pass


    @abstractmethod
    def diagonal_win(self) -> bool:
        pass


    @abstractmethod
    def is_occupied(self, box_num: int) -> bool:
        pass


    @abstractmethod
    def input_within_range(self, box_num: int) -> bool:
        pass