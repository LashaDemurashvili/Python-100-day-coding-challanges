student_dict = {
    "student": ["lasha", "gio", "beka"],
    "score": [67, 89, 68]
}

# # looping through dictionaries
# for key, value in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)


