numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

e_num = [n for n in numbers if n % 2 == 0]
print(e_num)

o_num = [n for n in numbers if n % 2 != 0]
print(o_num)


print(numbers == sorted(e_num + o_num))
