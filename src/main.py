import time
from pprint import pprint
from args import Arguments
from helpers import Messages, get_date, get_vaccine_details, vaccine_message
from api import get_calendar_by_district, get_calendar_by_pincode, make_call, send_message


def main():
    arguements = Arguments()
    district_id, pincode, telegram, dose = arguements.get_arguments()
    date = get_date()
    calendar = None
    if district_id is not None:
        calendar = get_calendar_by_district(district_id, date)
    elif pincode is not None:
        calendar = get_calendar_by_pincode(pincode, date)

    if not calendar:
        print("[Error] Calendar not found!")
        return Messages.ERROR.value

    print("Checking for vaccine...")
    vaccine_details = get_vaccine_details(calendar, dose)
    if len(vaccine_details) > 0:
        print("Vaccine details:\n")
        pprint(vaccine_details)

        print(f"\n\nVaccine Available! Calling {telegram}...")
        send_message(telegram, text=vaccine_message(vaccine_details))
        call_success = make_call(telegram, text="Vaccine available")
        if call_success:
            return Messages.VACCINE_AVAILABLE.value
        else:
            print("Failed to call!")
    else:
        print("No vaccines available at the moment.")

    return Messages.VACCINE_NOT_AVAILABLE.value


if __name__ == '__main__':
    print("\n\nTo receive calls, visit https://api2.callmebot.com/txt/login.php and authenticate using telegram.\n\n")
    while(True):
        ret = main()
        if ret == Messages.VACCINE_AVAILABLE.value:
            print("Checking again in 300 seconds...")
            time.sleep(300)
            continue
        print("Checking again in 30 seconds...")
        time.sleep(30)