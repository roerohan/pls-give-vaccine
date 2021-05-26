from datetime import datetime
from enum import Enum

def get_date(): return datetime.now().strftime("%d-%m-%Y")


def get_vaccine_details(calendar, dose_number):
    centers = calendar["centers"]

    available_slots = []
    for center in centers:
        details = {
            "hospital_name": center["name"],
            "hospital_address": center["address"],
            "fee_type": center["fee_type"],
            "sessions": [],
        }

        for session in center["sessions"]:
            slot_count = session[f"available_capacity_dose{dose_number}"]
            if slot_count > 0:
                details["sessions"].append({
                    "slot_count": slot_count,
                    "slot_date": session["date"],
                    "age_limit": session["min_age_limit"],
                    "vaccine": session["vaccine"]
                })

        if len(details["sessions"]):
            available_slots.append(details)

    return available_slots


def vaccine_message(vaccine_details):
    REGISTRATION_URL = "https://selfregistration.cowin.gov.in"
    text = "<b>Vaccines Available!</b>\n"
    for detail in vaccine_details:
        text += "\n"
        text += f'Hospital: <b>{detail["hospital_name"]}</b>\n'
        text += f'Address: {detail["hospital_address"]}\n'
        text += f'Fee Type: {detail["fee_type"]}\n'

        for i, session in enumerate(detail["sessions"]):
            spaces = " " * (len(str(i+1)) + 4)
            text += "\n"
            text += f'{i + 1}. Vaccine: <b>{session["vaccine"]}</b>\n'
            text += f'{spaces}Date: <i>{session["slot_date"]}</i>\n'
            text += f'{spaces}Age Limit: <i>{session["age_limit"]}</i>\n'
            text += f'{spaces}Slot Count: <b>{session["slot_count"]}</b>\n'

    text += "\n"
    text += f"Registration URL: {REGISTRATION_URL} "
    return text


class Messages(Enum):
    ERROR = -1
    VACCINE_AVAILABLE = 1
    VACCINE_NOT_AVAILABLE = 0
