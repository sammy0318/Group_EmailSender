import smtplib
from email.message import EmailMessage
import ssl
import time

# ✅ Gmail credentials (use an app password, NOT your real password if 2FA is enabled)
sender_email = "xyz@gmail.com"
password = ""  # Replace with the app password generated from Google

# ✅ Recipient list
recipients = [
     

#Dont add more than 50 emails in a single run, as it may lead to your account being blocked.

]

# ✅ Email content
subject = ""

plain_text = """\

Hi Ma'am/Sir,

I hope you are doing well. 

blah blah balh 
"""

html_content = """\
<html>
  <body>
    <p>Hi Ma'am/Sir,<br><br>
        I hope you are doing well. <br><br>
         blah blah balh 
    
       Thank you for your time, and I look forward to connecting with you!
      .<br><br>

       📎 <b>Resume</b>: 
       🔗 <b>LinkedIn</b>: 
       🌐 <b>Portfolio</b>: 

       Thank you for your time and attention.<br><br>
       Best regards,<br>
       <b>XYZ</b>
    </p>
  </body>
</html>
"""

# ✅ Create and send email
context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls(context=context)
    server.login(sender_email, password)

    for email in recipients:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = email

        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype='html')

        try:
            server.send_message(msg)
            print(f"✅ Sent to {email}")
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")

        time.sleep(5)
