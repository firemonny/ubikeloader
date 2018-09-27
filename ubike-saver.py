import requests
import os.path
from datetime import datetime

subdiretory = "ubike_data"
try:
    os.mkdir(subdiretory)
except Exception:
    pass
ubike_data = requests.get("http://data.taipei/youbike")
timestamp = datetime.now().strftime("%Y%m%d%H%M00")
filename = "ubike_data_"+timestamp+".json"


with open(os.path.join(subdiretory,filename),"w") as output:
    output.write(ubike_data.text)
