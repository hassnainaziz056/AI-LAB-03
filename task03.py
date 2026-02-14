import random

class BackupSystem:
 def __init__(self):
  self.tasks = []
  for i in range(1, 8):
   status = random.choice(["Completed", "Failed"])
   self.tasks.append({"Task": f"Backup{i}", "Status": status})

 def display_tasks(self):
  print("\nBackup Task Status:")
  print("-" * 35)
  for task in self.tasks:
   print(f"{task['Task']}: {task['Status']}")
 print("-" * 35)

class BackupManagementAgent:
 def retry_failed_backups(self, system):
  print("\nScanning for Failed Backups...")
  print("-" * 35)
  for task in system.tasks:
   if task["Status"] == "Failed":
    print(f"Retrying {task['Task']}...")
    task["Status"] = "Completed"
    print(f"{task['Task']} is now Completed.")
  print("-" * 35)

system = BackupSystem()
print("INITIAL BACKUP STATUS")
system.display_tasks()

agent = BackupManagementAgent()
agent.retry_failed_backups(system)

print("\nFINAL BACKUP STATUS")
system.display_tasks()