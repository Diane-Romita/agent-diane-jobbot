# Agent Diane – JobBot

> *Simplifying complexity. Scaling possibility. Automating job search.*

Agent Diane is a Slack-integrated Python bot that automates job search tasks by pulling in relevant roles from job board RSS feeds (like LinkedIn), filtering based on your ideal criteria, and posting them directly into a Slack channel.

---

## 🚀 What It Does
- Pulls from RSS job feeds (LinkedIn, etc.)
- Filters job listings based on custom keywords
- Excludes unwanted terms like "Entry Level" or "Intern"
- Posts structured alerts directly into a Slack workspace

---

## 🛠 How to Use

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/agent-diane-jobbot.git
cd agent-diane-jobbot
```

### 2. Install dependencies
```bash
pip install feedparser requests
```

### 3. Set your Slack Webhook
Open `agent_diane_jobbot.py` and replace:
```python
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"
```
with your actual [Slack Incoming Webhook URL](https://api.slack.com/messaging/webhooks).

### 4. Run it
```bash
python agent_diane_jobbot.py
```

### 5. (Optional) Automate It
Set up a cron job, GitHub Actions workflow, or cloud function to run it daily.

---

## 🧠 Customization
You can modify:
- `RSS_FEEDS`: Add job boards or sources relevant to your industry
- `KEYWORDS`: Include titles, skills, tools, cloud products, etc.
- `EXCLUDE_KEYWORDS`: Filter out noise

---

## 🤖 Why Agent Diane?
Inspired by executive GTM strategist Diane Romita’s real-world job search automation workflow, this bot brings intelligent lead filtering into Slack — and helps you skip the spreadsheet.

Built for personal ops. Ready to scale.

---

## 📄 License
MIT – feel free to fork and adapt for your own Slack workspace.
