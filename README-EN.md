# GitHub Sentinel

GitHub Sentinel is an open-source tool AI Agent designed for developers and project managers. It automatically retrieves and aggregates updates from subscribed GitHub repositories on a regular basis (daily/weekly). Key features include subscription management, update retrieval, notification system, and report generation.

## Features
- Subscription management
- Update retrieval
- Notification system
- Report generation

## Environment requirements
- Python 3.10+
- GitHub access token

## Getting Started
1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Configure the application by editing `config.json`.
## Configuration
The configuration file `config.json` should contain the following settings:
```json
{
    "subscriptions": "subscriptions.json",
    "notification": {
        "email": {
            "smtp_server": "smtp.example.com",
            "port": 587,
            "recipients": ["recipient@example.com"]
        }
    },
    "report": {
        "output_path": "./reports/",
        "format": "md"
    },
    "schedule": {
        "daily_report_time": "09:00"
    }
}
```

3. Configure the repositories which your want to track their change by editing `subscriptions.json`
```json
[
    "ollama/ollama",
    "vllm-project/vllm"
]
```

4. Configure environment variable GITHUB_TOKEN to set your GitHub access token.
    ```sh
    export GITHUB_TOKEN='your_github_token'

5. Run the application:
    ```sh
    python src/cli.py
    ```


