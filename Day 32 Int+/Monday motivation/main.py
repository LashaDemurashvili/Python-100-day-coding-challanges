import random
import smtplib
from datetime import datetime

# CONSTANTS
MY_EMAIL = "test_1@gmail.com"
MY_PASSWORD = "password"
RECIPIENT_EMAIL = "test_2@gmail.com"

today = datetime.now()
weekday = today.weekday()

if weekday == 0:
    with open("quotes.txt") as data_file:
        all_quotes = data_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"subject:Monday motivation\n\n{quote}"  # \n\n for email text
                            )
