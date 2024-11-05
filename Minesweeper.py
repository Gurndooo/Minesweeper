import random

# Play game


class board:

    def __init__(self, dim_size, num_bombs):
        # Keep track of parameters

        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create the board
        self.board = self.make_new_board(self) # Plant the bombs

        # Initialize a set to keep track of where we've uncovered
        # We'll save (row, col) tuples into this set
        self.dug = set() # If we dig at 0, 0 then self.dug = {(0,0)}
        
    def make_new_board(self):
        # Construct a new board based on the dim_size and num_bombs
        # Construct the list of lists here (most natural for 2D board)

        # Generate new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # Creates a board like this:
        # [None, None, ....None]
        # [None, None, ....None]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)   # Assign random locations on board to bombs
            row = loc //self.dim_size                      
            col = loc % self.dim_size

            if board[row][col] == '*':
                # Bomb already planted
                continue

       
def play(dim_size=10, num_bombs=10):

    # step 1. Create the board and plant the bombs
    # step 2. Show the board and ask where to dig
    # step 3a. If location is a bomb, game over message
    # step 3b. If location is not a bomb, dig recursively until at least next to a bomb
    # step 4. Repeat step 2 and 3 until no more places to dig

    pass

board = [[None for _ in range(10)] for _ in range(10)]
print(board)
for row in board:
    print(row)
    print('\n')

print(board[0])