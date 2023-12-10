# main app

from user import User
from post import Post

ls = User("lasha", "lasha@test.com", "pass123", "CurrentJob")
ls.get_user_info()

# change job
ls.change_job("newJob")
ls.get_user_info()

person_1 = User("person1", "person11@gmai.com", "password111", "developer")
person_1.get_user_info()

new_post = Post("Posting new articles!", ls.name)
new_post.get_post_info()
