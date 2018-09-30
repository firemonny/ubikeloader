import requests
import os.path
import json
import config
from datetime import datetime
from sensorthingpy import *
from SensorthingSchema.SensorthingSchema import *

UBIKE_SERVER_URL = "http://data.taipei/youbike"

STATION_INFORMATION = 'ubike_station_information.json'

HISTORY_SENSORTHING_DATA_FILENAME = ''
if config.PRODUCTION:
    HISTORY_SENSORTHING_DATA_FILENAME = 'ubike_station_information.json'

# Create ObservedProperty Entity
ObservedPropertyId_ubikes = getObservedPropertyId('Available_ubikes')
if(ObservedPropertyId_ubikes ==0 ):
        ObservedPropertyId_ubikes = createObservedProperty(observationPropertydataset_available_ubikes)
ObservedPropertyId_docks = getObservedPropertyId('Available_docks')
if(ObservedPropertyId_docks == 0):
        ObservedPropertyId_docks = createObservedProperty(observationPropertydataset_available_docks)

# Create Sensor Entity
Sensor_ubike_Id = getSensorId('Sensor of available ubikes')
if(Sensor_ubike_Id == 0):
        Sensor_ubike_Id = createSensor(sensor_available_ubike_Dataset)
Sensor_dock_Id = getSensorId('Sensor of available docks')
if(Sensor_dock_Id  == 0):
        Sensor_dock_Id  = createSensor(sensor_available_docks_Dataset)

# Create the sensorthingdata.json to track back the entity data
historydata = {}
historydata["Things_data"]=[]


ubike_data = requests.get("http://data.taipei/youbike")
payload = ubike_data.json()["retVal"]

for i in range (1,406):
    key = "%04d" % i
    if(key in payload):
        ubikedata = payload[key]
        ## Create thing entity
        thingDataset['name'] = ubikedata["sno"]+":"+ubikedata["snaen"]
        thingDataset['description'] = 'The ubike station with number of available ubikes and available docks'
        thingDataset['properties']['sno'] = ubikedata['sno']
        thingDataset['properties']['sna'] = ubikedata['sna']
        thingDataset['properties']['sarea'] = ubikedata['sarea']
        thingDataset['properties']['ar'] = ubikedata['ar']
        thingDataset['properties']['sareaen'] = ubikedata['sareaen']
        thingDataset['properties']['snaen'] = ubikedata['snaen']
        thingDataset['properties']['aren'] = ubikedata['aren']
        newThingId = createThings(thingDataset)
        ##Create location entity
        locationDataset['description'] = 'The geographic location of ubike station for the Taipei City on ' + ubikedata['snaen']
        locationDataset['name'] = ubikedata["sno"]+":"+ubikedata["snaen"]
        locationDataset['location']['coordinates'] = [ubikedata['lng'],ubikedata['lat']]
        locationDataset['Things'][0]['@iot.id'] = newThingId
        newLocationId = createLocation(locationDataset)

        ##Create datastream for ubike
        datastreamDataset_available_ubikes['name'] = ubikedata["sno"]+":"+ubikedata["snaen"] + '_ubikes'
        datastreamDataset_available_ubikes['description'] = 'The datastream of available ubikes for ' + ubikedata["snaen"]
        datastreamDataset_available_ubikes['Sensor']['@iot.id'] = Sensor_ubike_Id
        datastreamDataset_available_ubikes['ObservedProperty']['@iot.id'] = ObservedPropertyId_ubikes
        datastreamDataset_available_ubikes['Thing']['@iot.id'] = newThingId
        newDatastreamId_bikes = createDatastream(datastreamDataset_available_ubikes)

        ##Create datastream for docks
        datastreamDataset_available_docks['name'] = ubikedata["sno"]+":"+ubikedata["snaen"] + '_docks'
        datastreamDataset_available_docks['description'] = 'The datastream of available dock for ' + ubikedata["snaen"]
        datastreamDataset_available_docks['Sensor']['@iot.id'] = Sensor_dock_Id
        datastreamDataset_available_docks['ObservedProperty']['@iot.id'] = ObservedPropertyId_docks
        datastreamDataset_available_docks['Thing']['@iot.id'] = newThingId
        newDatastreamId_docks = createDatastream(datastreamDataset_available_docks)
        ## Save the entity data
        newthingData = {
                 "stationID": ubikedata["sno"],
                 "ThingID": newThingId,
                 "DatastreamId_ubikes": newDatastreamId_bikes,
                 "DatastreamId_docks": newDatastreamId_docks,
                 "mday": ""}
        historydata["Things_data"].append(newthingData)
    else:
        pass
with open(HISTORY_SENSORTHING_DATA_FILENAME,'w') as outputfile:
    json.dump(historydata,outputfile)
