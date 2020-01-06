
import random
import os

# grids separate and global as they are worked on by many functions

grid_player1 = [['0.', '..A ', '..B ', '..C ', '..D ', '..E  ', '       E  ', '0.', '..A ', '..B ', '..C ', '..D ', '..E '],
                ['1.', '|...', '|...', '|...', '|...', '|...', '|       N  ', '1.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['2.', '|...', '|...', '|...', '|...', '|...', '|       E  ', '2.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['3.', '|...', '|...', '|...', '|...', '|...', '|       M  ', '3.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['4.', '|...', '|...', '|...', '|...', '|...', '|       Y  ', '4.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['5.', '|...', '|...', '|...', '|...', '|...', '|          ', '5.', '|...', '|...', '|...', '|...', '|...', '|']]
grid_player2 = [['0.', '..A ', '..B ', '..C ', '..D ', '..E  ', '       E  ', '0.', '..A ', '..B ', '..C ', '..D ', '..E '],
                ['1.', '|...', '|...', '|...', '|...', '|...', '|       N  ', '1.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['2.', '|...', '|...', '|...', '|...', '|...', '|       E  ', '2.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['3.', '|...', '|...', '|...', '|...', '|...', '|       M  ', '3.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['4.', '|...', '|...', '|...', '|...', '|...', '|       Y  ', '4.', '|...', '|...', '|...', '|...', '|...', '|'],
                ['5.', '|...', '|...', '|...', '|...', '|...', '|          ', '5.', '|...', '|...', '|...', '|...', '|...', '|']]


def change_player_screen():
    input('''
    ***********************************************************************************************
    ***********************************************************************************************
    **                                                                                           **
    **   ||==\  ||     /\    || //  ||==  ||==\      /==  ||  ||    /\    ||\ ||   /==    ||==   **
    **   ||==/  ||   ||  ||  ||//   ||==  ||==/     ||    ||==||  ||  ||  || \||  ||      ||==   **
    **   ||     ||== ||==||  ||     ||==  ||  \      \==  ||  ||  ||==||  ||  ||   \==||  ||==   **
    **                                                                                           **
    **                                                             Press Enter to continue...    **
    ***********************************************************************************************
    ***********************************************************************************************
    ''')

# global variables that are worked on by multiple functions at different moments


player1_ship1 = []
player1_ship2 = []
player1_ship3 = []

player2_ship1 = []
player2_ship2 = []
player2_ship3 = []

computer_hit_priority = []

coordinates_translator = {
                        'A1': [1, 1], 'B1': [1,2], 'C1': [1,3], 'D1': [1,4], 'E1': [1,5],
                        'A2': [2, 1], 'B2': [2,2], 'C2': [2,3], 'D2': [2,4], 'E2': [2,5],
                        'A3': [3, 1], 'B3': [3,2], 'C3': [3,3], 'D3': [3,4], 'E3': [3,5],
                        'A4': [4, 1], 'B4': [4,2], 'C4': [4,3], 'D4': [4,4], 'E4': [4,5],
                        'A5': [5, 1], 'B5': [5,2], 'C5': [5,3], 'D5': [5,4], 'E5': [5,5]
                        }

all_map_coordinates = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1',
                       'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2',
                       'E3', 'E4', 'E5']
player1_all_map_coordinates = all_map_coordinates[:]
player2_all_map_coordinates = all_map_coordinates[:]
computer_all_map_coordinates = all_map_coordinates[:]

placing_coord_vert_2box = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1',
                           'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'E1', 'E2',
                           'E3', 'E4']
placing_coord_vert_3box = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 
                           'D1', 'D2', 'D3', 'E1', 'E2', 'E3']
placing_coord_hori_2box = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 
                           'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 
                           'D4', 'D5']
placing_coord_hori_3box = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 
                           'B5', 'C1', 'C2', 'C3', 'C4', 'C5']


# intro section, the title and information about the game at the beginning


def intro():
    os.system('clear')
    input('''
    ***********************************************************************************************
    ***********************************************************************************************
    **                                                                                           **
    **   ||==\    /\    =====  =====  ||    ||==  /==  ||  ||  ||  ||==\                         **
    **   ||==/  ||  ||    ||     ||   ||    ||==  \=\  ||==||  ||  ||==/                         **
    **   ||==/  ||==||    ||     ||   ||==  ||==  ==/  ||  ||  ||  ||                            **
    **                                                                                           **
    **  by Mechanical Lemons 2 Reborn Again                        Press Enter to continue...    **
    ***********************************************************************************************
    ***********************************************************************************************
    ''')
    input('''
    ***********************************************************************************************
    ***********************************************************************************************
    ** 1. You place 3 ships on the board (2 ships with the length of 2 and a 3rd with length 3). **
    ** 2. First select the direction (1 for vertical, 2 for horizontal).                         **
    ** 3. Then select the coordinates (A1 or B4 and so on) of the front of the ship to place it. **
    ** 4. Fire at the enemy by selecting coordinates on the grid (A1, B5, C2 and so on)          **
    **    Hits will show up as [*] and misses as .X.                                             **
    **                                                             Press Enter to continue...    **
    ***********************************************************************************************
    ***********************************************************************************************
    ''')


# function that allows the player to select vs another player or computer


def play_vs_player_or_computer():
    versus=input('''
    ***********************************************************************************************
    ***********************************************************************************************
    ** Type 1 to play versus a fellow human.                                                     **
    ** Type 2 to play versus the computer.                                                       **
    ** Type 3 to exit.                                                                           **
    **                                                                                           **
    **                                                                                           **
    **                                                                                           **
    ***********************************************************************************************
    ***********************************************************************************************
    ''')
    if versus == str(1):
        player1_setup()
        change_player_screen()
        player2_setup()
        change_player_screen()
        gameplay(1)
    if versus == str(2):
        player1_setup()
        change_player_screen()
        computer_setup()
        change_player_screen()
        gameplay(2)
    if versus == str(3):
        print('Thanks for trying our game. Seeya!')
        exit()
    else:
        print('Invalid command. Try again later.Maybe.')
        exit()


# function that prints the given grid 


def show_grid(grid):
    for i in grid:
        for j in i:
            print(j, end='')
        print('\n')


# function that guides Player 1 through setting up ships on the grid


def player1_setup():
    global grid_player1
    # show_grid(grid_player1)
    show_grid(grid_player1)
    ships = ['1', '2', '3']
    for i in ships:
        valid_direction = False
        while valid_direction is False:
            direction = input(f'Player 1. Select ship {i} direction (1 vertical,'
                               ' 2 horizontal):')
            if direction != str(1) and direction != str(2):
                print('Invalid choice for direction.')
                valid_direction = False
            elif direction == str(1) or direction == str(2):
                valid_direction = True
                continue
        valid_coordinates = False
        while valid_coordinates is False:
            coordinates_input = input(f'Select the coordinates for the'
                                       'front of the ship ' + i + ':')
            if (i == str(1) or i == str(2)) and direction == str(1):
                if coordinates_input.upper() not in placing_coord_vert_2box:
                    print('Please select valid coordinates (A1, to A4, as A-E5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_vert_2box:
                    valid_coordinates = True
                    continue
            elif (i == str(1) or i == str(2)) and direction == str(2):
                if coordinates_input.upper() not in placing_coord_hori_2box:
                    print('Please select valid coordinates (A1, to D1, as E1-5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_hori_2box:
                    valid_coordinates = True
                    continue
            elif i == str(3) and direction == str(1):
                if coordinates_input.upper() not in placing_coord_vert_3box:
                    print('Please select valid coordinates (A1, to A4, as A-E4 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_vert_3box:
                    valid_coordinates = True
                    continue
            elif i == str(3) and direction == str(2):
                if coordinates_input.upper() not in placing_coord_hori_3box:
                    print('Please select valid coordinates (A1, to A3, as D-E1-5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_hori_3box:
                    valid_coordinates = True
                    continue
        coordinates = coordinates_translator[coordinates_input.upper()]
        update_grid_player1(i, direction, coordinates, 1, grid_player1)
    show_grid(grid_player1)
    return grid_player1


# function that guides Player 2 to set up ships on the grid


def player2_setup():
    global grid_player2
    # show_grid(grid_player2)
    show_grid(grid_player2)
    ships = ['1', '2', '3']
    for i in ships:
        valid_direction = False
        while valid_direction is False:
            direction = input(f'Player 2. Select ship {i} direction (1 vertical,'
                               ' 2 horizontal):')
            if direction != str(1) and direction != str(2):
                print('Invalid choice for direction.')
                valid_direction = False
            elif direction == str(1) or direction == str(2):
                valid_direction = True
                continue
        valid_coordinates = False
        while valid_coordinates is False:
            coordinates_input = input(f'Select the coordinates for the'
                                       'front of the ship ' + i + ':')
            if (i == str(1) or i == str(2)) and direction == str(1):
                if coordinates_input.upper() not in placing_coord_vert_2box:
                    print('Please select valid coordinates (A1, to A4, as A-E5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_vert_2box:
                    valid_coordinates = True
                    continue
            elif (i == str(1) or i == str(2)) and direction == str(2):
                if coordinates_input.upper() not in placing_coord_hori_2box:
                    print('Please select valid coordinates (A1, to D1, as E1-5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_hori_2box:
                    valid_coordinates = True
                    continue
            elif i == str(3) and direction == str(1):
                if coordinates_input.upper() not in placing_coord_vert_3box:
                    print('Please select valid coordinates (A1, to A4, as A-E4 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_vert_3box:
                    valid_coordinates = True
                    continue
            elif i == str(3) and direction == str(2):
                if coordinates_input.upper() not in placing_coord_hori_3box:
                    print('Please select valid coordinates (A1, to A3, as D-E1-5 will'
                          ' place the ship outside the grid.)')
                    valid_coordinates = False
                elif coordinates_input.upper() in placing_coord_hori_3box:
                    valid_coordinates = True
                    continue
        coordinates = coordinates_translator[coordinates_input.upper()]
        grid_player2 = update_grid_player2(i, direction, coordinates, 2, grid_player2)
    show_grid(grid_player2)
    return grid_player2  


# function that sets up the grid for the computer, places ships at random locations


def computer_setup():
    global grid_player2
    direction_list = [1, 2]
    # show_grid(grid_player2)
    ships = ['1', '2', '3']
    for i in ships:
        direction = str(random.choice(direction_list))
        # print('Computer chose direction.')
        coordinates_input = ''
        coordinates = []
        if (i == str(1) or i == str(2)) and direction == str(1):
            coordinates_input = random.choice(placing_coord_vert_2box)    
        elif (i == str(1) or i == str(2)) and direction == str(2):
            coordinates_input = random.choice(placing_coord_hori_2box)  
        elif i == str(3) and direction == str(1):
            coordinates_input = random.choice(placing_coord_vert_3box)
        elif i == str(3) and direction == str(2):
            coordinates_input = random.choice(placing_coord_hori_3box)
        # print(coordinates_input)
        coordinates = coordinates_translator[coordinates_input]
        # print(coordinates_input)
        grid_player2 = update_grid_player2(i, direction, coordinates, 2, grid_player2)
    # show_grid(grid_player2)
    return grid_player2  


# Player 1 put in his layout information in the previous function, the update function
# places the ships graphycally


def update_grid_player1(ship, direction, coordinates, player, working_grid):
    # global grid_player1
    # global grid_player2
    ship_player1 = []
    working_grid = grid_player1
    y = coordinates[0]
    x = coordinates[1]
    if ship == str(1):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            player1_ship1.append(f'{y}, {x}')
            player1_ship1.append(f'{y+1}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            player1_ship1.append(f'{y}, {x}')
            player1_ship1.append(f'{y}, {x+1}')
    elif ship == str(2):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            # player1_ships.append([[y, x], [y+1, x]])
            player1_ship2.append(f'{y}, {x}')
            player1_ship2.append(f'{y+1}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            # player1_ships.append([[y, x], [y, x+1]])
            player1_ship2.append(f'{y}, {x}')
            player1_ship2.append(f'{y}, {x+1}')
    elif ship == str(3):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            working_grid[y+2][x] = '|[O]'
            # player1_ships.append([[y, x], [y+1, x], [y+2, x]])
            player1_ship3.append(f'{y}, {x}')
            player1_ship3.append(f'{y+1}, {x}')
            player1_ship3.append(f'{y+2}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            working_grid[y][x+2] = '|[O]'
            # player1_ships.append([[y, x], [y, x+1], [y, x+2]])
            player1_ship3.append(f'{y}, {x}')
            player1_ship3.append(f'{y}, {x+1}')
            player1_ship3.append(f'{y}, {x+2}') 
    return grid_player1


# Player 1 put in his layout information in the previous function, the update function
# places the ships graphycally
# this function is also used when Player one is against the Computer


def update_grid_player2(ship, direction, coordinates, player, working_grid):
    # global grid_player1
    # global grid_player2
    y = coordinates[0]
    x = coordinates[1]
    if ship == str(1):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            player2_ship1.append(f'{y}, {x}')
            player2_ship1.append(f'{y+1}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            player2_ship1.append(f'{y}, {x}')
            player2_ship1.append(f'{y}, {x+1}')
    elif ship == str(2):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            player2_ship2.append(f'{y}, {x}')
            player2_ship2.append(f'{y+1}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            player2_ship2.append(f'{y}, {x}')
            player2_ship2.append(f'{y}, {x+1}')
    elif ship == str(3):
        if direction == str(1):
            working_grid[y][x] = '|[O]'
            working_grid[y+1][x] = '|[O]'
            working_grid[y+2][x] = '|[O]'
            player2_ship3.append(f'{y}, {x}')
            player2_ship3.append(f'{y+1}, {x}')
            player2_ship3.append(f'{y+2}, {x}')
        elif direction == str(2):
            working_grid[y][x] = '|[O]'
            working_grid[y][x+1] = '|[O]'
            working_grid[y][x+2] = '|[O]'
            player2_ship3.append(f'{y}, {x}')
            player2_ship3.append(f'{y}, {x+1}')
            player2_ship3.append(f'{y}, {x+2}')    
    return grid_player2


# main gameplay function


def gameplay(player):
    if player == 1:
        turn = 0
        while turn < 51:
            turn += 1
            if turn % 2 != 0:
                player1_turn()
                os.system('clear')
                change_player_screen()
            elif turn % 2 == 0:
                player2_turn()
                os.system('clear')
                change_player_screen()
    elif player == 2:
        turn = 0
        while turn < 51:
            turn += 1
            if turn % 2 != 0:
                player1_turn()
                os.system('clear')
                change_player_screen()
            elif turn % 2 == 0:
                computer_turn()
                os.system('clear')
                # change_player_screen()


# function for Player 1 to put in the attack coordinates and to return hit result


def player1_turn():
    global grid_player1
    global grid_player2
    working_grid = grid_player1 # working_grid and enemy_grid for clarity
    enemy_grid = grid_player2
    show_grid(working_grid)
    valid_fire_location = False
    while valid_fire_location is False:
        fire_location = input('Player 1. Select enemy location to hit:')
        fire_location = fire_location.upper()
        if fire_location in player1_all_map_coordinates:
            valid_fire_location = True
            player1_all_map_coordinates.remove(fire_location)
        else:
            print('Invalid fire location')
            valid_fire_location = False
    fire_location = coordinates_translator[fire_location]
    y = fire_location[0]
    x = fire_location[1]
    if enemy_grid[y][x] == '|[O]':
        enemy_grid[y][x] = '|[X]'
        working_grid[y][x+7] = '|[*]'
        if f'{y}, {x}' in player2_ship1:
            player2_ship1.remove(f'{y}, {x}')
            if player2_ship1 == []:
                print('*****Congratulations, you sunk the enemy ship no. 1, the S.S. Goodwater.')
                input('Press Enter to continue...')
        if f'{y}, {x}' in player2_ship2:
            player2_ship2.remove(f'{y}, {x}')
            if player2_ship2 == []:
                print('*****Congratulations, you sunk the enemy ship no. 2, the S.S. Potato.')
                input('Press Enter to continue...')
        if f'{y}, {x}' in player2_ship3:
            player2_ship3.remove(f'{y}, {x}')
            if player2_ship3 == []:
                print('*****Congratulations, you sunk the enemy ship no. 3, the S.S. Lemon.')
                input('Press Enter to continue...')
    else:
        enemy_grid[y][x] = '|.X.'
        working_grid[y][x+7] = '|.X.'
    grid_player1 = working_grid
    grid_player2 = enemy_grid
    hit_counter = 0
    for i in enemy_grid:
        for j in i:
            if j == '|[O]':
                hit_counter += 1
    if hit_counter == 0:
        show_grid(grid_player1)
        print('Player 1 wins. '*30)
        exit()
    show_grid(grid_player1)
    input('Press Enter to continue...')
    return grid_player1, grid_player2


# function for Player 2 to put in the attack coordinates and to return hit result


def player2_turn():
    global grid_player1
    global grid_player2
    working_grid = grid_player2 # working_grid and enemy_grid for clarity
    enemy_grid = grid_player1
    show_grid(working_grid)
    valid_fire_location = False
    while valid_fire_location is False:
        fire_location = input('Player 2. Select enemy location to hit:')
        fire_location = fire_location.upper()
        if fire_location in player2_all_map_coordinates:
            valid_fire_location = True
            player2_all_map_coordinates.remove(fire_location)
        else:
            print('Invalid fire location')
            valid_fire_location = False
    fire_location = coordinates_translator[fire_location]
    y = fire_location[0]
    x = fire_location[1]
    if enemy_grid[y][x] == '|[O]':
        enemy_grid[y][x] = '|[X]'
        working_grid[y][x+7] = '|[*]'
        if f'{y}, {x}' in player1_ship1:
            player1_ship1.remove(f'{y}, {x}')
            if player1_ship1 == []:
                print('*****Congratulations, you sunk the enemy ship no. 1, the S.S. Starfish.')
                input('Press Enter to continue...')
        if f'{y}, {x}' in player1_ship2:
            player1_ship2.remove(f'{y}, {x}')
            if player1_ship2 == []:
                print('*****Congratulations, you sunk the enemy ship no. 2, the S.S. Potato Juice.')
                input('Press Enter to continue...')
        if f'{y}, {x}' in player1_ship3:
            player1_ship3.remove(f'{y}, {x}')
            if player1_ship3 == []:
                print('*****Congratulations, you sunk the enemy ship no. 3, the S.S. Lemonade.')
                input('Press Enter to continue...')
    else:
        enemy_grid[y][x] = '|.X.'
        working_grid[y][x+7] = '|.X.'
    grid_player2 = working_grid
    grid_player1 = enemy_grid
    hit_counter = 0
    for i in enemy_grid:
        for j in i:
            if j == '|[O]':
                hit_counter += 1
    if hit_counter == 0:
        show_grid(grid_player1)
        print('Player 2 wins. '*30)
        exit()
    show_grid(grid_player2)
    input('Press Enter to continue...')
    return grid_player1, grid_player2


# function for Computer player to put in the attack coordinates and to return hit result


def computer_turn():
    global grid_player1
    global grid_player2
    fire_location = ''
    working_grid = grid_player2
    enemy_grid = grid_player1
    # show_grid(working_grid)
    if len(computer_hit_priority) != 0:
        for i in computer_hit_priority:
            if i in computer_all_map_coordinates:
                fire_location = i
                computer_hit_priority.remove(i)
                break
    else: 
        fire_location = random.choice(computer_all_map_coordinates)
    computer_all_map_coordinates.remove(fire_location)
    fire_location = coordinates_translator[fire_location.upper()]
    y = fire_location[0]
    x = fire_location[1]
    if enemy_grid[y][x] == '|[O]':
        enemy_grid[y][x] = '|[X]'
        working_grid[y][x+7] = '|[*]'
        if f'{y}, {x}' in player1_ship1:
            player1_ship1.remove(f'{y}, {x}')
            if player1_ship1 == []:
                print('*****Computer has sunk player\'s first ship, the S.S. Starfish.')
        if f'{y}, {x}' in player1_ship2:
            player1_ship2.remove(f'{y}, {x}')
            if player1_ship2 == []:
                print('*****Computer has sunk player\'s 2nd ship, the S.S. Potato Juice.')
        if f'{y}, {x}' in player1_ship3:
            player1_ship3.remove(f'{y}, {x}')
            if player1_ship3 == []:
                print('*****Computer has sunk player\'s 3rd ship, the S.S. Lemonade.')
    else:
        enemy_grid[y][x] = '|.X.'
        working_grid[y][x+7] = '|.X.'
    grid_player2 = working_grid
    grid_player1 = enemy_grid
    hit_counter = 0
    for i in grid_player2:
        for j in i:
            if j == '|[*]' and working_grid[y][x+7] == '|[*]':
                for key in coordinates_translator:
                    if coordinates_translator[key] == [y+1, x] and key in computer_all_map_coordinates:
                        computer_hit_priority.append(key)
                        # print(f'Added key {key} to priority list.')
                    if coordinates_translator[key] == [y, x+1] and key in computer_all_map_coordinates:
                        computer_hit_priority.append(key)
                        # print(f'Added key {key} to priority list.')
                    if coordinates_translator[key] == [y-1, x] and key in computer_all_map_coordinates:
                        computer_hit_priority.append(key)
                        # print(f'Added key {key} to priority list.')
                    if coordinates_translator[key] == [y, x-1] and key in computer_all_map_coordinates:
                        computer_hit_priority.append(key)
                        # print(f'Added key {key} to priority list.')
    # print(computer_hit_priority)
    for i in enemy_grid:
        for j in i:
            if j == '|[O]':
                hit_counter += 1
    if hit_counter == 0:
        print('Computer wins! ' * 30)
        show_grid(grid_player2)
        exit()
    # show_grid(grid_player2)
    input('Press Enter to continue...')
    return grid_player1, grid_player2


intro()
play_vs_player_or_computer()


 

