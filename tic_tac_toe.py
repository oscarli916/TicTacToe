from grid.grid import Grid
from player.player import Player

def check_user_input(box_num: int, grid: Grid) -> bool:
    if box_num < 1 or box_num > 9:
        return False
    
    if grid.is_occupied(box_num):
        return False

    return True


# Initialize 
grid = Grid()
player_value = ["X", "O"]
player_list = [Player(value) for value in player_value]
num_player = len(player_list)


count = 0
grid.display()
while not grid.game_end():

    current_player = count % num_player
    box_num = input(f"Player {player_list[current_player].value}. Please choose a box.")

    input_valid = check_user_input(int(box_num), grid)
    while not input_valid:
        print("Input is not valid. Please try again.")
        box_num = input(f"Player Please choose a box.")
        input_valid = check_user_input(int(box_num), grid)

    player_list[current_player].choose_box(int(box_num), grid)

    grid.display()

    count += 1