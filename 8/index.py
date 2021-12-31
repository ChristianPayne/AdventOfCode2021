# Segment - a-g that make up a digit
# Digit - 0-9 that is made up of segments
# Display - 4 Digit combination
# Output - 1 Digit on a display but has jumbled segment locations
import csv
from collections import defaultdict
data = []
with open('./input.txt') as csv_data:
  data = [{"inputs" : row[0].strip().split(" "), "outputs" : row[1].strip().split(" ")} for row in csv.reader(csv_data, delimiter="|")]


def part1 ():
  segment_count = {
    "0" : 6,
    "1" : 2,
    "2" : 5,
    "3" : 5,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 3,
    "8" : 7,
    "9" : 6,
  }

  count_dict = defaultdict(int)
  rows = data.copy()
  for row in rows:
    # Get the length of the segments for each digit.
    # print(row["outputs"])
    for digit in row["outputs"]:
      count_dict[len(digit)] += 1

  print(count_dict.items())
  print( "The sum of 1,4,7,8 is ",
    count_dict[segment_count["1"]] +
    count_dict[segment_count["4"]] +
    count_dict[segment_count["7"]] +
    count_dict[segment_count["8"]]
  )

part1()