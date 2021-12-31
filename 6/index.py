from collections import defaultdict

data = []
with open('./input.txt') as csv_data:
  # Pull in raw data as strings in a list.
  # Int cast every point for every line for every row.
  data = [int(value) for value in next(csv_data).split(',')]

def Challenge_Part1_Part2 (days):
  allFish = data.copy()

  fishMap = {}
  for fish in allFish:
    if(fish not in fishMap):
      fishMap[fish] = 0
    fishMap[fish] += 1

  
  for days in range(days):
    updatedFishMap = defaultdict(int)
    for fish, count in fishMap.items():
      if(fish == 0):
        updatedFishMap[6] += count
        updatedFishMap[8] += count
      else:
        updatedFishMap[fish - 1] += count

      fishMap = updatedFishMap

  return(sum(fishMap.values()))


print(f"Final fish total is {Challenge_Part1_Part2(80)}")
print(f"Final fish total is {Challenge_Part1_Part2(256)}")
