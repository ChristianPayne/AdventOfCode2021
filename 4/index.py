import csv

boards = []
numbers = []
with open('./input.txt') as csv_file:
  csv = csv.reader(csv_file, delimiter=' ')
  numbers = next(csv)
  boards = [board for board in csv if len(board) != 0]

# print(boards)

class Number:
  value = 0
  marked = False

  def __init__(self, value):
      self.value = value

  def mark (self):
    self.marked = True

class Row:
  numbers = []
  
  def __init__(self, numbers):
      self.numbers = [Number(num) for num in numbers]

  def markNumber (self, number):
    for num in self.numbers:
      if(num.value == number):
        num.mark()
  
  def winCheck (self) -> bool:
    marks = [num.marked for num in self.numbers if num.marked == True]
    # print(f"Row: Marks = {marks}")
    if(len(marks) == len(self.numbers)):
      return True
    else:
      return False
    

class Board:
  name = 0
  rows = []
  won = False
  def __init__(self, rows):
       self.rows = [Row(row) for row in rows]

  def markNumber (self, number):
    for row in self.rows:
      row.markNumber(number)

  def winCheck (self) -> bool:
    # Check to see if we have a win on a row.
    wins = [row.winCheck() for row in self.rows if row.winCheck() == True]
    if (len(wins) >= 1):
      return True
    
    # We also need to do a column check here.
    for i in range(len(self.rows[0].numbers)):
      marks = [row.numbers[i] for row in self.rows if row.numbers[i].marked == True]
      if(len(marks) == len(self.rows)):
        return True
    
    return False

    # If the number we pass matches in the row, change that num to marked = True
    # Then run look through every board to check for a win.

  # def markNumber (self):
  #   pass

board1 = Board([
  [1,2,123],
  [1,2,789],
  [12,12,12],
])

board1.markNumber(12)
print(board1.winCheck())


# Pull in data from input file.
# Parse data by into an array.
# Assign first chunk to a numbers array.
# Find a way to find line breaks.
  # Numbers are comma delimited ,
  # Boards are return delimited \r
  # Board numbers are space delimited. " "