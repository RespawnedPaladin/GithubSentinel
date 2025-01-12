import json

class SubscriptionManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_subscriptions(self):
        try:
            with open(self.filepath, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_subscription(self, repo):
        subscriptions = self.get_subscriptions()
        if repo not in subscriptions:
            subscriptions.append(repo)
            with open(self.filepath, "w") as file:
                json.dump(subscriptions, file, indent=4)

    def remove_subscription(self, repo):
        subscriptions = self.get_subscriptions()
        if repo in subscriptions:
            subscriptions.remove(repo)
            with open(self.filepath, "w") as file:
                json.dump(subscriptions, file, indent=4)
