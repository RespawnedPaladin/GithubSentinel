import json
import os

CONFIG_FILE = "config.json"

class Config:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.open_ai_key = os.getenv("OPENAI_API_KEY")
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.load_config()
    
    def load_config(self):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            self.notification_settings = config.get('notification_settings')
            self.subscriptions_file = config.get('subscriptions')
            self.report_settings=config.get('report')
            self.update_interval = config.get('update_interval', 24 * 60 * 60)  # Default to 24 hours

    def save_config(config):
        with open(CONFIG_FILE, "w") as file:
            json.dump(CONFIG_FILE, file, indent=4)