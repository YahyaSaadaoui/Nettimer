def extract_nettime_data(page):
    page.wait_for_selector("#CWIN-INTERNAL", timeout=60000)

    def get_value(label):
        return page.locator(
            f'div.lay-cell:has(div.ib-name:has-text("{label}")) div.ib-value'
        ).first.inner_text().strip()

    return {
        "daily_solde": get_value("Solde journalier"),
        "monthly_solde": get_value("Solde mensuel")
    }
