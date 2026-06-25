# Gmail Summarizer

A tool that connects to multiple Gmail accounts, fetches today's emails, and
(eventually) lets you ask a chatbot questions about your inbox using an LLM.

## ⚠️ Before every commit — safety habit, read this

This repo is **public**. `credentials.json` and `token.json` contain real
OAuth credentials and must NEVER be pushed to GitHub.

**Every single time, before running `git commit`:**
```
git status
```
Read the output. If `credentials.json` or `token.json` appear anywhere in
that list (as tracked, staged, or untracked-but-about-to-be-added), STOP —
do not commit — fix `.gitignore` first.

This matters even more here because the repo is public: anyone could see a
leaked credential immediately, not just you.

## Setup (for future reference / if you reclone this)

1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Get your own `credentials.json` from Google Cloud Console (Gmail API, OAuth
   Desktop app credentials) — this file is intentionally not included in this
   repo, since it's personal and sensitive.
4. (Install steps and run instructions will be added here as the project develops.)

## Project status

- [x] Google Cloud project + OAuth credentials set up
- [x] Local repo connected to GitHub
- [ ] Fetch today's emails from one Gmail account
- [ ] Support multiple Gmail accounts
- [ ] Basic chatbot using an LLM API
- [ ] Connect chatbot to email data (answer questions about inbox)
