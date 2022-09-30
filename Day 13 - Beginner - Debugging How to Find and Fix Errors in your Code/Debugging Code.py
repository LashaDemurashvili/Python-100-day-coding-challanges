############DEBUGGING#####################

# # Describe Problem
# def my_function():
#     for i in range(1, 20): # 1 - 19 - not include 20 - we need 21 to execute code: correct is : range(1, 21):
#         if i == 20:
#             print("You got it")
#
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # we need (0, 5) because in randint include both 1 and 6: correct is randint(0, 5)
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:  # we need <= because 1994 not include for this code
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")


## Fix the Errors
# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


# # Fixed
# age = int(input("How old are you?"))
# if age >= 18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You need to grow up, you just {age} years old.")


# # Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# # fixed
# # Print is Your Friend
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Pages = {pages}")
# print(f"Words Per Page = {word_per_page}")
# print(f"Total word is {total_words}")


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


## fixed
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
