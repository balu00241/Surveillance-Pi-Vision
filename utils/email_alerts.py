# utils/email_alerts.py
import smtplib
from email.mime.text import MIMEText

def send_alert(message, to_email='badambalu8@gmail.com'):
    from_email = 'balujoker8@gmail.com'  # Replace with your Gmail address
    password = 'knok nauy meaa lqoa'           # Replace with your Gmail password or App Password
    msg = MIMEText(message)
    msg['Subject'] = 'Motion Detected At Your Property'
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
        print("Alert sent successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")
