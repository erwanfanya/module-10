classmates = ["Aarav", "Ahmad", "Erik","king","Donovan"]
print("Class list:", classmates)
print("Total classmates:", len(classmates))
print("First classmate:", classmates[0])
print("Last classmate:", classmates[-1])
print("First three classmates:", classmates[:3])

classmates.append("jared")
print("\n After adding jared:", classmates)
classmates.remove("king")
print("\n After removing king:",classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)


teacher = {"name": "Mr. smith", "subject": "math", "experience":4}
print("\n Teacher profile:", teacher)

print("subject:", teacher["subject"])
print("experience:",teacher.get("experience","not found"))
teacher["experiences"] = 4
teacher["email"] = "mr.smith@gmail.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)

roll_numbers = [1,2,3,4,5]

names = ["Aarav", "Ahmad", "Erik", "king", "Donovan"]
student_directory = dict(zip(roll_numbers,names))
print("\n Student directory:", student_directory)
print("student at roll 3:", student_directory[3])




