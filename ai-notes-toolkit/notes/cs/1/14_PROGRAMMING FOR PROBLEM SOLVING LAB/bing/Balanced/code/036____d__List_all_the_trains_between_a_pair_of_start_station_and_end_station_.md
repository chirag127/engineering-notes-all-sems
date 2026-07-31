## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides various methods to query the train data using HTTP requests and JSON responses.
- To use the Indian Railways API, we need to register and obtain an API key from https://indianrailapi.com/.
- One of the methods that the Indian Railways API provides is the Train Between Stations method, which takes the following parameters:

  - apikey: The API key obtained from the registration.
  - from: The code of the start station.
  - to: The code of the end station.
  - date: The date of travel in DD-MM-YYYY format.

- The Train Between Stations method returns a JSON response that contains an array of trains that match the given parameters, along with their details such as train number, name, departure time, arrival time, travel time, days of operation, classes, and availability.
- To list all the trains between a pair of start station and end station, we need to parse the JSON response and display the relevant information in a tabular format.
- For example, if we want to list all the trains between New Delhi (NDLS) and Mumbai Central (BCT) on 15-03-2023, we can use the following HTTP request:

  - https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<apikey>/From/NDLS/To/BCT/Date/15-03-2023

- The JSON response will look something like this:

  ```json
  {
    "Trains": [
      {
        "TrainNo": "02951",
        "TrainName": "MUMBAI RAJDHANI",
        "TrainType": "RAJDHANI",
        "From": "NDLS",
        "To": "BCT",
        "DepartureTime": "16:25",
        "ArrivalTime": "08:15",
        "TravelTime": "15:50",
        "Days": "SUN,MON,TUE,WED,THU,FRI,SAT",
        "Classes": "1A,2A,3A",
        "Availability": [
          {
            "ClassCode": "1A",
            "ClassName": "FIRST AC",
            "Availability": "AVAILABLE-0001"
          },
          {
            "ClassCode": "2A",
            "ClassName": "SECOND AC",
            "Availability": "AVAILABLE-0010"
          },
          {
            "ClassCode": "3A",
            "ClassName": "THIRD AC",
            "Availability": "AVAILABLE-0020"
          }
        ]
      },
      {
        "TrainNo": "02925",
        "TrainName": "PASCHIM EXPRESS",
        "TrainType": "SUPERFAST",
        "From": "NDLS",
        "To": "BCT",
        "DepartureTime": "11:05",
        "ArrivalTime": "10:45",
        "TravelTime": "23:40",
        "Days": "SUN,MON,TUE,WED,THU,FRI,SAT",
        "Classes": "1A,2A,3A,SL",
        "Availability": [
          {
            "ClassCode": "1A",
            "ClassName": "FIRST AC",
            "Availability": "AVAILABLE-0002"
          },
          {
            "ClassCode": "2A",
            "ClassName": "SECOND AC",
            "Availability": "AVAILABLE-0005"
          },
          {
            "ClassCode": "3A",
            "ClassName": "THIRD AC",
            "Availability": "AVAILABLE-0015"
          },
          {
            "ClassCode": "SL",
            "ClassName": "SLEEPER CLASS",
            "Availability": "AVAILABLE-0030"
          }
        ]
      },
      // more trains ...
    ]
  }
  ```

- To display the information in a tabular format, we can use the following markdown syntax:

  | Train No | Train Name | Departure Time | Arrival Time | Travel Time | Days | Classes | Availability |
  | -------- | ---------- | -------------- | ------------ | ----------- | ---- | ------- | ------------ |
  | 02951 | MUMBAI RAJDHANI | 16:25 | 08:15 | 15:50 | SUN,MON,TUE,WED,THU,FRI,SAT | 1A,2A,3A |