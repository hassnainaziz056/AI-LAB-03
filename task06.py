class Building:
 def __init__(self):
  self.grid = {
  'a': 'safe', 'b': 'safe', 'c': 'fire',
  'd': 'safe', 'e': 'fire', 'f': 'safe',
  'g': 'safe', 'h': 'safe', 'j': 'fire' }

 def display(self):
  print("\nEnvironment Status:")
  print("-" * 25)
  rooms = list(self.grid.keys())
  
  for i in range(0, 9, 3): 
   row = rooms[i:i+3]
   for r in row:
    if self.grid[r] == 'fire':
     print("F", end=" ")
    else:
     print(" ", end=" ")
  print()
 print("-" * 25)

class FirefightingRobot:
 def __init__(self, building):
  self.building = building
  self.position = 'a'
  self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

 def move_and_extinguish(self):
  for room in self.path:
   self.position = room
  print(f"\nRobot moved to room {room}")
  if self.building.grid[room] == 'fire':
   print(f"Fire detected in room {room}")
   self.building.grid[room] = 'safe'
   print(f"Fire extinguished in room {room}")
  else:
   print(f"Room {room} is safe")
  self.building.display()

building = Building()
robot = FirefightingRobot(building)

print("INITIAL ENVIRONMENT")
building.display()

robot.move_and_extinguish()

print("\nFINAL ENVIRONMENT")
building.display()