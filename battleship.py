from pandas import DataFrame
import numpy as np


class Grid():
    '''Holds one battleship Grid'''
    # TODO: explain attributes
    def __init__(self, player, ship_nmbrs):
        self.game_over = False  # set to True if all ships are hit
        self.board = DataFrame(False,
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.shots = np.array([[False]*10]*10)    # shots taken
        self.player = player    # 'computer' or 'user'
        self.ships = ship_nmbrs

    def draw(self):
        '''Create a grid with printable characters'''
        print_grid = DataFrame(False,
                index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        if self.player == 'computer':
            print_grid[:] = ' ' # all non-shot water fields
            # element-wise multiplication of two boolean matrices, ~ inverts a matrix
            print_grid[np.multiply(~self.board,self.shots)] = '~' # all shot water fields
            print_grid[self.board] = '0' # all ships
            print_grid[np.multiply(self.board,self.shots)] = 'x' # all shot ship fields
        elif self.player == 'user':
            print_grid[:] = '?' # all non-shot fields
            print_grid[np.multiply(~self.board,self.shots)] = '~' # all shot water fields
            print_grid[np.multiply(self.board,self.shots)] = 'x' # all shot ship fields
        else:
            raise ValueError("grid player is neither 'user' nor 'computer'")
        return print_grid

    def __str__(self):
        '''Print grid in string format'''
        return self.draw().to_string(header=True, index=True)

    def shoot(self, shoot_str):
        '''Shoot at a field (row, col) and return ocean or hit'''
        # row in 'A', 'B', ... Replace with 0, 1, ... by getting ASCII number
        col = ord(shoot_str[0].upper())-65  # 0 ... 9
        row = int(shoot_str[1:])-1          # 0 ... 9
        print(row, ' '*9, col)
        if self.shots[row, col] == True:
            return 'Field is already shot'
        self.shots[row, col] = True    # Save shot

        # check, if a ship is hit
        if self.board[shoot_str[0].upper()][col+1] == True:
            # TODO: check if ship is destroyed
            # TODO: update ships attribute in case of destruction
            return 'Hit'

        # TODO: check if game is over
        # TODO: return ocean, hit ,destroyal or game_over
        return "Ocean"

    def distribute_ships(self):
        '''Distribute ships on grid'''
        # TODO
        pass


class Battleship():
    ''' The battleship game board '''
    # TODO: Explain attributes

    def __init__(self):
        # number of ships. First index are ships of size one, second of size two etc.
        self.ship_nmbrs = []
        self.pc = Grid('computer', self.ship_nmbrs)
        self.user = Grid('user', self.ship_nmbrs)

    def __str__(self):
        pc = self.pc.draw()
        user = self.user.draw()
        indent = " "*2  # indent at the left side
        space = " "*8   # space between pc and user Grid
        out = indent+"Computer"+" "*24+space+"User\n"
        out += indent+" "*4+"  ".join(pc.columns)+space+" "*4+"  ".join(user.columns)
        for row in range(len(pc)):
            out += "\n"+indent+"{:2d}  ".format(row+1)+"  ".join(pc.iloc[row,:])
            out += space+"{:2d}  ".format(row+1)+"  ".join(user.iloc[row,:])
        return out

    def set_ship_nmbrs(self, ship_nmbrs):
        '''Set custom ship numbers'''
        self.ship_nmbrs = ship_nmbrs
        self.pc.ship_nmbrs = ship_nmbrs
        self.user.ship_nmbrs = ship_nmbrs

    def distribute_ships(self):
        '''Distribute ships on both player and pc grid'''
        self.user.distribute_ships()
        self.pc.distribute_ships()

    def instructions(self):
        '''Print instructions of the battleship game'''
        # TODO
        # Basic introduction to game
        # Printed Grids: what character means what?
        # Possible user inputs
        # How does the computer move?
        return "To be added."

    def create_computer_move(self):
        # TODO: let pc shoot randomly, except a ship is hit
        # return field string
        return "dummy field"

    def restart(self):
        '''Restart game. Only saved param is ship_nmbrs'''
        # do not update self.ship_nmbrs as it could be customized
        self.pc = Grid('computer', self.ship_nmbrs)
        self.user = Grid('user', self.ship_nmbrs)
        # new ship positions
        self.distribute_ships()

    def remaining_ships(self):
        # TODO: print remaining ships of pc and user
        # return string to print
        return "Print ships dummy return string"
