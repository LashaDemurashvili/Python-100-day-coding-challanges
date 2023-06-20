"""
Program Descriptions
Day 5 - Beginner - Python Loops

Program Desc:
calculate average height
"""


info = """
# input format: 175 187 196
# NOTE: separated by only space
"""
print(info)

try:
    student_heights = input("Input a list of student heights: ").split()

    ln = 0
    sm = 0

    for i in student_heights:
        ln += 1

    for i in student_heights:
        sm += int(i)

    print(f"Number of students: {ln}")
    print(f"Sum of the students height: {sm}")
    average = sm / ln

    # round result :.0f
    print(f"Average height is {average:.0f}")
except Exception as e:
    print(e)