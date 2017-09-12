#!/usr/bin/env python
import pickle

classroom = [
    {
        "name": "Jimmy",
        "grades":
         {
              "French": 10,
              "English": 14,
              "Math": 8,
              "History": 12,
              "Science": 6
        }
    },
    {
        "name": "Bob",
        "grades":
         {
              "French": 10,
              "English": 14,
              "Math": 8,
              "History": 12,
              "Science": 6
        }
    },
    {
        "name": "Jennifer",
        "grades":
         {
              "French": 18,
              "English": 18,
              "Math": 16,
              "History": 15,
              "Science": 16
        }
    }
]

with open("classroom.pickle", "w") as f:
    pickle.dump(classroom, f)
 
def student_code(): 
@    @pickling@@

student_code()
data = []

with open("classroom.pickle", "r") as f:
    data = pickle.load(f)
    
data_ok=True

for student in data:
    if student["name"] == "Jimmy":
        for grade in student["grades"]:
            if student["grades"][grade] < 10:
                data_ok = False

print data_ok