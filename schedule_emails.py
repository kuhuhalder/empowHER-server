import smtplib
import schedule
import time
import os

# list of paired emails and names
paired_people = [('email1', 'name1', 'email2', 'name2'), ('email3', 'name3', 'email4', 'name4'), ...]

# email content
email_content = """\
Subject: Your WiCS Buddy 🤖

Hi {name1} and {name2},

This is just a friendly reminder that you are each other's WiCS buddy for this week! Please take the time to connect with each other and discuss anything WiCS-related or just catch up on life.

Have a great week!

Best regards,
WiCS Buddy Bot 🤖
"""

# sender email account details
sender_email = os.environ.get('EMAIL_ADDRESS')
sender_password = os.environ.get('PASSWORD')

def send_email(to_email, to_name):
    # replace {name1} and {name2} with the corresponding names
    email_text = email_content.format(name1=to_name[0], name2=to_name[1])
    
    # connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # login to the sender email account
        smtp.login(sender_email, sender_password)

        # send the email
        smtp.sendmail(sender_email, to_email, email_text)

def send_emails():
    for pair in paired_people:
        email1, name1, email2, name2 = pair
        send_email(email1, (name1, name2))
        send_email(email2, (name2, name1))

# schedule the sending of the emails every Friday at 9:00 AM
schedule.every().friday.at("09:00").do(send_emails)

while True:
    # run the scheduled tasks
    schedule.run_pending()
    
    # wait for 1 minute before checking the schedule again
    time.sleep(60)
