def fileReader(file):
    with open(file) as file:
        f_read = file.readlines()
        f_nums = [int(i.replace("\n", "")) for i in f_read]
        return f_nums


file1 = fileReader('file1.txt')
file2 = fileReader('file2.txt')

print(file1)

# check match numbers
result = [num for num in file1 if num in file2]
print(result)

