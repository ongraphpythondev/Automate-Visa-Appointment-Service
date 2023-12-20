from selenium import webdriver
import random
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import argparse
from utils import *
from config import Username, Password


# This is the main function
def main(startdate, enddate, Location):
    username = Username.strip()
    password = Password.strip()

    User_start_date = startdate.capitalize().strip()
    User_end_date = enddate.capitalize().strip()
    location = Location

    # check Validation
    start_date_object = datetime.strptime(User_start_date, "%B %Y")
    end_date_object = datetime.strptime(User_end_date, "%B %Y")
    if end_date_object > start_date_object:
        print("Validation successful: End date is greater than start date.")
    else:
        raise ValueError("Validation failed: End date is less than start date.")

    url = "https://ais.usvisa-info.com/en-ca/niv/users/sign_in"
    PROXIES = [
        "http://92.222.153.172:3128/",
        "http://5.135.204.121:3128/",
        "http://180.254.239.207:8080/",
    ]

    random_proxy = random.choice(PROXIES)
    chrome_options = Options()
    # chrome_options.add_argument(f'--proxy-server={random_proxy}')

    # this driver is define for linux  if it don't work in the windows so uncomment the below code

    # chromedriver_path = 'path/to/chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=chromedriver_path)

    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()

    login(driver, url, username, password)
    sleep(2)
    navigate_to_schedule_appointment(driver)
    location_available = interact_with_dropdown(
        driver, User_start_date, User_end_date, selected_options=location
    )

    if location_available:
        get_time_appointment(driver)
        appointments_submit(driver)
        sleep(1)
        driver.quit()
    else:
        print("Date is not available of the given date range!!!")
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process startdate and enddate.")
    parser.add_argument(
        "startdate", help="Start date in string(full name of month) format"
    )
    parser.add_argument("enddate", help="End date in Year(2023) format")
    parser.add_argument("location", nargs="+", help="Pass the location in a string")

    args = parser.parse_args()
    try:
        main(args.startdate, args.enddate, args.location)
    except ValueError as e:
        print(e)
