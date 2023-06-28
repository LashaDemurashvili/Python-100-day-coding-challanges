
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"  # check if guess == "a"
    else:
        return guess == "b"


x = check_answer("b", 12, 111)
print(x)
