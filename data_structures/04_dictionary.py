student = {"name": "Auli", "age": 20, "grade": "A"}
print("===== Info of",student["name"],"======")

student["city"] = "Dhaka"
student["age"] = 21
student["grade"] = "A"

for key, value in student.items():
    print(f"{key}: {value}")
