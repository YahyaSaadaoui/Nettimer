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

The run also writes widget data into:

```text
output/nettime_widget.json
```

### Work mode (normal / ramadan)

The project supports two persistent work modes:

* `normal` = target `8:30`
* `ramadan` = target `7:00`

Switch mode (and persist choice):

```bash
python main.py --mode ramadan
python main.py --mode normal
```

Check current mode without scraping:

```bash
python main.py --status
```

Set mode without scraping:

```bash
python main.py --mode ramadan --status
python main.py --mode normal --status
```

Once `ramadan` is activated, it stays active for next runs until you cancel it with `--mode normal`.

---

## Windows desktop widget (Rainmeter)

You can pin NetTime values on your Windows desktop with Rainmeter.

### 1. Install Rainmeter (Windows)

Download and install Rainmeter from:

```text
https://www.rainmeter.net/
```

### 2. Copy the skin files

From this repository, copy:

```text
windows_widget/rainmeter/NetTime
```

to:

```text
%USERPROFILE%\Documents\Rainmeter\Skins\NetTime
```

Or run the installer script from Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File "\\wsl.localhost\Ubuntu-24.04\home\username\nettimer\windows_widget\install_rainmeter_skin.ps1"
```

### 3. Check the data path

Open `NetTime.ini` and verify this variable:

```ini
DataPath=\\wsl.localhost\Ubuntu-24.04\home\username\nettimer\output\nettime_widget.json
```

If your Linux username, distro name, or project path differs, update it.

### 4. Load the widget

In Rainmeter:

1. Open **Manage**.
2. Select `NetTime`.
3. Load `NetTime.ini`.
4. Right-click the widget and enable **Draggable** to place it.
5. Disable **Draggable** and enable **Click through** if you want it to stay fixed.

---

## Background execution (Linux)

The project can be scheduled using `cron` to run at specific times.

Example (Monday–Friday at 11:00, 15:00, 17:00):

```cron
0 11,15,17 * * 1-5 /path/to/run_nettime.sh
```

An example launcher script (`run_nettime_exemple.sh`) is provided.

### Fetch every 5 minutes

Install a 5-minute cron job with:

```bash
./setup_cron_5min.sh
```

Remove it with:

```bash
./remove_cron_5min.sh
```

The Rainmeter widget is configured to re-read JSON data every 30 seconds, so updates appear quickly after each fetch.

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

