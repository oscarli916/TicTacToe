from __future__ import annotations

from grid.grid import Grid

class Player():

    def __init__(self, value: str, grid: Grid) -> None:
        self.value = value
        self.grid = grid


    def get_box_input(self) -> int:
        while True:
            try:
                box_num = int(input(f"Player {self.value}. Please choose a box."))
                return box_num
            except ValueError:
                print("Input is not a integer. Please try again.")
        
    
    def take_turn(self, next_player: Player) -> Player | None:

        while True:
            box_num = self.get_box_input()
            if not self.grid.input_within_range(box_num):
                print("Input is not in range. Please try again.")
            elif self.grid.is_occupied(box_num):
                print("The box is occupied. Please try again.")
            else:
                break

        self.grid.set_box_value(box_num, self.value)

        if self.grid.grid_full() or self.grid.grid_win():
            return None
        return next_player