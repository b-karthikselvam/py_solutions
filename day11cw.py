import tripdata as m 
from datetime import datetime
import json
a = m.trip_details("Paris","04/01/2004","City of Light,")

time = datetime.strptime(a["date"],"%d/%m/%Y")
time2 = time.strftime("%B/%d/%Y")
a["date"] = time2
json_str = json.dumps(a)
print(json_str)




#tripdata.py

# def trip_details(place,dates,comment):
#     trip = {"city":place,
#             "date":dates,
#             "comment":comment}
#     return trip