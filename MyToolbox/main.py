import smtplib
import random
import datetime as dt

email = "chonku@gmail.com"
password = ("")
now = dt.datetime.now()

with open("quotes.txt", "r") as file:
    lines = file.readlines()

if now.weekday() == 1:
    quote = random.choice(lines)
    print (f"Sending {quote}")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="gaurav.tyagi@toptal.com",
                            msg=f"Subject:Today's Quote\n\n {quote}".encode('utf-8'))
