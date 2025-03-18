# age = 20
#
# height  =  5.68
#
# school = "PLPAcademy"
#
# student = True
#
# print(type(age))
# print(type(height))
# print(type(school))
# print(type(student))
#
# print("Age", age)
#
# age = 34
# print(age)
# age = "Age in string"
# print(age)
#
#
# tempx = 30
#
# if (tempx > 25):
#     print ("It is a hot day")
# else:
#     print ("It is a cool day")

marks = int(input("What are your marks"))

if marks > 70:
    print("Well Done")
elif marks > 50:
    print("Nice Trial")
elif marks > 30:
    print("Try harder next time")
else:
    print("That's really a failure")

if marks % 2 == 0:
    print("You scored even marks")
else:
    print("You scored odd marks")

def marksot (name):
    print("Hello" + name + "you scored" + "marksot")

marksot("Alice")