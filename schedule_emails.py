import smtplib
import time
import os
from dotenv import load_dotenv 
from make_pairings import make_pairings, get_emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE

dotenv_path = './env/email.env'
load_dotenv(dotenv_path=dotenv_path)

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

html = """\
<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
    <h2>Hi {partner1} 🙏 I'm empowHER  👩‍💻 ! Today is your lucky day! </h2>
    <p>If you're receiving this message, this means you've signed up to meet other members ☺️ </p> 
    <p>Have fun this week getting to know your members! I'm sure you'd have lots of fun getting to know each other. </p> 
    <p><a href="https://kuhuhalder.notion.site/empowHER-Mentorship-Guide-13d4696ed6c946b4acfed4756d614df2">Here are some suggestions for what to do when you can hangout or some questions to ask your mentor/mentee. </a></p>
    <p> Here are the contact details of your buddy/s: </p>
    <ul>
    {contact_details}
    </ul>
    <p>Have a great day 🎉 </p>
</div>
"""

def get_contact_details(paired_people, email, name):
    # Find all the paired people for this person
    buddies = [p for p in paired_people if p[0] == email or p[2] == email]
    contact_details_html = ""
    for buddy in buddies:
        # Find the name and email of this person's buddy
        buddy_name = buddy[1] if buddy[0] == email else buddy[3]
        buddy_email = buddy[2] if buddy[0] == email else buddy[0]
        contact_details_html += f"<li>{buddy_name} ({buddy_email})</li>"
    return contact_details_html

def send_email(sender, recipient, to_name, contact_details):
    to_email = recipient if type(recipient) == str else COMMASPACE.join(recipient)
    contact_details_html = ""
    for buddy_name, buddy_email in contact_details:
        contact_details_html += f"<li>{buddy_name} ({buddy_email})</li>"
    message = MIMEMultipart('related')
    message['Subject'] = 'Your EmpowHER buddy is here!'
    message['From'] = sender
    message['To'] = to_email
    html_body = MIMEText(html.format(partner1=to_name[0], contact_details=contact_details_html), 'html')
    message.attach(html_body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(sender, recipient, message.as_string())

def send_emails(paired_people):
    for pair in paired_people:
        email1, name1, email2, name2 = pair
        send_email(EMAIL_ADDRESS, email1, (name1, name2), [(name2, email2)])
        send_email(EMAIL_ADDRESS, email2, (name2, name1), [(name1, email1)])

if __name__ == '__main__':
    emails_and_names = get_emails()
    pairings = make_pairings(emails_and_names)
    send_emails(pairings)
