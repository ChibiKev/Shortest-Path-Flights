# Dynamic Programing 
# Show All Paths
def flightPathAllSolution(graph, start, end, path=[]):
  try:
    path = path + [start]
    if start == end:
      return [path]
    if start not in graph:
      return []
    paths = []
    for location in graph[start]:
      if location not in path:
        newLocations = flightPathAllSolution(graph, location, end, path)
        for newLocation in newLocations:
          paths.append(newLocation)
    return paths
  except:
    return None
    
# Function For Path
def flightPath(start, end):
  # Graph of Path
  graphPath = {
    "NY": ["Iceland", "Maine"],
    "Iceland": ["London"],
    "Maine": ["London"],
    "London": ["Egypt","Berlin"],
    "Berlin": ["Paris"],
    "Paris": ["London", "Amsterdam"],
    "Egypt": [None],
    "Amsterdam": [None]
  }

  solution = flightPathAllSolution(graphPath, start, end)
  sizeOfSolution = len(solution)
  if sizeOfSolution == 1:
    solution = solution[0]
  elif sizeOfSolution == 0:
    solution = None
  return solution

# Tests
tests = [
  ["NY", "Berlin"],
  ["NY", "London"],
  ["Berlin", "Amsterdam"],
  ["Paris", "Egypt"],
  ["NY", "Egypt"],
  ["NY", "Amsterdam"],
  ["Amsterdam", "London"],
  ["NY", "NY"],
  ["Amsterdam", "NY"],
  ["Egypt", "Paris"],
  ["Berlin", "Maine"],
  ["Paris", "Iceland"],
  ["London", "London"],
  ["Berlin", "Germany"],
  ["Maine", 0],
  ["Paris", "London"]
]

# Test Solutions
testsSolutions = [
  [["NY", "Iceland", "London", "Berlin"], ["NY", "Maine", "London", "Berlin"]],
  [["NY", "Iceland", "London"], ["NY", "Maine", "London"]],
  ["Berlin", "Paris", "Amsterdam"],
  ["Paris", "London", "Egypt"],
  [["NY", "Iceland", "London", "Egypt"], ["NY", "Maine", "London", "Egypt"]],
  [["NY", "Iceland", "London", "Berlin", "Paris", "Amsterdam"], ["NY", "Maine", "London", "Berlin", "Paris", "Amsterdam"]],
  None,
  ["NY"],
  None,
  None,
  None,
  None,
  ["London"],
  None,
  None,
  ["Paris", "London"]
]

# Running Tests
for testNumber in range(len(tests)):
  test = tests[testNumber]
  answer = flightPath(test[0], test[1])
  if answer == testsSolutions[testNumber]:
    print("Test #"+ str(testNumber) + ": Success")
  else:
    print("Test #"+ str(testNumber) + ": Failed")

# Manual Input
while True:
  print("Theses are the locations you can travel to:\nNY, Iceland, Maine, London, Egypt, Berlin, Paris, Amsterdam")
  start = input("Where is your origin?\n")
  end = input("Where is your destination?\n")
  answer = flightPath(start, end)
  print("The shortest path to your location is:")
  print(answer)
  if input("Continue? Yes (Y) or No (N)\n") == 'N':
    break