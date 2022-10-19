class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1  # other account
        self.following += 1  # self


user_01 = User("001", "lasha")
user_02 = User("002", "beka")

user_01.follow(user_02)

print(user_01.followers, "followers", "of user_01")
print(user_01.following, "following", "of user_01")

print()

print(user_02.followers, "followers", "of user_02")
print(user_02.following, "following", "of user_02")



