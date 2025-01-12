import smtplib
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, config):
        self.config = config["email"]

    def send_notification(self, message):
        msg = MIMEText(message, "html")
        msg["Subject"] = "GitHub Sentinel Daily Report"
        msg["From"] = self.config["username"]
        msg["To"] = ", ".join(self.config["recipients"])

        with smtplib.SMTP(self.config["smtp_server"], self.config["port"]) as server:
            server.starttls()
            server.login(self.config["username"], self.config["password"])
            server.send_message(msg)
