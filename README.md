# Passenger App
By using flask mysql nginx uWsgi

## Requirements

* [Docker]
* [Docker-compose]


## Run

Clone the repo

    $ git clone git@github.com:maradwan/Passenger-App.git
    $ docker-compose up -d


# Install pytest for testing
* pip install pytest

## Run Testing

    # To Test
    $ pytest -vv test.py



## Add new data 
	$ curl -v --request POST --url 'http://127.0.0.1/people' -H 'content-type: application/json' --data '{ "survived": false, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}'

## Uptdate data
	$ curl --request PUT --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' --data ' {"survived": true, "passengerClass": 1, "name": "Mr. Osama", "sex": "Male", "age": 25, "siblingsOrSpousesAboard": 110, "parentsOrChildrenAboard":11, "fare":19.25}'
 
## Get Spesfic Record
	$ curl --request GET --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' 

## Get all data 
	$ curl --request GET --url http://127.0.0.1/people --header 'Content-Type: application/json' 

## Delete data
	$ curl --request DELETE --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' 

## GUI 

     http://127.0.0.1
