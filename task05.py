import random
import time

class HospitalEnvironment:
 def __init__(self): 
  self.corridors = ["Corridor1", "Corridor2"]
  self.rooms = {
  "Room101": {"patient_id": "P101", "medicine": "Paracetamol", "time": "10:00"},
  "Room102": {"patient_id": "P102", "medicine": "Insulin", "time": "10:00"},
  "Room103": {"patient_id": "P103", "medicine": "Antibiotic", "time": "10:00"}
  }
  self.nurse_station = "NurseStation"
  self.medicine_storage = {
  "Paracetamol": 5,
  "Insulin": 5,
  "Antibiotic": 5
  }
  self.staff_available = True

 def display_schedule(self):
  print("\nToday's Delivery Schedule")
  print("-" * 40)
  for room, data in self.rooms.items():
   print(f"{room} -> Patient: {data['patient_id']} | Medicine: {data['medicine']} | Time:{data['time']}")
  print("-" * 40)

class DeliveryRobot:
 def __init__(self, environment):
  self.env = environment
  self.location = "DockingStation"
  self.carrying = None

 def move_to(self, location):
  print(f"Moving from {self.location} to {location}")
  self.location = location
  time.sleep(0.5)

 def pick_medicine(self, medicine):
  if self.env.medicine_storage.get(medicine, 0) > 0:
   self.env.medicine_storage[medicine] -= 1
   self.carrying = medicine
   print(f"Picked up {medicine}")
  else:
   print(f"{medicine} not available in storage")
   self.alert_staff("Medicine shortage")


 def scan_patient_id(self, expected_id):
  print("Scanning patient ID...")
  scanned_id = expected_id
 
  if scanned_id == expected_id:
   print("Patient ID verified")
   return True
 
  else:
   print("Patient ID mismatch")
   self.alert_staff("ID mismatch")
   return False

 def deliver_medicine(self, room):
  if self.carrying is None:
   print("No medicine to deliver")
   return
  expected_id = self.env.rooms[room]["patient_id"]
  if self.scan_patient_id(expected_id):
   print(f"Delivered {self.carrying} to {room}")
   self.carrying = None

 def alert_staff(self, reason):
  if self.env.staff_available:
   print(f"Alerting staff: {reason}")
  else:
   print("Staff not available, logging issue")

 def execute_delivery(self):
  for room, data in self.env.rooms.items():
   self.move_to(self.env.medicine_storage)
   self.move_to("MedicineStorage")
   self.pick_medicine(data["medicine"])
   self.move_to(room)
   self.deliver_medicine(room)
   print("-" * 40)

hospital = HospitalEnvironment()

robot = DeliveryRobot(hospital)

hospital.display_schedule()
robot.execute_delivery()

print("\nAll scheduled deliveries attempted.")