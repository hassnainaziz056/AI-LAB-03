import random

class SecuritySystem:
 def __init__(self):
  self.components = {}
  states = ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"]
  for i in range(65, 74):
   self.components[chr(i)] = random.choice(states)
 
 
 def display_system(self):
  print("\nSystem Status:")
  print("-" * 40)
  for comp, state in self.components.items():
   print(f"Component {comp}: {state}")
  print("-" * 40)

class UtilityBasedSecurityAgent:
 def __init__(self):
  self.low_risk_list = []
  self.high_risk_list = []

 def scan_system(self, system):
  print("\nScanning System...")
  print("-" * 40)
  for comp, state in system.components.items():
   if state == "Safe":
    print(f"[SUCCESS] Component {comp} is Safe.")
   elif state == "Low Risk Vulnerable":
    print(f"[WARNING] Component {comp} has Low Risk Vulnerability.")
    self.low_risk_list.append(comp)
   elif state == "High Risk Vulnerable":
    print(f"[CRITICAL] Component {comp} has High Risk Vulnerability.")
    self.high_risk_list.append(comp)
 print("-" * 40)

 def patch_vulnerabilities(self, system):
  print("\nPatching Low Risk Vulnerabilities...")
  print("-" * 40)
  for comp in self.low_risk_list:
   system.components[comp] = "Safe"
   print(f"[PATCHED] Component {comp} Low Risk Vulnerability fixed.")
  
  for comp in self.high_risk_list:
   print(f"[ACTION REQUIRED] Component {comp} requires Premium Service for High Risk patch.")
  print("-" * 40)
  self.low_risk_list.clear()

system = SecuritySystem()

print("INITIAL SYSTEM CHECK")
system.display_system()

agent = UtilityBasedSecurityAgent()
agent.scan_system(system)

agent.patch_vulnerabilities(system)

print("\nFINAL SYSTEM CHECK")
system.display_system()