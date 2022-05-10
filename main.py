import datetime
import smtplib
import random

my_email = "sdeveloper444@gmail.com"
password = "206480220aB"

now = datetime.datetime.now()
if now.weekday() == 1:
    with open("Birthday Wisher (Day 32) start/quotes.txt") as data:
        quote_list = data.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="michaelkleyman99@gmail.com",
                            msg=f"Subject:Weekly Motivation\n\n{random.choice(quote_list)}\nSincerely Michael Kleyman")


