# Contributing

Thanks for improving Nettimer. This is a personal automation project, so changes should keep the repo safe to clone, easy to configure, and careful with private data.

## Local Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. Create local configuration:

   ```bash
   cp .env.example .env
   ```

4. Fill in `.env` with local credentials and Telegram settings.

## Development Notes

- Do not commit `.env`, logs, screenshots, HTML debug dumps, or generated files from `output/`.
- Keep dashboard selectors and sample data sanitized.
- Prefer small pull requests with one clear purpose.
- Add or update documentation when setup, scheduling, or environment variables change.
- For scheduler changes, keep Linux/WSL usage in mind and avoid hard-coded local paths.

## Smoke Checks

Before opening a pull request, run the checks that match your change:

```bash
python main.py --status
python main.py --mode normal --status
python main.py --mode ramadan --status
bash setup_cron_5min.sh
bash remove_cron_5min.sh
```

Only run `python main.py` when your `.env` points to an authorized NetTime account.

## Useful Follow-Up Work

- Add unit tests for time parsing and work-mode persistence.
- Validate required environment variables before launching Playwright.
- Handle Telegram API errors explicitly.
- Add sanitized screenshots for the Rainmeter widget setup.
