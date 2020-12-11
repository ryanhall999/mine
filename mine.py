import random

def minesweeper (n) :
  arr = [[0 for row in range (n)] for column in range (n)]
  x = random.randint(0,4)
  y = random.randint(0,4)
  arr[y][x] = 'X' 

  if (x >= 1 and x <= 3):
    arr[y][x+1] += 1 # center right
    arr[y][x-1] += 1 # center left

  if(x == 0):
    arr[y][x+1] += 1 # center right
  
  if(x == 4):
    arr[y][x-1] += 1 # center left


  for row in arr:
    print(" ".join(str(cell) for cell in row))
    print("")

if __name__ == "__main__":
  minesweeper(5)