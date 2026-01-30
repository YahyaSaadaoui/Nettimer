# NetTime Scraper & Telegram Notifier (Personal Project)

## Overview

This project is a **personal technical experiment** that combines:

* Web automation / scraping with Python
* Background task scheduling
* Data extraction & transformation
* Push notifications via a Telegram bot

The goal is to explore how to:

* Automate interaction with a web interface
* Extract structured information
* Process it locally
* Deliver concise notifications to a mobile device

This project is **not intended for production use** and is meant purely as a **learning and experimentation exercise**.

---

## Features

* Headless browser automation using **Playwright (Chromium)**
* Secure handling of credentials via environment variables
* Extraction of selected values from a dashboard-style interface
* Local transformation of data (daily / monthly balances)
* Telegram bot notifications
* Scheduled execution using `cron`
* Runs silently in the background

---

## Example Notification

```
⏱ Time Summary

📅 Daily balance : -4:21
📆 Monthly balance : 9:42

🏠 Estimated end time : 18:53
```

---

## Project Structure

```
nettimer/
├── core/               # Browser + time calculation logic
├── scraper/            # Login & data extraction
├── notifier/           # Telegram notification sender
├── exporter/           # (optional) data export logic
├── output/             # Generated output files
├── main.py             # Entry point
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── run_nettime_exemple.sh
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd nettimer
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## Configuration

### Environment variables

Create a `.env` file based on the example:

```bash
cp .env.example .env
```

Edit `.env` and fill in the required values:

```env
NETTIME_USERNAME=
NETTIME_PASSWORD=
NETTIME_URL=

TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

> Credentials are stored locally and never committed to the repository.

---

## Running the project

### Manual run

```bash
python main.py
```

If everything is configured correctly, a Telegram notification will be sent.

---

## Background execution (Linux)

The project can be scheduled using `cron` to run at specific times.

Example (Monday–Friday at 11:00, 15:00, 17:00):

```cron
0 11,15,17 * * 1-5 /path/to/run_nettime.sh
```

An example launcher script (`run_nettime_exemple.sh`) is provided.

---

## Security & Scope

This project is intentionally limited in scope:

* Runs **locally only**
* Uses standard browser automation
* Extracts **only data visible to the logged-in user**
* Does not bypass authentication
* Does not interact with private APIs
* Does not upload scraped data to third-party services

It is designed as a **personal learning project**, not a monitoring or surveillance tool.

---

## Why this project

This project was built to practice and demonstrate:

* Python automation
* Web scraping with modern tools
* Clean project structuring
* Background task scheduling
* Notification systems
* Secure handling of configuration and secrets

It serves as a sandbox for experimenting with **automation patterns commonly used in internal tools**.

---

## Disclaimer

This repository is provided for **educational and experimental purposes only**.
Any usage should comply with the terms of the target systems being accessed.

