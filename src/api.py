import requests


def url(route): return "https://cdn-api.co-vin.in/api/v2" + route


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}


def get_districts(state_id):
    try:
        return requests.get(url(f"/admin/location/districts/{state_id}"), headers=headers).json()
    except Exception as e:
        print("[Error] Failed to get districts")
        print(f"State ID: {state_id}")
        print(e)


def get_calendar_by_district(district_id, date):
    try:
        return requests.get(url(f"/appointment/sessions/calendarByDistrict?district_id={district_id}&date={date}"), headers=headers).json()
    except Exception as e:
        print("[Error] Failed to get calendar by district")
        print(f"District ID: {district_id}")
        print(f"Date: {date}")
        print(e)


def get_calendar_by_pincode(pincode, date):
    try:
        return requests.get(url(f"/appointment/sessions/calendarByPin?pincode={pincode}&date={date}"), headers=headers).json()
    except Exception as e:
        print("[Error] Failed to get calendar by pincode")
        print(f"Pincode: {pincode}")
        print(f"Date: {date}")
        print(e)


def make_call(telegram_username, text):
    CALL_URL = f"http://api.callmebot.com/start.php?source=auth&user=@{telegram_username}&text={text}&lang=en-US-Standard-B"
    r = requests.get(CALL_URL)
    return "ERROR" not in r.text


def send_message(telegram_username, text):
    TEXT_URL = f"https://api.callmebot.com/text.php?user={telegram_username}&text={text}&links=yes&html=yes"
    r = requests.get(TEXT_URL)
    return "ERROR" not in r.text