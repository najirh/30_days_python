# This application send email

import smtplib #this is the main lib
from email.mime.text import MIMEText    #text 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase #this for including attachment
from email import encoders # this function is going encode the attachment
import os


# setup email config
# smtp_server = "smpt.google.com"
smtp_server = "mail.zeroanalyst.com"
smtp_port = 587
sender_mail = "dev@zeroanalyst.com"
email_password = "admin@1234!"
receiver_mail = "business.najir@gmail.com"

#mail
subject = "This mail include attachment"
body = "Hi this is a test mail from Python"

# compose mail
message = MIMEMultipart()
message["From"] = sender_mail
message["To"] = receiver_mail
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


# include attachment
file_path = ['img1.png', 'orders.csv']

for file in file_path:
    if os.path.exists(file):
        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)  
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(file)}",
            )
            message.attach(part)
    else:
        print(f"File path doesn't {file} exists")
        

try:
    # setup 
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()   #start the server

    # login to our account
    server.login(sender_mail, email_password)

    # send mail
    server.sendmail(sender_mail, receiver_mail, message.as_string())
    print("mail sent!")
except Exception as e:
    print(f"Unable to send mail {e}")













# to
# from
# subject
# body = 