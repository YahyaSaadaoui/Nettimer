#!/bin/bash
set -euo pipefail

MARKER="# NETTIMER_EVERY_5_MIN"
TMP_CRON="$(mktemp)"
trap 'rm -f "$TMP_CRON"' EXIT

crontab -l 2>/dev/null | grep -v "$MARKER" > "$TMP_CRON" || true
crontab "$TMP_CRON"

echo "Removed NetTimer 5-minute cron job (if it existed)."
