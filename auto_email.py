import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

def send_email(subject, body, to_email):
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL
    
    # Sender email and password
    sender_email = "fwoodwar@gmail.com"
    sender_password = "@rmyDud3"  # It's recommended to store sensitive data securely!

    # Create a secure SSL context
    context = ssl._create_unverified_context()
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
send_email("Automation Test", "This is an automated email.", "fwoodwar@gmail.com")