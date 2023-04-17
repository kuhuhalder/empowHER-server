import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv 
dotenv_path = './env/email.env'
load_dotenv(dotenv_path=dotenv_path)
#email configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
<<<<<<< HEAD
EMAIL_PASSWORD = os.getenv('PASSWORD')

=======
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
print(os.getenv('EMAIL_ADDRESS'))
print(os.getenv('EMAIL_PASSWORD'))
>>>>>>> 18a7aacf34df18b3f508c85c34517ac156bec8a2
def no_buddy(buddy, msg):
    #content of email  
    msg['To'] = buddy[0]  #access email
    html="""<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
            <h2>Hi $(partner1) 👋  I'm empowHER  🤖 ! You've got mail 💌</h2>
            <p>If you're receiving this message, this means you've signed up to meet other members ☺️ </p> 
            <p>Take a break this week and treat yourself to some me-time! You will receive a new buddy/s the following week. </p> 
            <p>Have a great day ⚡️ </p>

        </div>"""
    html = html.replace("$(partner1)", buddy[1])
    msg.set_content(html, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)

    
def main(pairs):

    for pair in pairs: 
        msg = EmailMessage() #instantiate email message class to send email
        msg['Subject'] = 'empowHER Buddy Bot Pair!'
        msg['From'] = EMAIL_ADDRESS
        
        #content of email  
        #access email at pair[whatever person they are, 1 or 0][0]
        if pair[1][0] == '0':
            print(pair[0][1] + " does not have a buddy")
            no_buddy(pair[0], msg)
        elif pair[0][0] == '0':
            print(pair[1][1] + " does not have a buddy")
            no_buddy(pair[1], msg)            
        else:
            #content of email  
            # msg['To'] = [pair[0][0], pair[1][0]]  #access email
            msg['To'] = 'achuth810@gmail.com'
            html="""<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
                    <h2>Hi 👋  I'm the WiCS Buddy Bot 🤖 ! You've got mail 💌</h2>
                    <p>If you're receiving this message, this means you've signed up to meet other members of WiCS ☺️ </p> 
                    <p>Here is your buddy pod for the week:</p> 
                    <ul style="list-style-type:none;">
                        <li>$(partner1)</li>
                        <li>$(partner2)</li>
                    </ul>
                    <p>Please contact them via email. Have a great day ⚡️ </p>

                </div>"""
            html = html.replace("$(partner1)", pair[0][1])
            html = html.replace("$(partner2)", pair[1][1])

            msg.set_content(html, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
                smtp.send_message(msg)

    return

pairs = [[('achuth810@gmail.com', 'Jane'), ('achuth.nair@rutgers.edu', 'John')]]
main(pairs)
