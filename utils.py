from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
from time import sleep


# This function is for login activity
def login(driver, url, username, password):
    driver.get(url)
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "user_email"))
    ).send_keys(username)
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "user_password"))
    ).send_keys(password)
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "icheckbox"))
    ).click()
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.NAME, "commit"))
    ).click()
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "small"))
    ).click()


# This Fnction is for ScheduleAppointment activity
def navigate_to_schedule_appointment(driver):
    ScheduleAppointment = driver.find_element(By.CLASS_NAME, "accordion-title")
    ScheduleAppointment.click()
    sleep(2)
    ScheduleAppointment_Button = driver.find_element(
        By.CLASS_NAME, "small-only-expanded"
    )
    ScheduleAppointment_Button.click()
    sleep(3)


# This Fuction is for get the day of appoinment of the given range and covered all the usecase of the daterange
def interact_with_dropdown(driver, User_start_date, User_end_date, selected_options=[]):
    dropdown = Select(
        driver.find_element(By.ID, "appointments_consulate_appointment_facility_id")
    )

    location_found = False
    for selected_option in selected_options:
        if selected_option:
            dropdown.select_by_visible_text(selected_option.capitalize().strip())

            sleep(2)

            try:
                WebDriverWait(driver, 40).until(
                    EC.element_to_be_clickable(
                        (By.ID, "appointments_consulate_address")
                    )
                ).click()
                sleep(2)
                WebDriverWait(driver, 40).until(
                    EC.element_to_be_clickable(
                        (By.ID, "appointments_consulate_appointment_date")
                    )
                ).click()

                sleep(3)

                datepicker_title_div = driver.find_elements(
                    By.CLASS_NAME, "ui-datepicker-title"
                )

                # startdate
                startdate_month_element = datepicker_title_div[0].find_element(
                    By.CLASS_NAME, "ui-datepicker-month"
                )
                startdate_year_element = datepicker_title_div[0].find_element(
                    By.CLASS_NAME, "ui-datepicker-year"
                )

                startdate_month_text = startdate_month_element.text
                startdate_year_text = startdate_year_element.text

                full_startdate_calender = (
                    f"{startdate_month_text} {startdate_year_text}"
                )

                # enddate
                enddate_month_element = datepicker_title_div[1].find_element(
                    By.CLASS_NAME, "ui-datepicker-month"
                )
                enddate_year_element = datepicker_title_div[1].find_element(
                    By.CLASS_NAME, "ui-datepicker-year"
                )

                enddate_month_text = enddate_month_element.text
                enddate_year_text = enddate_year_element.text

                full_enddate_calender = f"{enddate_month_text} {enddate_year_text}"

                if (
                    User_start_date == full_startdate_calender
                    and User_end_date == full_enddate_calender
                ):
                    get_all_available_dates_first_calender = driver.find_elements(
                        By.CSS_SELECTOR,
                        "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr>td>a",
                    )
                    get_all_available_dates_last_calender = driver.find_elements(
                        By.CSS_SELECTOR,
                        "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr>td>a",
                    )

                    if get_all_available_dates_first_calender:
                        location_found = True

                        available_date = random.choice(
                            get_all_available_dates_first_calender
                        )
                        available_date.click()
                    elif get_all_available_dates_last_calender:
                        location_found = True

                        available_date = random.choice(
                            get_all_available_dates_last_calender
                        )
                        available_date.click()
                    else:
                        print(f"There is not date availabe within the give date")
                elif User_start_date == full_enddate_calender:
                    while (
                        User_end_date != full_startdate_calender
                        or User_end_date != full_enddate_calender
                    ):
                        try:
                            WebDriverWait(driver, 40).until(
                                EC.element_to_be_clickable(
                                    (By.CLASS_NAME, "ui-datepicker-next")
                                )
                            ).click()
                            sleep(3)

                            datepicker_title_div = driver.find_elements(
                                By.CLASS_NAME, "ui-datepicker-title"
                            )

                            # startdate
                            startdate_month_element = datepicker_title_div[
                                0
                            ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                            startdate_year_element = datepicker_title_div[
                                0
                            ].find_element(By.CLASS_NAME, "ui-datepicker-year")

                            startdate_month_text = startdate_month_element.text
                            startdate_year_text = startdate_year_element.text

                            full_startdate_calender = (
                                f"{startdate_month_text} {startdate_year_text}"
                            )

                            # enddate
                            enddate_month_element = datepicker_title_div[
                                1
                            ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                            enddate_year_element = datepicker_title_div[1].find_element(
                                By.CLASS_NAME, "ui-datepicker-year"
                            )

                            enddate_month_text = enddate_month_element.text
                            enddate_year_text = enddate_year_element.text

                            full_enddate_calender = (
                                f"{enddate_month_text} {enddate_year_text}"
                            )
                            if not full_enddate_calender:
                                break

                            get_all_available_dates_first_calender = driver.find_elements(
                                By.CSS_SELECTOR,
                                "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr>td>a",
                            )
                            get_all_available_dates_last_calender = driver.find_elements(
                                By.CSS_SELECTOR,
                                "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr>td>a",
                            )

                            if get_all_available_dates_first_calender:
                                location_found = True

                                available_date = random.choice(
                                    get_all_available_dates_first_calender
                                )
                                available_date.click()

                            elif get_all_available_dates_last_calender:
                                location_found = True

                                available_date = random.choice(
                                    get_all_available_dates_last_calender
                                )
                                available_date.click()

                            if (
                                User_end_date == full_startdate_calender
                                or User_end_date == full_enddate_calender
                            ):
                                print()
                                break
                        except Exception as e:
                            break
                else:
                    if (
                        User_start_date != full_startdate_calender
                        or User_start_date != full_enddate_calender
                    ):
                        while (
                            User_start_date != full_startdate_calender
                            or User_start_date != full_enddate_calender
                        ):
                            try:
                                WebDriverWait(driver, 40).until(
                                    EC.element_to_be_clickable(
                                        (By.CLASS_NAME, "ui-datepicker-next")
                                    )
                                ).click()
                                sleep(3)

                                datepicker_title_div = driver.find_elements(
                                    By.CLASS_NAME, "ui-datepicker-title"
                                )

                                # startdate
                                startdate_month_element = datepicker_title_div[
                                    0
                                ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                                startdate_year_element = datepicker_title_div[
                                    0
                                ].find_element(By.CLASS_NAME, "ui-datepicker-year")

                                startdate_month_text = startdate_month_element.text
                                startdate_year_text = startdate_year_element.text

                                full_startdate_calender = (
                                    f"{startdate_month_text} {startdate_year_text}"
                                )

                                # enddate
                                enddate_month_element = datepicker_title_div[
                                    1
                                ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                                enddate_year_element = datepicker_title_div[
                                    1
                                ].find_element(By.CLASS_NAME, "ui-datepicker-year")

                                enddate_month_text = enddate_month_element.text
                                enddate_year_text = enddate_year_element.text

                                full_enddate_calender = (
                                    f"{enddate_month_text} {enddate_year_text}"
                                )
                                if not full_enddate_calender:
                                    print("Error: End date not getting updated.")
                                    break

                                get_all_available_dates_first_calender = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr>td>a",
                                )
                                get_all_available_dates_last_calender = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr>td>a",
                                )
                                if get_all_available_dates_first_calender:
                                    location_found = True

                                    available_date = random.choice(
                                        get_all_available_dates_first_calender
                                    )
                                    available_date.click()
                                elif get_all_available_dates_last_calender:
                                    location_found = True

                                    available_date = random.choice(
                                        get_all_available_dates_last_calender
                                    )
                                    available_date.click()

                                if User_start_date == full_startdate_calender:
                                    get_all_available_dates_first_calender = driver.find_elements(
                                        By.CSS_SELECTOR,
                                        "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr>td>a",
                                    )
                                    if get_all_available_dates_first_calender:
                                        location_found = True

                                        available_date = random.choice(
                                            get_all_available_dates_first_calender
                                        )
                                        available_date.click()

                                elif User_start_date == full_enddate_calender:
                                    get_all_available_dates_last_calender = driver.find_elements(
                                        By.CSS_SELECTOR,
                                        "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr>td>a",
                                    )
                                    if get_all_available_dates_last_calender:
                                        location_found = True

                                        available_date = random.choice(
                                            get_all_available_dates_last_calender
                                        )
                                        available_date.click()

                                if (
                                    User_end_date == full_startdate_calender
                                    or User_end_date == full_enddate_calender
                                ):
                                    print()
                                    break
                            except Exception as e:
                                break
                    elif User_start_date == full_startdate_calender:
                        print("inside the loop")
                        while (
                            User_end_date != full_startdate_calender
                            or User_end_date != full_enddate_calender
                        ):
                            try:
                                datepicker_title_div = driver.find_elements(
                                    By.CLASS_NAME, "ui-datepicker-title"
                                )

                                # startdate
                                startdate_month_element = datepicker_title_div[
                                    0
                                ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                                startdate_year_element = datepicker_title_div[
                                    0
                                ].find_element(By.CLASS_NAME, "ui-datepicker-year")

                                startdate_month_text = startdate_month_element.text
                                startdate_year_text = startdate_year_element.text

                                full_startdate_calender = (
                                    f"{startdate_month_text} {startdate_year_text}"
                                )

                                # enddate
                                enddate_month_element = datepicker_title_div[
                                    1
                                ].find_element(By.CLASS_NAME, "ui-datepicker-month")
                                enddate_year_element = datepicker_title_div[
                                    1
                                ].find_element(By.CLASS_NAME, "ui-datepicker-year")

                                enddate_month_text = enddate_month_element.text
                                enddate_year_text = enddate_year_element.text

                                full_enddate_calender = (
                                    f"{enddate_month_text} {enddate_year_text}"
                                )
                                if not full_enddate_calender:
                                    print("Error: End date not getting updated.")
                                    break

                                get_all_available_dates_first_calender = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-first > table > tbody > tr>td>a",
                                )
                                get_all_available_dates_last_calender = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > table > tbody > tr>td>a",
                                )

                                if get_all_available_dates_first_calender:
                                    location_found = True

                                    available_date = random.choice(
                                        get_all_available_dates_first_calender
                                    )
                                    available_date.click()

                                elif get_all_available_dates_last_calender:
                                    location_found = True

                                    available_date = random.choice(
                                        get_all_available_dates_last_calender
                                    )
                                    available_date.click()

                                if (
                                    User_end_date == full_startdate_calender
                                    or User_end_date == full_enddate_calender
                                ):
                                    print()
                                    break

                                WebDriverWait(driver, 40).until(
                                    EC.element_to_be_clickable(
                                        (By.CLASS_NAME, "ui-datepicker-next")
                                    )
                                ).click()
                                sleep(2)
                            except Exception:
                                break
            except:
                print(
                    "There are no available appointments at the selected location. Please try again later."
                )

            if location_found:
                break

        else:
            selected_locations = [
                option.text.strip() for option in dropdown.options if option.text
            ]
            location_found = interact_with_dropdown(
                driver,
                User_start_date,
                User_end_date,
                selected_options=selected_locations,
            )

    return location_found


# This Function is for to get the time of the appointment
def get_time_appointment(driver):
    time_dropdown_element = driver.find_element(
        By.ID, "appointments_consulate_appointment_time"
    )
    time_dropdown_element.click()
    sleep(1)
    dropdown = Select(
        driver.find_element(By.ID, "appointments_consulate_appointment_time")
    )

    options = dropdown.options
    options = options[1:]

    random_option = random.choice(options)
    random_option.click()
    sleep(1)


# This function is for to submit the appointment
def appointments_submit(driver):
    # get the selected location
    dropdown = Select(
        driver.find_element(By.ID, "appointments_consulate_appointment_facility_id")
    )
    selected_location = dropdown.first_selected_option.text

    # get the selected date
    element_id = "appointments_consulate_appointment_date"
    selected_date = driver.execute_script(
        f'return document.getElementById("{element_id}").value'
    )

    # get the selected time
    time_dropdown = Select(
        driver.find_element(By.ID, "appointments_consulate_appointment_time")
    )
    selected_time = time_dropdown.first_selected_option.text
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.ID, "appointments_submit"))
    ).click()
    print(
        "Appoinment booked",
        "\n\n",
        f"Location: {selected_location}",
        "\n",
        f"Date: {selected_date}",
        "\n",
        f"Time: {selected_time}",
    )
    sleep(2)
