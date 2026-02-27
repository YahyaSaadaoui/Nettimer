#!/bin/bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
MARKER="# NETTIMER_EVERY_5_MIN"
JOB="*/5 * * * * /bin/bash -lc 'cd \"$REPO_DIR\" && ./run_nettime.sh' $MARKER"

TMP_CRON="$(mktemp)"
trap 'rm -f "$TMP_CRON"' EXIT

crontab -l 2>/dev/null | grep -v "$MARKER" > "$TMP_CRON" || true
echo "$JOB" >> "$TMP_CRON"
crontab "$TMP_CRON"

echo "Installed NetTimer cron job:"
echo "$JOB"
echo "Data will be fetched every 5 minutes."
