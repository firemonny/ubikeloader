import sys
import time
start_time = time.time()
import requests
import os.path
import json
from datetime import datetime
from sensorthingpy import *
from SensorthingSchema.SensorthingSchema import *
import config
import pytz
from multiprocessing import Pool

UBIKE_SERVER_URL = "http://data.taipei/youbike"
dir_path = os.path.dirname(os.path.realpath(__file__))


HISTORY_SENSORTHING_DATA_FILENAME =''
if config.PRODUCTION:
    HISTORY_SENSORTHING_DATA_FILENAME = dir_path + '/ubike_station_information.json'


# Post Observation to the existing datastream
historydata = None
writer = None

if config.PRODUCTION:
    print("Production Mode")
# convert from Taipei time format "YYYYmmddhhMMSS" to utc datetime object
def timeFormatTaipeiConverttoUTC(timetext):
    datetimeobject = datetime.strptime(timetext,'%Y%m%d%H%M%S')
    local_tz = pytz.timezone("Asia/Taipei")
    local_dt = local_tz.localize(datetimeobject, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt

def getThingIdFromData(data, stationID):
    for singledata in data:
        if(singledata['stationID'] == stationID):
            return singledata
    return None


def changeHistoryDataTime(data, stationID, time_text):
    for singledata in data:
        if(singledata['stationID'] == stationID):
            singledata['mday'] = time_text
            return


def loadData(station, historydata):
    station_id = station['sno']
    station_history_data = getThingIdFromData(
        historydata['Things_data'], station['sno'])
    currentDateTime_datetime_object = timeFormatTaipeiConverttoUTC(station["mday"])
    station_last_update_time = ""
    # handle the last update time for 0
    if(station_history_data['mday']==""):
        station_last_update_time = currentDateTime_datetime_object.isoformat()
    #check the data time
    else:
        station_last_update_time_datetime_object = timeFormatTaipeiConverttoUTC(station_history_data["mday"])
        dataValid = (station_last_update_time_datetime_object < currentDateTime_datetime_object)
        if(not dataValid):
            return
        else:
            station_last_update_time = station_last_update_time_datetime_object.isoformat()
    obserationDataset["phenomenonTime"] = station_last_update_time
    obserationDataset["result"] = station["sbi"]
    createObservation(obserationDataset,station_history_data["DatastreamId_ubikes"])
    obserationDataset["phenomenonTime"] = station_last_update_time
    obserationDataset["result"] = station["bemp"]
    createObservation(obserationDataset,station_history_data["DatastreamId_docks"])
    changeHistoryDataTime(historydata['Things_data'], station["sno"], station["mday"])

def main():
    if(os.path.isfile(HISTORY_SENSORTHING_DATA_FILENAME)):
        with open(HISTORY_SENSORTHING_DATA_FILENAME) as historydatafile:
            historydata = json.load(historydatafile)
    else:
        print('Please run the station_information_loader.py to get historysensorthingdata.json')
        exit()
    # p = Pool()
    ubike_data = requests.get(UBIKE_SERVER_URL)
    if( ubike_data.status_code == 200):
        payload = ubike_data.json()["retVal"]
        for i in range (1,406):
            key = "%04d" % i
            if(key in payload):
                ubikedata = payload[key]
                print("Posting station:%04d data." % i)
                loadData(ubikedata, historydata)
                # p.apply_async(loadData,
                #                args=(station, historydata))
            # p.close()
            # p.join()
    # else:
    #     print('outputfile is missing')
    #     exit()
    with open(HISTORY_SENSORTHING_DATA_FILENAME, 'w') as outputfile:
        json.dump(historydata, outputfile)
    #
    print("My program took", time.time() - start_time, "to run")


if __name__ == "__main__":
    main()
