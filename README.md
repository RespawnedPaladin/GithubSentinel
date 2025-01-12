# GitHub Sentinel

GitHub Sentinel 是一款专为开发人员和项目经理设计的开源工具 AI Agent。它能定期（每天/每周）从订阅的 GitHub 资源库中自动检索和汇总更新。主要功能包括订阅管理、更新检索、通知系统和报告生成。

## 功能
- 订阅管理
- 更新检索
- 通知系统
- 报告生成

## 环境要求
- Python 3.10+
- GitHub access token

## 入门
1. 安装依赖:
    ```sh
    pip install -r requirements.txt
    ```

2. 通过编辑`config.json`来配置应用.
## 配置
`config.json`应当包含如下设置:
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

3. 通过编辑`subscriptions.json`来配置你期望跟踪变化的GitHub项目仓库

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


