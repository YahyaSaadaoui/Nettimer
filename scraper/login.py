from config.settings import NETTIME_URL

def login(page, username, password):
    page.goto(NETTIME_URL)

    page.fill("#input-user", username)
    page.fill("#input-password", password)
    page.click("#btn-submit")

    page.wait_for_selector("#form-login", state="detached", timeout=60000)

    page.wait_for_selector('div[menu-id="VistaResumen"] button', timeout=60000)
    page.click('div[menu-id="VistaResumen"] button')

    page.wait_for_selector("text=Solde", timeout=60000)
