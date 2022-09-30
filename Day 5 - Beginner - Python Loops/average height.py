# input like this - 175 187 196
# separated by only space

student_heights = input("Input a list of student heights ").split()

# average = ?

ln = 0
sm = 0

for i in student_heights:
    ln += 1

for i in student_heights:
    sm += int(i)

print(ln)
print(sm)
average = sm/ln

print(f"Average height is {average}")