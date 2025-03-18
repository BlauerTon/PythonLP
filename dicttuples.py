# This is a tuple
student = ("Sahsa", "Julia", "Wendi",3.3, False)
print(student)
print(student[-3])


# This is a dictionary
students = {
    "name" : "Sahsa",
    "age" : 24,
    "is_student": True,
    "courses": ["Math", "Science", "English"],
    "interests": {
        "interest1": "Swimming",
        "interest2": "Tennis"
    }
}
      #inserting data into the dictionary
students["height"] = 177

print(students)
print(students["name"])

# this is a set
student_ids = {1,2,3,4,"John", True}
print(student_ids)