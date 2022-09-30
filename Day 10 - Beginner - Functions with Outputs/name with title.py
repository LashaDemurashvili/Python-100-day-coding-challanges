def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You should write four >> first << and >> last << name"
    return f"{f_name} {l_name}".title()

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
