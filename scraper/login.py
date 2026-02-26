from config.settings import NETTIME_URL
import time
import os
from pathlib import Path


def _dump_debug(page, prefix="login_fail"):
    out_dir = Path(__file__).resolve().parents[1] / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = int(time.time())
    screenshot = out_dir / f"{prefix}_{ts}.png"
    html = out_dir / f"{prefix}_{ts}.html"
    try:
        page.screenshot(path=str(screenshot), full_page=True)
    except Exception:
        # ignore screenshot errors
        pass
    try:
        content = page.content()
        html.write_text(content, encoding="utf-8")
    except Exception:
        pass
    return screenshot, html


def login(page, username, password):
    """Perform login and wait for the app dashboard to be ready.

    This function is more defensive than before: it waits for load state,
    checks if the login form is still present (which likely means bad creds),
    and on failure saves a screenshot + HTML into `output/` for debugging.
    """
    page.goto(NETTIME_URL)

    page.fill("#input-user", username)
    page.fill("#input-password", password)
    page.click("#btn-submit")

    # Wait for either the login form to be removed (success) or for navigation/network to settle
    try:
        page.wait_for_selector("#form-login", state="detached", timeout=80000)
    except Exception:
        # not necessarily fatal; try to wait for load state to ensure page processed the request
        try:
            page.wait_for_load_state("networkidle", timeout=80000)
        except Exception:
            pass

    # If the login form is still present after attempts, treat as possible failed login
    try:
        still_present = page.query_selector("#form-login")
        if still_present:
            shot, html = _dump_debug(page, "login_still_present")
            raise RuntimeError(f"Login form still present after submit. Saved debug files: {shot}, {html}")
    except Exception:
        # query_selector may throw in some contexts; ignore and continue to try locating dashboard
        pass

    # Try multiple ways to detect the dashboard/menu. Be tolerant to small variations.
    menu_selectors = [
        'div[menu-id="VistaResumen"] button',
        'div[menu-id=VistaResumen] button',
        'button:has-text("VistaResumen")',
        'text=Solde',
    ]

    found = False
    last_error = None
    for sel in menu_selectors:
        try:
            # wait a bit for each selector; total time remains reasonable
            page.wait_for_selector(sel, timeout=20000)
            found = True
            # If the selector is a button/menu, try clicking it when appropriate
            if "button" in sel or sel.startswith("div"):
                try:
                    page.click(sel)
                except Exception:
                    # ignore click failures; presence is the main signal
                    pass
            break
        except Exception as exc:
            last_error = exc
            continue

    if not found:
        shot, html = _dump_debug(page, "login_timeout")
        # re-raise with helpful context
        raise RuntimeError(
            f"Unable to find the dashboard/menu after login. Tried selectors: {menu_selectors}."
            f" Saved debug files: {shot}, {html}. Last error: {last_error}"
        )

    # Finally, wait for a dashboard-specific text to ensure the app is ready
    try:
        page.wait_for_selector("text=Solde", timeout=20000)
    except Exception:
        # not fatal; dashboard might use different wording
        pass
