import cmd
import json
from services.notifier import Notifier
from services.report import ReportGenerator
from services.subscription import SubscriptionManager
from config import Config
from logger import setup_logger
from utils.github_client import GitHubClient

logger = setup_logger()
config = Config()
subscription_manager = SubscriptionManager(config.subscriptions_file)

class SentinelCLI(cmd.Cmd):
    intro = "Welcome to GitHub Sentinel! Type ? or help to see available commands.\n"
    prompt = "(sentinel) "

    def do_subscribe(self, repo):
        "Subscribe to a GitHub repository: subscribe owner/repo"
        try:
            subscription_manager.add_subscription(repo)
            logger.info(f"Subscribed to {repo}")
            print(f"Subscribed to {repo}")
        except Exception as e:
            logger.error(f"Error subscribing to {repo}: {e}")
            print(f"Error subscribing to {repo}: {e}")

    def do_unsubscribe(self, repo):
        "Unsubscribe from a GitHub repository: unsubscribe owner/repo"
        try:
            subscription_manager.remove_subscription(repo)
            logger.info(f"Unsubscribed from {repo}")
            print(f"Unsubscribed from {repo}")
        except Exception as e:
            logger.error(f"Error unsubscribing from {repo}: {e}")
            print(f"Error unsubscribing from {repo}: {e}")

    def do_list(self, _):
        "List all subscribed repositories: list"
        try:
            subscriptions = subscription_manager.get_subscriptions()
            print("Subscribed repositories:")
            for repo in subscriptions:
                print(f"- {repo}")
        except Exception as e:
            logger.error(f"Error listing subscriptions: {e}")
            print(f"Error: {e}")

    def do_config(self, args):
        "View or modify configuration: config view | config set key value"
        try:
            if args.startswith("view"):
                for key, value in config.__dict__.items():
                    print(f"{key}: {value}")
            elif args.startswith("set"):
                _, key, value = args.split()
                keys = key.split(".")
                sub_config = config
                for k in keys[:-1]:
                    sub_config = sub_config[k]
                sub_config[keys[-1]] = value
                save_config(config)
                logger.info(f"Updated configuration '{key}' to '{value}'")
                print(f"Configuration '{key}' updated to '{value}'")
            else:
                print("Invalid command. Use 'config view' or 'config set key value'.")
        except Exception as e:
            logger.error(f"Error updating configuration: {e}")
            print(f"Error: {e}")

#    def do_start_scheduler(self, _):
#        "Start the background scheduler: start_scheduler"
#        start_scheduler()

#    def do_stop_scheduler(self, _):
#        "Stop the background scheduler: stop_scheduler"
#        stop_scheduler()

    def do_fetch_updates(self, _):
        "fetch updates immediately"
        github_client = GitHubClient(config.github_token)
#        notifier = Notifier(config.notification_settings)
        report_generator = ReportGenerator(config)
        subscriptions = subscription_manager.get_subscriptions()
        try:
            updates = github_client.fetch_updates(subscriptions)
            report = report_generator.generate(updates)
            if report != None:
                print(report)
                print("Updates fetched:")
        except Exception as e:
            logger.error(f"Error listing subscriptions: {e}")
        
        
        
    def do_exit(self, _):
        "Exit the Sentinel CLI: exit"
        print("Goodbye!")
        return True

if __name__ == "__main__":
    SentinelCLI().cmdloop()
