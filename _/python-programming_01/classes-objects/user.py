class User:
    def __init__(self, user_name, user_email, user_password, user_current_job):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.job = user_current_job

    def change_password(self, new_password):
        self.password = new_password

    def change_job(self, new_job):
        self.job = new_job

    def user_info(self):
        print(f"User: {self.name.title()} current job is {self.job}, you can contact she/he at {self.email}.")


ls = User("lasha", "lasha@test.com", "pass123", "CurrentJob")

ls.user_info()

