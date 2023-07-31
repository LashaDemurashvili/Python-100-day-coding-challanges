my_dict = {
    'name': 'lasha',
    'surname': 'demurashvili'
}
for i, [k, v] in enumerate(my_dict.items(), 1):
    print(f"{i}. {k} - {v}")


print(my_dict['name'][0])