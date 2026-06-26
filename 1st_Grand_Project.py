print("=" * 50)
print("        🧪 Project 1 — Student Grade Manager")
print("=" * 50)

students = []
marks = []

for i in range(1, 4):
    name = input(f"Enter the Name of Student_{i}: ")
    mark = int(input(f"Enter the Marks of {name} (0-100): "))
    marks.append(mark)       # ✅ mark — variable
    students.append(name)

grades = []
for n in marks:
    if n >= 90:
        grades.append("A+ 🌟")
    elif n >= 80:
        grades.append("A 🎉")
    elif n >= 70:
        grades.append("B 👍")
    elif n >= 60:
        grades.append("C 📚")
    elif n >= 50:
        grades.append("D ⚠️")
    else:
        grades.append("F ❌")

# ✅ Table print
print("\n" + "=" * 50)
print(f"{'Name':<15} | {'Marks':^7} | {'Grade':^8}")
print("=" * 50)

for name, mark, grade in zip(students, marks, grades):
    print(f"{name:<15} | {mark:^7} | {grade:^8}")

print("=" * 50)

# ✅ Average
avg = sum(marks) / len(marks)
print(f"\n📊 Class Average: {avg:.1f}")
print("=" * 50)