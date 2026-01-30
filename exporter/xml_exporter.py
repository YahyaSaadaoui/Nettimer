import xml.etree.ElementTree as ET
from datetime import datetime

def export_to_xml(data, output_path="output/nettime.xml"):
    root = ET.Element("nettime")

    ET.SubElement(root, "timestamp").text = datetime.now().isoformat(timespec="seconds")

    daily = ET.SubElement(root, "daily")
    ET.SubElement(daily, "solde").text = data.get("daily_solde")

    monthly = ET.SubElement(root, "monthly")
    ET.SubElement(monthly, "solde").text = data.get("monthly_solde")
    ET.SubElement(monthly, "retard_cumule").text = data.get("monthly_delay")
    ET.SubElement(monthly, "jours_retard").text = data.get("delay_days")
    ET.SubElement(monthly, "moyenne_retard").text = data.get("avg_monthly_delay")

    misc = ET.SubElement(root, "stats")
    ET.SubElement(misc, "telework_days").text = data.get("telework_days")
    ET.SubElement(misc, "work_average_percent").text = data.get("work_avg_percent")

    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
