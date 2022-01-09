from box.box import Box

class Grid:

    def __init__(self) -> None:
        self.grid = [Box(i+1, str(i+1)) for i in range(9)]

    
    def display(self) -> str:
        print(" --- --- ---")
        for i in range(0, 9, 3):
            print(f"| {self.grid[i].get_value()} | {self.grid[i+1].get_value()} | {self.grid[i+2].get_value()} |")
            print(" --- --- ---")


    def set_box_value(self, box_num: int, value: str) -> None:
        self.grid[box_num - 1].set_value(value)


    def game_end(self) -> bool:
        if self.grid_full():
            return True
        
        if self.grid_win():
            return True

        return False


    def grid_full(self) -> bool:
        for box in range(len(self.grid)):
            if not self.is_occupied(box + 1):
                return False
        return True


    def grid_win(self) -> bool:
        return self.vertical_win() or self.horizontal_win() or self.diagonal_win()


    def vertical_win(self) -> bool:
        if self.grid[0].get_value() == self.grid[3].get_value() == self.grid[6].get_value():
            return True
        
        if self.grid[1].get_value() == self.grid[4].get_value() == self.grid[7].get_value():
            return True

        if self.grid[2].get_value() == self.grid[5].get_value() == self.grid[8].get_value():
            return True

        return False


    def horizontal_win(self) -> bool:
        if self.grid[0].get_value() == self.grid[1].get_value() == self.grid[2].get_value():
            return True
        
        if self.grid[3].get_value() == self.grid[4].get_value() == self.grid[5].get_value():
            return True

        if self.grid[6].get_value() == self.grid[7].get_value() == self.grid[8].get_value():
            return True

        return False


    def diagonal_win(self) -> bool:
        if self.grid[0].get_value() == self.grid[4].get_value() == self.grid[8].get_value():
            return True
        
        if self.grid[2].get_value() == self.grid[4].get_value() == self.grid[6].get_value():
            return True

        return False


    def is_occupied(self, box_num: int) -> bool:
        if self.grid[box_num - 1].occupied:
            return True
        return False