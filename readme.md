# Nettimer

Nettimer is a personal Python automation project for reading NetTime balance data from a web dashboard, estimating the end-of-day departure time, and sending a concise Telegram update. It also exports a JSON file that can be displayed in a Windows Rainmeter widget.

This repository is built for learning and personal workflow automation. Use it only with systems you are authorized to access and only in ways that follow the target system's terms.

## Features

- Headless browser automation with Playwright and Chromium.
- Environment-based configuration for credentials and Telegram settings.
- Extraction of daily and monthly NetTime balance values.
- Estimated departure time based on normal or Ramadan work targets.
- Telegram notifications for mobile updates.
- JSON export for a desktop widget.
- Optional cron scheduling for regular background refreshes.

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| Browser automation | Playwright |
| Configuration | python-dotenv |
| Notifications | Telegram Bot API, requests |
| Scheduling | cron on Linux/WSL |
| Desktop display | Rainmeter on Windows |

## Project Structure

```text
nettimer/
├── config/                # Runtime settings
├── core/                  # Browser setup, work modes, time calculation
├── exporter/              # JSON widget export
├── notifier/              # Telegram sender
├── output/                # Generated runtime files
├── scraper/               # Login and dashboard extraction
├── windows_widget/        # Rainmeter skin assets
├── main.py                # CLI entry point
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── run_nettime_example.sh # Example scheduled runner
├── setup_cron_5min.sh     # Installs the 5-minute cron job
└── remove_cron_5min.sh    # Removes the 5-minute cron job
```

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/YahyaSaadaoui/Nettimer.git
cd Nettimer
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and the Playwright browser runtime:

```bash
pip install -r requirements.txt
playwright install chromium
```

Create your local environment file:

```bash
cp .env.example .env
```

Fill in the values in `.env`:

```env
NETTIME_USERNAME=your_username
NETTIME_PASSWORD=your_password
NETTIME_URL=https://example.internal/nettime
TELEGRAM_BOT_TOKEN=123456:telegram-bot-token
TELEGRAM_CHAT_ID=123456789
```

Never commit `.env`, screenshots, logs, or generated output containing private data.

## Running

Run the scraper and send a Telegram update:

```bash
python main.py
```

Show the current persisted work mode without scraping:

```bash
python main.py --status
```

Switch the work mode:

```bash
python main.py --mode normal
python main.py --mode ramadan
```

The mode is persisted in `output/work_mode_state.json`. The normal target is `8:30`; the Ramadan target is `7:00`.

Each successful run writes widget data to:

```text
output/nettime_widget.json
```

## Scheduling

The repository includes a cron installer for Linux or WSL. It schedules Nettimer to refresh every 5 minutes:

```bash
bash setup_cron_5min.sh
```

Remove the scheduled job with:

```bash
bash remove_cron_5min.sh
```

By default, the cron job runs `run_nettime_example.sh`. If you need custom behavior, create a local `run_nettime.sh` file in the repository root. That file is ignored by Git, and the installer will use it when present.

## Windows Rainmeter Widget

The widget reads the generated JSON file and displays the latest NetTime values on the desktop.

1. Install Rainmeter from `https://www.rainmeter.net/`.
2. Copy `windows_widget/rainmeter/NetTime` into `%USERPROFILE%\Documents\Rainmeter\Skins\NetTime`.
3. Open `NetTime.ini` and update `DataPath` to the path of `output/nettime_widget.json` on your machine.
4. Load `NetTime.ini` from Rainmeter's Manage window.

The Rainmeter skin refreshes from the JSON file, so it updates after the next scheduled Nettimer run.

## Security Notes

- The project runs locally and stores secrets only in your local `.env` file.
- It uses normal browser automation against pages visible to the logged-in user.
- It does not bypass authentication, call private APIs, or upload scraped data to an external service except for the Telegram message you configure.
- Debug screenshots and HTML dumps can contain private data; keep `output/` local.

## Good First Improvements

- Add unit tests for `core/time_calc.py` and `core/work_mode.py`.
- Improve error handling around missing environment variables and Telegram failures.
- Add a Docker or devcontainer setup for repeatable local runs.
- Add sanitized screenshots of the Rainmeter widget and Telegram notification flow.

## License

This project is shared as a personal educational project. Check the repository license before reusing it in another project.
