import csv
from typing import List


data = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]
with open('./input.txt') as csv_data:
  # Pull in raw data as strings and organize into rows, getting rid of arrows.
  raw_data = [[row[0].split(','), row[2].split(',')] for row in csv.reader(csv_data, delimiter=" ")]
  # Int cast every point for every line for every row.
  data = [[[int(point) for point in line] for line in row] for row in raw_data]

def print_grid ():
  get_grid_rows = (y for y in grid)
  for _ in range(len(grid)):
    print(next(get_grid_rows))

def add_to_point (x ,y):
  grid[y][x] += 1

def make_line (line_points: List[List[int]]):
  # Make variables easier to read.
  x1 = line_points[0][0]
  y1 = line_points[0][1]
  x2 = line_points[1][0]
  y2 = line_points[1][1]

  # Calculate line direction
  xVal1 = x1 if x1 < x2 else x2
  xVal2 = x2 if x2 > x1 else x1
  yVal1 = y1 if y1 < y2 else y2
  yVal2 = y2 if y2 > y1 else y1

  # Add a check to make sure we are looking at straight lines only.
  if(x1 != x2 and y1 != y2): 
    print(f"Diagonal Line: {line_points}")
    # Calculate the points individually.
    x_points = [x for x in range(xVal1 , xVal2 + 1)]
    if x1 > x2:
      x_points.reverse()
    y_points = [y for y in range(yVal1 , yVal2 + 1)]
    if y1 > y2:
      y_points.reverse()

    # Build the new point list.
    points = []
    for i, _ in enumerate(x_points):
      points.append([x_points[i], y_points[i]])

    # print(points)
    # Loop through the final points and add them.
    for point in points:
      add_to_point(point[0],point[1])
  else:
    print(f"Straight Line: {line_points}")
    # Increment for all points on line.
    for x in range(xVal1 , xVal2 + 1):
      for y in range(yVal1 , yVal2 + 1):
        add_to_point(x,y)

# Draw all the lines
for line in data:
  make_line(line)

# Sum all the points that 2 or more lines overlap.
print(f"Final sum of two or more lines: {sum([len([val for val in row if val >= 2]) for row in grid if any(val >= 2 for val in row)])}")

# print_grid()