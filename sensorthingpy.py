import requests
import json
import time
import config
from helpers import *

# Golbal variable declaraion
SERVER_URL_CLASS = config.STA_URL
#  Create Request
def createThings(payload):
    """
        Creat the things in the Sensorthing server
        parameter: Things payload structure.
    """
    SERVER_URL_CREATE_THING = SERVER_URL_CLASS + "Things"
    r = postToServer(SERVER_URL_CREATE_THING,payload)
    # r = requests.post(SERVER_URL_CREATE_THING,
    #                   data=json.dumps(payload), headers=headers, auth=AUTH)
    if(r.status_code == 201):
        createThingID = r.json()['@iot.id']
        print("Creating Things(%d) to the server" % (createThingID))
        return createThingID
    else:
        print("The POST Things request was fail")
        print(r.status_code)
        return -1


def createObservedProperty(payload):
    """
        Creat the observed property in the Sensorthing server
        parameter: observed property payload structure.
    """
    SERVER_URL_CREATE_OBSERVEDPROPERTY = SERVER_URL_CLASS + "ObservedProperties"
    r = postToServer(SERVER_URL_CREATE_OBSERVEDPROPERTY,payload)
    # r = requests.post(SERVER_URL_CREATE_OBSERVEDPROPERTY,
    #                   data=json.dumps(payload), headers=headers, auth=AUTH)
    if(r.status_code == 201):
        createObseredpropertiesID = r.json()['@iot.id']
        print("Creating ObservedProperty (%d) to the server" %
              (createObseredpropertiesID))
        return createObseredpropertiesID
    else:
        print("The POST Things request was fail")
        print(r.json())
        return -1


def createLocation(payload):
    """
        Creat the location property in the Sensorthing server
        parameter: Location payload structure.
    """
    SERVER_URL_CREATE_LOCATION = SERVER_URL_CLASS + "Locations"
    r = postToServer(SERVER_URL_CREATE_LOCATION,payload)
    # r = requests.post(SERVER_URL_CREATE_LOCATION,
    #                   data=json.dumps(payload), headers=headers, auth=AUTH)
    if(r.status_code == 201):

        createLocationID = r.json()['@iot.id']
        print("Creating Location(%d) to the server" % (createLocationID))
        return createLocationID
    else:
        print("The POST Location request was fail")
        return -1


def createSensor(payload):
    """
        Creat the Sensor in the Sensorthing server
        parameter: Sensor payload structure.
    """
    SERVER_URL_CREATE_SENSOR = SERVER_URL_CLASS + "Sensors"
    r = postToServer(SERVER_URL_CREATE_SENSOR,payload)
    # r = requests.post(SERVER_URL_CREATE_SENSOR,
    #                   data=json.dumps(payload), headers=headers, auth=(AUTH_INFO['Username'],AUTH_INFO['Password']))
    if(r.status_code == 201):
        createSensorID = r.json()['@iot.id']
        print("Creating Sensor(%d) to the server" % (createSensorID))
        return createSensorID
    else:
        print("The POST Sensor request was fail")
        return -1


def createDatastream(payload):
    """
        Creat the datastream in the Sensorthing server
        parameter: Datastream payload structure.
    """
    SERVER_URL_CREATE_DATASTREAMS = SERVER_URL_CLASS + "Datastreams"
    r = postToServer(SERVER_URL_CREATE_DATASTREAMS,payload)
    # r = requests.post(SERVER_URL_CREATE_DATASTREAMS,
    #                   data=json.dumps(payload), headers=headers, auth=(AUTH_INFO['Username'],AUTH_INFO['Password']))
    if(r.status_code == 201):
        createDataStreamID = r.json()['@iot.id']
        print("Creating Datastream(%d) to the server" % (createDataStreamID))
        return createDataStreamID
    else:
        print("The POST Datastream request was fail")
        return -1


def createObservation(payload, datastreamID):
    """
    Create obervation on Server.
    Parameter: result, Time (ISO6801 format) and datastreamID
    """
    SERVER_URL = (SERVER_URL_CLASS + "Datastreams(%s)/" + "Observations")
    r = postToServer(SERVER_URL % str(datastreamID),payload)
    print(r.json())

def checkTheThings():
    """
        Check if the thing was created before
    """
    SERVER_URL_THING = SERVER_URL_CLASS + "Things"
    r = requests.get(SERVER_URL_THING)
    if(r.status_code == 200):
        response = r.json()["value"]
        return response
    else:
        return None


def getDatastreamID(thingID):
    """
        Get the thing Id cosspond to the Datastream Id
    """
    SERVER_URL_GETDATASTREAM = (
        SERVER_URL_CLASS + "Things(%s)/" + "Datastreams" + "?$select=id,name") % str(thingID)
    r = requests.get(SERVER_URL_GETDATASTREAM)
    DatastreamsArray = []
    if(r.status_code == 200):
        Datastreams = r.json()['value']
        for Datastream in Datastreams:
            DatastreamId = Datastream['@iot.id']
            DatastreamName = Datastream['name']
            DatastreamData = {'id': DatastreamId, 'name': DatastreamName}
            DatastreamsArray.append(DatastreamData)
            # print(("Get the Datastream ID(%s) from the thing") % str(DatastreamID))
        return DatastreamsArray
    else:
        print("No Datastream Id found")
        return None

# TODO:   check the functionality

def getThingId(text):
    SERVER_URL_THING = SERVER_URL_CLASS + "Things"
    query = '$filter=name eq \'{query_text}\''.format(query_text=text)
    r = requests.get(SERVER_URL_THING, params=query)
    if(r.status_code == 200):
        if(r.json()['@iot.count'] != 0):
            ThingId = r.json()['value'][0]['@iot.id']
            return ThingId
        else:
            return 0
    else:
        print('something wrong')
        return -1


def getObservedPropertyId(text):
    SERVER_URL_THING = SERVER_URL_CLASS + "ObservedProperties"
    query = '$filter=name eq \'{query_text}\'&$select=id'.format(
        query_text=text)
    r = requests.get(SERVER_URL_THING, params=query)
    if(r.status_code == 200):
        if(r.json()['@iot.count'] != 0):
            ObservedPropertyId = r.json()['value'][0]['@iot.id']
            return ObservedPropertyId
        else:
            return 0
    else:
        print('something wrong')
        return -1


def getSensorId(text):
    SERVER_URL_THING = SERVER_URL_CLASS + "Sensors"
    query = '$filter=name eq \'{query_text}\'&$select=id'.format(
        query_text=text)
    r = requests.get(SERVER_URL_THING, params=query)
    if(r.status_code == 200):
        if(r.json()['@iot.count'] != 0):
            SensorId = r.json()['value'][0]['@iot.id']
            return SensorId
        else:
            return 0
    else:
        print('something wrong')
        return -1


def checkObservationExist(id, text):
    query = '$filter=phenomenonTime eq \'{time_text}\''.format(time_text=text)
    SERVER_URL_OBSERVATION = SERVER_URL_CLASS + \
        'Datastreams(%s)/Observations' % str(id)
    print(SERVER_URL_OBSERVATION + '?' + query)
    r = requests.get(SERVER_URL_OBSERVATION, params=query)
    if(r.status_code == 200):
        if(r.json()['@iot.count'] != 0):
            return 1
        else:
            return 0
    else:
        print('something wrong')
        return -1
