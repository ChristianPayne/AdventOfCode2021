
data = []
with open('./test_data.txt') as csv_data:
  # Pull in raw data as strings in a list.
  # Int cast every point for every line for every row.
  data = [int(value) for value in next(csv_data).split(',')]
  counts = {}
  for val in data:
    counts[str(val)] = data.count(val)
  data = list(set(data))

  print(data)

  print(counts)

  

# print(len(data))
# print(len(set(data)))