## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides access to various data related to the Indian Railways network, such as train status, seat availability, fare enquiry, station code, etc.
- To use the Indian Railways API, we need to register and obtain an API key from https://indianrailapi.com/.
- Once we have the API key, we can use the Train Between Stations API to get the list of trains between a pair of start station and end station.
- The Train Between Stations API requires the following parameters:
  - API Key: The unique key obtained from the Indian Railways API website.
  - From Station Code: The station code of the start station. For example, NDLS for New Delhi.
  - To Station Code: The station code of the end station. For example, BCT for Mumbai Central.
  - Date: The date of travel in DD-MM-YYYY format. For example, 15-03-2023.
- The Train Between Stations API returns a JSON response that contains the following information for each train:
  - Train No: The train number.
  - Train Name: The train name.
  - Train Type: The train type, such as Rajdhani, Shatabdi, Duronto, etc.
  - Source: The source station code and name.
  - Destination: The destination station code and name.
  - Departure Time: The departure time from the source station.
  - Arrival Time: The arrival time at the destination station.
  - Travel Time: The total travel time in HH:MM format.
  - Days: The days of operation of the train in a week. For example, MON, TUE, WED, etc.
  - Classes: The classes available in the train, such as 1A, 2A, 3A, SL, etc.
  - Availability: The availability status of the seats in each class, such as AVAILABLE, RAC, WL, etc.
- For example, if we want to list all the trains between New Delhi and Mumbai Central on 15-03-2023, we can use the following URL:

  https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<API Key>/From/<NDLS>/To/<BCT>/Date/<15-03-2023>

- The JSON response will look something like this:

```json
{
  "ResponseCode": 200,
  "Message": "Success",
  "Trains": [
    {
      "TrainNo": "12951",
      "TrainName": "MUMBAI RAJDHANI",
      "TrainType": "RAJDHANI",
      "Source": "NDLS NEW DELHI",
      "Destination": "BCT MUMBAI CENTRAL",
      "DepartureTime": "16:25",
      "ArrivalTime": "08:15",
      "TravelTime": "15:50",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": "1A, 2A, 3A",
      "Availability": [
        {
          "ClassCode": "1A",
          "Availability": "AVAILABLE 4"
        },
        {
          "ClassCode": "2A",
          "Availability": "AVAILABLE 6"
        },
        {
          "ClassCode": "3A",
          "Availability": "WL 1"
        }
      ]
    },
    {
      "TrainNo": "12953",
      "TrainName": "AUG KR RAJ EXP",
      "TrainType": "RAJDHANI",
      "Source": "NDLS NEW DELHI",
      "Destination": "BCT MUMBAI CENTRAL",
      "DepartureTime": "17:40",
      "ArrivalTime": "09:45",
      "TravelTime": "16:05",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": "1A, 2A, 3A",
      "Availability": [
        {
          "ClassCode": "1A",
          "Availability": "AVAILABLE 2"
        },
        {
          "ClassCode": "2A",
          "Availability": "AVAILABLE 10"
        },
        {
          "ClassCode": "3A",
          "Availability": "WL 2

```
