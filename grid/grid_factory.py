from grid.grid import Grid
from grid.three_three import ThreeThreeGrid
from grid.error import UnsupportedGrid

class GridFactory:

    def create_grid(self, grid_size: int) -> Grid:
        if grid_size == 3:
            return ThreeThreeGrid()
        else:
            raise UnsupportedGrid(f"{grid_size}x{grid_size} grid is not supported!")