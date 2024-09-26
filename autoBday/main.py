
import pandas
import smtplib
import datetime
import random

birthdays = pandas.read_csv("birthdays.csv")

today = datetime.datetime.today()

day, month = today.day, today.month

matches = birthdays[(birthdays["day"] == day) & (birthdays["month"] == month)]

if not matches.empty:
    for index, row in matches.iterrows():
        name = row["name"]
        number = random.randint(1,3)
        if number == 1:
            with open("letter_1.txt","r") as letter:
                template = letter.read()
        elif number == 2:
            with open("letter_2.txt","r") as letter:
                template = letter.read()
        elif number == 3:
            with open("letter_3.txt","r") as letter:
                template = letter.read()

        template = template.replace("[NAME]", name)

        my_email = "zamusgm97@gmail.com"
        passwd = "despjrtuyhasayru"

        connection = smtplib.SMTP("smtp.gmail.com")

        connection.starttls()
        connection.login(user=my_email, password=passwd)
        connection.sendmail(from_addr=my_email, to_addrs="zamusgm97@gmail.com",
                             msg=f"Subject:Birthday Letter\n\n {template}")
        connection.close()
else:
    print("No Birthdays Today")










