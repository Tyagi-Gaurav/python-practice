##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

email = "chonku@gmail.com"
password = ("")

templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
now = dt.datetime.now()

for data in birthday_data:
    if data["month"] == now.month and data["day"] == now.day:
        template = random.choice(templates)
        with open(f"letter_templates/{template}", "r") as file:
            content = file.readlines()
            contents = "".join(content)

        new_content = contents.replace("[NAME]", data["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs="gaurav.tyagi@toptal.com",
                                msg=f"Subject:Happy Birthday\n\n {new_content}".encode('utf-8'))

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.




