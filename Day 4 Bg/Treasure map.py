"""
Day 4 - Beginner - Randomisation and Python Lists

Program Descriptions:

Condition of the task:
directory ==> Images/Treasure Map.png
"""

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
print("from ==> 11 to 33")
position = input("Where do you want to put the treasure?\n: ")


y = int(position[0])-1
x = int(position[1])-1
map[x][y] = "X"

print(f"{row1}\n{row2}\n{row3}")




