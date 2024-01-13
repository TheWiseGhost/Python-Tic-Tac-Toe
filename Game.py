import random

class Tic_Tac_Toe():
  def __init__(self):
    self.board = []

  # Creates the board
  def create_board(self):
    # Creates 3 rows
    for x in range(3):
      row = []
      # Makes the rows like ---
      for i in range(3):
        row.append("-")
      # This will append each row to the board
      self.board.append(row)

  # Displays the board
  def display_board(self):
    num = 1
    # Prints the horiziontal coordinates
    print("    1   2   3")
    print("  -------------")
    for row in self.board:
      # Prints the vertical coordinates
      print(num, end=' ')
      print("|", end = ' ')
      # Prints out board
      for x in row:
        # Prints the board out without the brackets and commas
        print(x, end=' ')
        print("|", end= ' ')
      # Prints a new line for every row
      print()
      print("  -------------", end = '')
      print()
      num += 1

  # Creates a 50/50 random 
  # This will be used in determining a random first player (X/O)
  def random(self):
    return random.randint(0, 1)

  # This will swap the player
  def swap_player(self):
    if self.player == 'X':
      self.player = 'O'
    else:
      self.player = 'X'

  # Places player on the board on the coordinates of user input
  def place_player(self, row, col):
    self.board[row-1][col-1] = self.player


  # Makes sure the user inputted coordinates don't already have something there and are on the board. 
  def check_spot_valid(self, row, col):
    valid = False
    while valid != True:
      if row > 3 or row < 1:
        print("That space is off the board!")
      elif col > 3 or col < 1:
        print("That space is off the board!")
      else:
        if self.board[row-1][col-1] != '-':
          print(f"There is already a {self.board[row-1][col-1]} there!")
        else:
          valid = True
          break

      row, col = list(map(int, input(f"Player {self.player} pick another spot (row,column). ").split(',')))

    return row, col


  # Checks if a player has won
  def check_win(self):
    board_length = len(self.board)
    
    # Checks rows
    for row in range(board_length):
      win = True
      for col in range(board_length):
        if self.board[row][col] != self.player:
          win = False
          break
      # Works because when win is true it will return true but when win is false it will do nothing and won. 
      if win:
        return win

    # Checks columns
    for row in range(board_length):
      win = True
      for col in range(board_length):
        if self.board[col][row] != self.player:
          win = False
          break
      if win:
        return win

    # Checks top left to bottom right diagonal
    win = True
    for x in range(board_length):
      if self.board[x][x] != self.player:
        win = False
        break
    if win:
      return win

    # Checks top right to bottom left diagonal
    win = True
    for x in range(board_length):
      if self.board[x][2-x] != self.player:
        win = False
        break
    if win:
      return win
      
    # If the checks pass through everything above, then no one has won so return false
    return False

    
  # Resets the board, used for playing again
  def reset_board(self):
    self.board = []


  # Checks if the board is full and game is a tie
  def check_full_board(self):
    board_length = len(self.board)
    for row in range(board_length):
      for col in range(board_length):
        if self.board[row][col] == '-':
          return False
          break
    return True


  # Used so computer can place random player
  def computer_placer(self):
    true = True
    while true == True:
      random_row = random.randint(0, 2)
      random_col = random.randint(0, 2)

      if self.board[random_row][random_col] == '-':
        self.board[random_row][random_col] = self.computer
        true = False
      else:
        true = True

    
  # Starts the game
  def pvp_start(self):
    self.create_board()
    self.display_board()

    if self.random() == 1:
      self.player = 'X'
    else:
      self.player = 'O'

    while True:
      # User input that turns the input into a list and uses python method to sepearte it into the desired row and column variable
      # Rescources for learning how to do map and split are https://www.w3schools.com/python/ref_string_split.asp 
      # and https://www.geeksforgeeks.org/python-map-function/
      # User input will be row,col
      row, col = list(map(int, input(f"Player {self.player} pick a spot (row,column). ").split(',')))

      
      row, col = self.check_spot_valid(row, col)


      self.place_player(row, col)
      self.display_board()
      
      if self.check_win():
        print(f"Congratulations player {self.player}! You won!")
        return False
      if self.check_full_board():
        print("Tie! Nice try player X and player O!")
        return False
        
      self.swap_player()


  def one_player_start(self):
    self.create_board()
    self.display_board()

    if self.random() == 1:
      self.player = 'X'
      self.computer = 'O'
    else:
      self.player = 'O'
      self.computer = 'X'
      
    while True:
      row, col = list(map(int, input(f"Player {self.player} pick a spot (row,column). ").split(',')))

      row, col = self.check_spot_valid(row, col)
      
      self.place_player(row, col)

      if self.check_win():
        self.display_board()
        print(f"Congratulations player {self.player}! You won!")
        return False

      self.display_board()
      print("Computer placing...")

      self.computer_placer()
      
      # Swaps the player to the computer player and then checks win and then swaps the player back. 
      self.swap_player()
      if self.check_win():
        self.display_board()
        print(f"Nice try! Player {self.computer} won!")
        return False
      self.swap_player()
      
    
      if self.check_full_board():
        print(f"Tie! Nice try player {self.player}!")
        return False

      self.display_board()



print("Hello! This is a Tic_Tac_Toe Game!")
game_choice = input("Would you like to play 1 player or 2 player (1/2). ")

game = Tic_Tac_Toe()    

# Gets what user wants to play and does according version of game
if game_choice == '2':
  game.pvp_start()
else:
  game.one_player_start()
  

# Play again
play_again = input("Do you want to play again? (y/n). ")

while play_again == 'y':
  game.reset_board()
  game_choice = input("Would you like to play 1 player or 2 player (1/2). ")
  if game_choice == '2':
    game.pvp_start()
  else:
    game.one_player_start()
  play_again = input("Do you want to play again? (y/n). ")
else:
  print("Thanks for playing!")
  exit()

