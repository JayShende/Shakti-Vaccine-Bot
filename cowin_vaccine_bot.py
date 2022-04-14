import requests
import random
from datetime import datetime
date_today=datetime.today().strftime('%d-%m-%Y')

api_cowin=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=365&date={date_today}"
cowin=requests.get(url=api_cowin)
data_cowin=cowin.json()


center_len=len(data_cowin["centers"])

print(center_len)
center_o = 0

total_num_of_session =len(data_cowin["centers"][center_o]["sessions"])


def fun():
    session_len = len(data_cowin["centers"][center_no]["sessions"])
    print(session_len)
    for i in range(session_len):
        session_no=i
        #json_variables()
        name = data_cowin["centers"][center_no]["name"]
        address = data_cowin["centers"][center_no]["address"]
        ditrict = data_cowin["centers"][center_no]["district_name"]
        pincode = data_cowin["centers"][center_no]["pincode"]
        fee_type = data_cowin["centers"][center_no]["fee_type"]

        date = data_cowin["centers"][center_no]["sessions"][session_no]["date"]
        vaccine = data_cowin["centers"][center_no]["sessions"][session_no]["vaccine"]
        cap = data_cowin["centers"][center_no]["sessions"][session_no]["available_capacity"]
        dose1_cap = data_cowin["centers"][center_no]["sessions"][session_no]["available_capacity_dose1"]
        dose2_cap = data_cowin["centers"][center_no]["sessions"][session_no]["available_capacity_dose2"]

        min_age = data_cowin["centers"][center_no]["sessions"][session_no]["min_age_limit"]
        allow_all = data_cowin["centers"][center_no]["sessions"][session_no]["allow_all_age"]
        print(allow_all)

        flag_all = ""
        if (allow_all == True):
            flag_all = "All Ages"
        else:
            flag_all = "Age Restricted"
        msg_send = f"""
         Vaccine 💉 - {vaccine} 

        {name}

        Address - {address}
        Date - {date}
        Pincode - {pincode}
        Fee Type - {fee_type}
        Age Group - {min_age} ({flag_all}) 

        Available Capacity - {cap}
        1st Dose Slot - {dose1_cap}
        2nd Dose Slot - {dose2_cap}

        🔰   Made with ❤❤   🔰
        """
        chat_id=-1001649994169
        api_telegram = f"https://api.telegram.org/bot0-----3085267:xxxxxxxxxxxxxxx/sendMessage?chat_id={chat_id}&text={msg_send}"

        telegram = requests.get(url=api_telegram)
        print(msg_send)

import time

while (True):
    for i in range(1):
        num = random.randint(0, center_len)
        print(num)
        center_no = num
        fun()
    time.sleep(120)

