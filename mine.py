import random

def generateMineSweeperMap (n, k) :
  arr = [[0 for row in range (n)] for column in range (n)]

  for num in range(k):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    arr[y][x] = 'X' 

    if(x >= 0 and x <= n-2) and (y >= 0 and y <= n-1):
      if arr[y][x+1] != 'X':
        arr[y][x+1] += 1 # center right

    if(x >= 1 and x <= n-1) and (y >= 0 and y <= n-1):
      if arr[y][x-1] != 'X':
        arr[y][x-1] += 1 # center left

    if(x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
      if arr[y-1][x-1] != 'X':
        arr[y-1][x-1] += 1 # top left

    if(x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
      if arr[y-1][x+1] != 'X':
        arr[y-1][x+1] += 1 # top right

    if(x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
      if arr[y-1][x] != 'X':
        arr[y-1][x] += 1 # top center 

    if(x >= 0 and x <= n-2) and (y >= 0 and y <= n-2):
      if arr[y+1][x+1] != 'X':
        arr[y+1][x+1] += 1 # bottom right   

    if(x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
      if arr[y+1][x-1] != 'X':
        arr[y+1][x-1] += 1 # bottom left   

    if(x >= 0 and x<= n-1) and (y >= 0 and y <= n-2):
      if arr[y+1][x] != 'X':
        arr[y+1][x] += 1 # bottom center   
  return arr

def generatePlayersMap (n):
  arr = [['-' for row in range(n)] for column in range(n)]

def displayMap (map):
  for row in map:
    print(" ".join(str(cell) for cell in row))
    print("")

def checkWon (map):
  for row in map:
    for cell in row:
      if cell == '-':
        return False
  return True

def checkContinueGame (score):
  print("Your Score: ", score)
  isContinue = input("Do you want to try again? (y/n) :")
  if isContinue == 'n':
    return False
  return True

def Game ():
  GameStatus = True
  while GameStatus:

    difficulty = input("Select Difficulty (b, i, h): ")
    if difficulty.lower() == 'b':
      n = 5
      k = 3
    elif difficulty.lower() == "i":
      n = 6
      k = 8
    else:
      n = 8
      k = 20
    
    minesweeper_map = generateMineSweeperMap(n, k)
    player_map = generatePlayersMap(n)
    score = 0

    while True:
      
      if checkWon(player_map) == False:
        
        print("Enter your cell you want to open :")
        x = input("X (1 to 5) :")
        y = input("Y (1 to 5) :")
        x = int(x) - 1 # 0 based index
        y = int(y) - 1 # 0 based index
        
        if (minesweeper_map[y][x] == 'X'):

          print("Game Over!")
          displayMap(minesweeper_map)
          GameStatus = checkContinueGame(score)
          break

        else:

          player_map[y][x] == minesweeper_map[y][x]
          displayMap(player_map)
          score += 1

      else:
        
        displayMap(player_map)
        print("You have Won!")
        GameStatus = checkContinueGame(score)
        break


if __name__ == "__main__":
  try:
    Game()
  except KeyboardInterrupt:
    print('\nEnd of Game.')