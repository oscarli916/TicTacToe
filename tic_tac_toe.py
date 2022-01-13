from grid.grid_factory import GridFactory
from player.player import Player

GRID_SIZE = 3

# Initialize 
factory = GridFactory()
grid = factory.create_grid(GRID_SIZE)
player1 = Player("X", grid)
player2 = Player("O", grid)
current_player = player1
next_player = player2


grid.display()


while current_player:
    
    temp_current_player = current_player
    current_player = current_player.take_turn(next_player)
    next_player = temp_current_player

    grid.display()


if grid.grid_win():
    print(f"Player {next_player.value} wins.")
elif grid.grid_full():
    print("It is a draw game.")
