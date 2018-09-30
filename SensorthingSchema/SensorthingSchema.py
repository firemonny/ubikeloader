# Dataset structure format declaration
obserationDataset = {
    'result': 0.0,
    'phenomenonTime':''
    }

observationPropertydataset_available_ubikes = {
   "name": "Available_ubikes",
   "definition": "Number of ubikes available for rental",
   "description": "http://goo.gl/pmcIo3"
}
observationPropertydataset_available_docks = {
   "name": "Available_docks",
   "definition": "Number of docks accepting ubike returns",
   "description": "http://goo.gl/pmcIo3"
}

sensor_available_ubike_Dataset = {
   "name": "Sensor of available ubikes",
   "description": "A sensor for track the number of available ubike",
   "encodingType": "text/html",
   "metadata": "http://goo.gl/pmcIo3"
}

sensor_available_docks_Dataset = {
   "name": "Sensor of available docks",
   "description": "A sensor for track the number of available docks",
   "encodingType": "text/html",
   "metadata": "http://goo.gl/pmcIo3"
}
thingDataset = {
    "description": "",
            "name": "",
            "properties": {
                "sno":"",
                "sna": "",
                "sarea": "",
                "ar": "",
                "sareaen":"",
                "snaen": "",
                "aren":""
            }
        }
locationDataset = {
           "description": "",
           "name": "",
           "encodingType": "application/vnd.geo+json",
           "location":
            {
             "type": "Point",
              "coordinates": None
                },
            "Things":[{
                "@iot.id": 0
            }]
                }
datastreamDataset_available_ubikes ={
    "name": "",
   "description": "",
   "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
   "unitOfMeasurement": {
      "name": "available",
      "symbol": "TOT",
      "definition": "The total number count for available ubikes"
   },
   "Sensor": {
      "@iot.id": 0
   },
   "ObservedProperty": {
      "@iot.id": 0
   },
   "Thing": {
      "@iot.id": 0
   }
}

datastreamDataset_available_docks ={
    "name": "",
   "description": "",
   "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
   "unitOfMeasurement": {
      "name": "available",
      "symbol": "TOT",
      "definition": "The total number count for available docks"
   },
   "Sensor": {
      "@iot.id": 0
   },
   "ObservedProperty": {
      "@iot.id": 0
   },
   "Thing": {
      "@iot.id": 0
   }
}
