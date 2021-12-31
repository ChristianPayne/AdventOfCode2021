data = []
with open('./input.txt') as csv_data:
  # Pull in raw data as strings in a list.
  # Int cast every point for every line for every row.
  data = [int(value) for value in next(csv_data).split(',')]

def part1():
  lowest_sum = 1000000000000000000000
  for mark in range(len(data)):
    calc = sum([abs(mark - pos) for pos in data])
    if(calc < lowest_sum):
      lowest_sum = calc

  print (f"Part 1: Lowest sum {lowest_sum}")

def add_up_fuel (units_away) -> int:
  return sum([index for index, _ in enumerate(range(units_away))]) + units_away

def part2():
  lowest_sum = 1000000000000000000000
  for mark in range(len(data)):
    calc = sum([add_up_fuel(abs(mark - pos)) for pos in data])
    if(calc < lowest_sum):
      lowest_sum = calc

  print (f"Part 2: Lowest sum {lowest_sum}")
  # 97998838 too low
  # 98363777 correct!

part1()
part2()