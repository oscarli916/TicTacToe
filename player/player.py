from grid.grid import Grid

class Player():

    def __init__(self, value) -> None:
        self.value = value


    def choose_box(self, box_num: int, grid: Grid) -> None:
        grid.set_box_value(box_num, self.value)

