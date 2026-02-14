import random

class SecuritySystem:
    
    def __init__(self):
        self.components = {}
        for i in range(65, 74):
            comp = chr(i)
            self.components[comp] = random.choice([True, False])

    def display_system(self):
        print("\nSystem Status:")
        print("-" * 30)
        for comp, status in self.components.items():
            state = "Safe" if status else "Vulnerable"
            print(f"Component {comp}: {state}")
        print("-" * 30)


class SecurityAgent:
    
    def __init__(self):
        self.vulnerable_list = []

    def scan_system(self, system): 
        print("\nScanning System...")
        print("-" * 30)
        for comp, status in system.components.items():
            if not status:
                print(f"[WARNING] Component {comp} is Vulnerable!")
                self.vulnerable_list.append(comp)
            else:
                print(f"[SUCCESS] Component {comp} is Secure.")
        print("-" * 30)

    def patch_vulnerabilities(self, system):  
        print("\nPatching Vulnerabilities...")
        print("-" * 30)
        for comp in self.vulnerable_list:
            system.components[comp] = True
            print(f"[PATCHED] Component {comp} has been secured.")
        print("-" * 30)
        self.vulnerable_list.clear()


system = SecuritySystem()
print("INITIAL SYSTEM CHECK")
system.display_system()

agent = SecurityAgent()
agent.scan_system(system)

agent.patch_vulnerabilities(system)

print("\nFINAL SYSTEM CHECK")
system.display_system()