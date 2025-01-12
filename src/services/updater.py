from utils.github_api import GitHubAPI

class UpdateFetcher:
    def __init__(self, github_token):
        self.api = GitHubAPI(github_token)

    def fetch_updates(self, subscriptions):
        updates = {}
        for repo in subscriptions:
            updates[repo] = self.api.get_latest_commits(repo)
        return updates
