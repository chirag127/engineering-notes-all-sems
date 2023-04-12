## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides access to various data related to the Indian Railways network, such as train status, seat availability, fare enquiry, etc.
- To use the Indian Railways API, we need to register and obtain an API key, which is a unique identifier that allows us to make requests to the API.
- The API key can be obtained from https://indianrailapi.com/api-registration.
- Once we have the API key, we can use the Train Between Stations API, which returns the list of trains running between two given stations on a given date.
- The Train Between Stations API has the following parameters:

  - apikey: The API key obtained from the registration.
  - from: The station code of the start station.
  - to: The station code of the end station.
  - date: The date of travel in DD-MM-YYYY format.

- The Train Between Stations API returns a JSON response, which is a data format that can be easily parsed and manipulated by various programming languages.
- The JSON response contains an array of train objects, each of which has the following attributes:

  - TrainNo: The train number.
  - TrainName: The train name.
  - TrainType: The train type, such as Express, Superfast, Rajdhani, etc.
  - From: The station code of the start station.
  - To: The station code of the end station.
  - DepartureTime: The departure time from the start station in HH:MM format.
  - ArrivalTime: The arrival time at the end station in HH:MM format.
  - TravelTime: The total travel time in HH:MM format.
  - Availability: The seat availability status for different classes, such as 1A, 2A, 3A, SL, etc.

- For example, if we want to list all the trains between New Delhi (NDLS) and Mumbai Central (BCT) on 15-03-2023, we can use the following URL:

  - https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<apikey>/From/NDLS/To/BCT/Date/15-03-2023

- The JSON response for this URL would look something like this:

```json
{
  "ResponseCode": 200,
  "Message": "Success",
  "Trains": [
    {
      "TrainNo": "12951",
      "TrainName": "MUMBAI RAJDHANI",
      "TrainType": "RAJDHANI",
      "From": "NDLS",
      "To": "BCT",
      "DepartureTime": "16:25",
      "ArrivalTime": "08:15",
      "TravelTime": "15:50",
      "Availability": [
        {
          "ClassCode": "1A",
          "ClassName": "FIRST AC",
          "Availability": "AVAILABLE-0006"
        },
        {
          "ClassCode": "2A",
          "ClassName": "SECOND AC",
          "Availability": "AVAILABLE-0010"
        },
        {
          "ClassCode": "3A",
          "ClassName": "THIRD AC",
          "Availability": "AVAILABLE-0012"
        }
      ]
    },
    {
      "TrainNo": "12953",
      "TrainName": "AG KRANTI RJDHN",
      "TrainType": "RAJDHANI",
      "From": "NDLS",
      "To": "BCT",
      "DepartureTime": "16:50",
      "ArrivalTime": "09:45",
      "TravelTime": "16:55",
      "Availability": [
        {
          "ClassCode": "1A",
          "ClassName": "FIRST AC",
          "Availability": "AVAILABLE-0004"
        },
        {
          "ClassCode": "2A",
          "ClassName": "SECOND AC",
          "Availability": "AVAILABLE-0008"
        },
        {
          "ClassCode": "3A",
          "ClassName": "THIRD AC",
          "Availability": "AVAILABLE-0010"
        }
      ]
    },
    {
      "TrainNo": "12955",
      "TrainName": "JAIPUR SUPERFAST",
      "TrainType": "SUPERFAST",
      "From": "NDLS",
      "To": "BCT",
      "DepartureTime

```
