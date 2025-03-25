# agent_diane_jobbot.py

"""
Agent Diane – Job Search Bot
A Python-based Slack-integrated agent that fetches job listings, filters them by predefined criteria,
and posts relevant opportunities into a Slack channel.
"""

import feedparser
import requests

# === CONFIGURATION ===
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
RSS_FEEDS = [
    "https://www.linkedin.com/jobs-guest/jobs/rss/?keywords=VP%20Salesforce",
    "https://www.linkedin.com/jobs-guest/jobs/rss/?keywords=Revenue%20Operations",
    # Add more feeds as needed
]

KEYWORDS = [
    "Salesforce", "Data Cloud", "Revenue Ops", "Chief of Staff", "GTM",
    "VP", "Digital Transformation", "Slack Automation"
]

EXCLUDE_KEYWORDS = ["Entry Level", "Intern"]


# === CORE FUNCTION ===
def fetch_and_filter_jobs():
    matches = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title.lower()
            summary = entry.summary.lower()
            if any(k.lower() in title + summary for k in KEYWORDS) and not any(
                e.lower() in title + summary for e in EXCLUDE_KEYWORDS):
                matches.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.summary,
                    "published": entry.published
                })
    return matches


def post_to_slack(job):
    message = {
        "text": f"📌 *New Role for Agent Diane*\n*{job['title']}*\n<{job['link']}|View job listing>\n_{job['published']}_"
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    return response.status_code == 200


# === RUN ===
if __name__ == "__main__":
    jobs = fetch_and_filter_jobs()
    for job in jobs:
        success = post_to_slack(job)
        print(f"Posted: {job['title']} – {'✅' if success else '❌'}")

    # TEMP: Force a test post to confirm Slack works
    test_job = {
        "title": "🚨 Test Alert: VP of Strategy at DreamCo",
        "link": "https://example.com/job",
        "summary": "Test post for debugging Slack webhook",
        "published": "Now"
    }
    post_to_slack(test_job)
