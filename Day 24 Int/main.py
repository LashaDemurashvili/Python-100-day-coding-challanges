"""
my_dict = {
    'name': 'lasha',
    'surname': 'demurashvili'
}
for i, [k, v] in enumerate(my_dict.items(), 1):
    print(f"{i}. {k} - {v}")


me = 'Hello my name is lasha demurashvili, and I am 25'
print(me.split())

print('my name'.ljust(10, '/'))

"""


# code with nonajanashia
# day23 save_01


def process_data(data):
    match data:
        case 1:
            print(1)
        case 3:
            print(3)
        case 4:
            print(4)


process_data(1)
process_data(44)
