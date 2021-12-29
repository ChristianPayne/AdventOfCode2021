import csv
from typing import List, final
# print(boards)

class Number:
  value = 0
  marked = False

  def __init__(self, value):
      self.value = value

  def mark (self):
    self.marked = True
    # print("I got a mark!")

class Row:
  numbers = []
  
  def __init__(self, numbers):
      self.numbers = [Number(num) for num in numbers]
      # print([num.value for num in self.numbers])

  # If the number we pass matches in the row, change that num to marked = True
  def markNumber (self, number):
    for num in self.numbers:
      # print(f"Checking {num.value} against {number}")
      if(num.value == number):
        num.mark()
        
  
  def winCheck (self) -> bool:
    marks = [num.marked for num in self.numbers if num.marked == True]
    if(len(marks) == len(self.numbers)):
      return True
    else:
      return False
    
  def sumUnmarked (self) -> int:
    return sum([num.value for num in self.numbers if num.marked == False])

class Board:
  name = 0
  rows = []
  won = False
  def __init__(self, rows):
       self.rows = [Row(row) for row in rows]

  def markNumber (self, number):
    for row in self.rows:
      row.markNumber(number)

  def winCheck (self):
    # Check to see if we have a win on a row.
    wins = [row.winCheck() for row in self.rows if row.winCheck() == True]
    if (len(wins) >= 1):
      self.won = True
      # print("Won with a row!")
    
    # We also need to do a column check here.
    for i in range(len(self.rows[0].numbers)):
      marks = [row.numbers[i] for row in self.rows if row.numbers[i].marked == True]
      if(len(marks) == len(self.rows)):
        self.won = True
        # print("Won with a column!")

  def sumUnmarked (self) -> int:
    return sum([row.sumUnmarked() for row in self.rows])


# Board Setup
boards: List[Board] = []
numbers: List[int] = []
with open('./input.txt') as csv_file:
  csv = csv.reader(csv_file, delimiter=' ')
  rawNumbers = next(csv)[0]
  numbers = [int(number) for number in rawNumbers.split(',')]
  boardData = [
    [int(num) for num in board if len(num) > 0] 
    for board in csv if len(board) != 0]
  
  boardQueue = []
  for index,row in enumerate(boardData):
    if((index + 1) % 5 == 0):
      boardQueue.append(row)
      newBoard = Board(boardQueue)
      boards.append(newBoard)
      boardQueue = []
      # print(f"New Board {newBoard}")
    else:
      boardQueue.append(row)

# Lets play
def Play ():
  winningBoards: List[Board] = []
  finalNumber = 0
  for number in numbers:
    if(len(winningBoards) == len(boards)):
      break
    else:
      print(f"{len(winningBoards)} | {len(boards)}")

    print(f"New Number {number}")
    for board in [board for board in boards if board.won == False]:
      board.markNumber(number)
      board.winCheck()
      if(board.won):
        # print(f"Board Won!")
        winningBoards.append(board)
        finalNumber = number
        # print(finalNumber)
  # print(winningBoards)
  print(f"Last winning board {winningBoards[-1].name} with number {finalNumber}")
  print([[num.marked for num in row.numbers] for row in winningBoards[-1].rows])
  print(f"Final Score: {winningBoards[-1].sumUnmarked() * finalNumber}")
Play()



# board1 = Board([
#   [1,2,123],
#   [1,2,789],
#   [12,12,12],
# ])

# board1.markNumber(12)
# print(board1.winCheck())
