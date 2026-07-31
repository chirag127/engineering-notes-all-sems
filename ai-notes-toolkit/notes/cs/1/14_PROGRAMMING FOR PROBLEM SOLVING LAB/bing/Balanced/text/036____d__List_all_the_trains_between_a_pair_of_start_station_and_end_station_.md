## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides various methods to query the train data using HTTP requests and JSON responses.
- To use the Indian Railways API, we need to register and obtain an API key, which is a unique identifier that allows us to access the data.
- One of the methods that the Indian Railways API provides is the Train Between Stations method, which takes two parameters: source and destination station codes.
- The station codes are four-letter codes that represent the railway stations in India. For example, the station code for New Delhi is NDLS and the station code for Mumbai Central is BCT.
- The Train Between Stations method returns a list of trains that run between the given source and destination stations, along with their train numbers, names, departure and arrival times, travel time, days of operation, and classes of seats available.
- To use the Train Between Stations method, we need to construct a URL that contains the API key, the source station code, and the destination station code, and send a GET request to the URL.
- For example, to list all the trains between New Delhi and Mumbai Central, we can use the following URL:

`https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<API_KEY>/From/<SOURCE_STATION_CODE>/To/<DESTINATION_STATION_CODE>/`

- Replacing the placeholders with the actual values, we get:

`https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/123456789/From/NDLS/To/BCT/`

- Sending a GET request to this URL will return a JSON response that contains a list of trains, such as:

```json
{
  "ResponseCode": 200,
  "Message": "Success",
  "Trains": [
    {
      "TrainNo": "02951",
      "TrainName": "MUMBAI RAJDHANI",
      "TrainType": "RAJDHANI",
      "Source": "NDLS",
      "DepartureTime": "16:25",
      "Destination": "BCT",
      "ArrivalTime": "08:15",
      "TravelTime": "15:50",
      "Distance": "1384",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": [
        {
          "ClassCode": "1A",
          "Availability": "Y"
        },
        {
          "ClassCode": "2A",
          "Availability": "Y"
        },
        {
          "ClassCode": "3A",
          "Availability": "Y"
        }
      ]
    },
    {
      "TrainNo": "02953",
      "TrainName": "AUG KR RAJ EXP",
      "TrainType": "RAJDHANI",
      "Source": "NDLS",
      "DepartureTime": "17:15",
      "Destination": "BCT",
      "ArrivalTime": "09:45",
      "TravelTime": "16:30",
      "Distance": "1384",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": [
        {
          "ClassCode": "1A",
          "Availability": "Y"
        },
        {
          "ClassCode": "2A",
          "Availability": "Y"
        },
        {
          "ClassCode": "3A",
          "Availability": "Y"
        }
      ]
    },
    ...
  ]
}
```

- To display the list of trains in a tabular format, we can use the markdown syntax for tables, such as:

| Train No | Train Name | Departure Time | Arrival Time | Travel Time | Days |
| -------- | ---------- | -------------- | ------------ | ----------- | ---- |
| 02951 | MUMBAI RAJDHANI | 16:25 | 08:15 | 15:50 | SUN, MON, TUE, WED, THU, FRI, SAT |
| 02953 | AUG KR RAJ EXP | 17:15 | 09:45 | 16:30 | SUN, MON, TUE, WED, THU, FRI, SAT |
| ... | ... | ... | ... | ... | ... |

- This is one possible way to list all the trains between a pair of