# Dynamic Programming
# Show Only 1 Path
def flightPathOneSolution(graph, start, end, path=[]):
  try:
    path = path + [start] 
    if start == end: # Breakcase
      return path
    if start not in graph:
      return None
    for location in graph[start]:
      if location not in path:
        newLocation = flightPathOneSolution(graph, location, end, path)
        if newLocation:
          return newLocation
  except:
    return None

# Dynamic Programing 
# Show All Paths
def flightPathAllSolution(graph, start, end, path=[]):
  try:
    path = path + [start] # Breakcase
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
def flightPath(function, start, end):
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

  solution = []
  if function:
    solution = flightPathAllSolution(graphPath, start, end)
    sizeOfSolution = len(solution)
    if sizeOfSolution == 1:
      solution = solution[0]
    elif sizeOfSolution == 0:
      solution = None
  else:
    solution = flightPathOneSolution(graphPath, start, end)
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

# Test Solutions For One
testsAnswerOne = [
  ["NY", "Iceland", "London", "Berlin"],
  ["NY", "Iceland", "London"],
  ["Berlin", "Paris", "Amsterdam"],
  ["Paris", "London", "Egypt"],
  ["NY", "Iceland", "London", "Egypt"],
  ["NY", "Iceland", "London", "Berlin", "Paris", "Amsterdam"],
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

# Test Solutions For All
testsAnswerAll = [
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
  # Test Method:
  # 0 = Only 1 Solution
  # 1 = All Solutions
  testMethod = 1
  answer = flightPath(testMethod, test[0], test[1])
  if testMethod == 0:
    if answer == testsAnswerOne[testNumber]:
      print("Test #"+ str(testNumber) + ": Success")
    else:
      print("Test #"+ str(testNumber) + ": Failed")
  elif testMethod == 1:
    if answer == testsAnswerAll[testNumber]:
      print("Test #"+ str(testNumber) + ": Success")
    else:
      print("Test #"+ str(testNumber) + ": Failed")
