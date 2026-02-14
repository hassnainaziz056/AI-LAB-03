import random
class DataCenter:
 def __init__(self):
  self.servers = {}
  states = ["Underloaded", "Balanced", "Overloaded"]
  for i in range(1, 6):
   self.servers[f"Server{i}"] = random.choice(states)

 def display_status(self):
  print("\nServer Load Status:")
  print("-" * 35)
  for server, state in self.servers.items():
   print(f"{server}: {state}")
  print("-" * 35)

class LoadBalancer:
 def scan_and_balance(self, datacenter):
  overloaded = []
  underloaded = []
  for server, state in datacenter.servers.items():
   if state == "Overloaded":
    overloaded.append(server)
   elif state == "Underloaded":
    underloaded.append(server)
  
  while overloaded and underloaded:
   o_server = overloaded.pop()
   u_server = underloaded.pop()

   datacenter.servers[o_server] = "Balanced"
   datacenter.servers[u_server] = "Balanced"

   print(f"Moved tasks from {o_server} to {u_server}.")

datacenter = DataCenter()
print("INITIAL SYSTEM STATE")
datacenter.display_status()
agent = LoadBalancer()

print("\nBalancing Load...")
agent.scan_and_balance(datacenter)

print("\nFINAL SYSTEM STATE")
datacenter.display_status()