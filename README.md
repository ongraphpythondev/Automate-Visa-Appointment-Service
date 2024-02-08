# Automate Visa Appointment Service 
In the Auto_appointment_booking_bot, I have implemented the method that schedules appointments for US flights occurring earlier date within the provided date range...
### Setup environment
```
python3.11 -m venv venv
```
## Activate the environment

```
source venv/bin/activate

```
## Install requirements
```
pip install -r requirements.txt

```
## Run the Auto_appointment_booking_bot.py file

### For a single location/city
```
python3 Auto_appointment_booking_bot.py "start date" "end date" "location/city"


Example: python3 custom.py "December 2023" "March 2024" "Calgary"
```



### For multiple cities/locations
```
python3 Auto_appointment_booking_bot.py "start date" "end date" "city1" "city2" ....etc.


Example: python3 custom.py "December 2023" "March 2024" "Calgary" "Halifax"
```


### If you do not specify a city/location
```
python3 Auto_appointment_booking_bot.py "start date" "end date" ""


Example: python3 custom.py "December 2023" "March 2024" ""
```


