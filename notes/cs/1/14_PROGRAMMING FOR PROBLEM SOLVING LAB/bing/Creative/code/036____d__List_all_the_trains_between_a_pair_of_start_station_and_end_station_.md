## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides various methods to query the train data using HTTP requests and JSON responses.
- To use the Indian Railways API, we need to register and obtain an API key, which is a unique identifier that allows us to access the data.
- One of the methods that the Indian Railways API provides is the Train Between Stations method, which takes the following parameters:
  - source: The code of the start station
  - dest: The code of the end station
  - date: The date of travel in DD-MM-YYYY format
  - class: The class of travel, such as 1A, 2A, 3A, SL, etc.
  - quota: The quota of travel, such as GN, CK, PQ, etc.
- The Train Between Stations method returns a JSON response that contains the following fields:
  - response_code: The status code of the request, such as 200 for success, 204 for no data, etc.
  - total: The total number of trains between the given stations
  - train: An array of objects, each representing a train, with the following fields:
    - number: The train number
    - name: The train name
    - from_station: An object with the following fields:
      - code: The code of the start station
      - name: The name of the start station
    - to_station: An object with the following fields:
      - code: The code of the end station
      - name: The name of the end station
    - classes: An array of objects, each representing a class, with the following fields:
      - code: The code of the class
      - name: The name of the class
      - available: A boolean value indicating whether the class is available or not
    - days: An array of objects, each representing a day, with the following fields:
      - code: The code of the day, such as MON, TUE, WED, etc.
      - runs: A boolean value indicating whether the train runs on that day or not
    - departure_time: The departure time of the train from the start station in HH:MM format
    - arrival_time: The arrival time of the train at the end station in HH:MM format
    - travel_time: The travel time of the train between the stations in HH:MM format
- To list all the trains between a pair of start station and end station, we need to construct a HTTP request with the appropriate parameters and send it to the Indian Railways API endpoint, which is https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<apikey>/From/<source>/To/<dest>/Date/<date>
- For example, to list all the trains between New Delhi (NDLS) and Mumbai Central (BCT) on 15-03-2023, we need to send the following request:

```
https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/xxxxxxxxxx/From/NDLS/To/BCT/Date/15-03-2023
```

- The response will be a JSON object that contains the list of trains, such as:

```
{
  "response_code": 200,
  "total": 5,
  "train": [
    {
      "number": "12951",
      "name": "MUMBAI RAJDHANI",
      "from_station": {
        "code": "NDLS",
        "name": "NEW DELHI"
      },
      "to_station": {
        "code": "BCT",
        "name": "MUMBAI CENTRAL"
      },
      "classes": [
        {
          "code": "1A",
          "name": "FIRST AC",
          "available": "Y"
        },
        {
          "code": "2A",
          "name": "SECOND AC",
          "available": "Y"
        },
        {
          "code": "3A",
          "name": "THIRD AC",
          "available": "Y"
        }
      ],
      "days": [
        {
          "code": "MON",
          "runs": "Y"
        },
        {
          "code": "TUE",
          "runs": "Y"
        },
        {
          "code": "WED",
          "runs": "Y"

```
