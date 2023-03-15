## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database or a web service that contains the information about the train schedules, routes, and availability.
- One possible way to access such a database or a web service is to use an API (Application Programming Interface) that allows us to send queries and receive responses in a structured format, such as JSON (JavaScript Object Notation) or XML (Extensible Markup Language).
- For example, we can use the Indian Railways API (https://indianrailapi.com/) to list all the trains between two stations in India. The API requires an API key, which can be obtained by registering on the website.
- To use the API, we need to construct a URL (Uniform Resource Locator) that specifies the parameters of our query, such as the start station code, the end station code, the date of travel, and the API key. For example, the URL for listing all the trains between New Delhi (NDLS) and Mumbai Central (BCT) on 15 March 2023 is:

https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<API_KEY>/From/NDLS/To/BCT/Date/15-03-2023

- The API will return a JSON response that contains an array of objects, each representing a train that matches our query. Each object will have properties such as TrainNo, TrainName, Source, Destination, DepartureTime, ArrivalTime, TravelTime, etc. For example, one possible object in the response is:

{
  "TrainNo": "12952",
  "TrainName": "MUMBAI RAJDHANI",
  "Source": "NDLS",
  "Destination": "BCT",
  "DepartureTime": "16:25",
  "ArrivalTime": "08:15",
  "TravelTime": "15:50",
  "TrainType": "RAJDHANI",
  "Classes": [
    {
      "ClassCode": "1A",
      "Availability": "AVAILABLE-0002"
    },
    {
      "ClassCode": "2A",
      "Availability": "AVAILABLE-0010"
    },
    {
      "ClassCode": "3A",
      "Availability": "AVAILABLE-0015"
    }
  ]
}

- To list all the trains between the start station and the end station, we can iterate over the array of objects in the response and print or display the relevant properties of each object, such as TrainNo, TrainName, DepartureTime, ArrivalTime, etc. For example, the output of listing all the trains between New Delhi and Mumbai Central on 15 March 2023 could be:

TrainNo | TrainName | DepartureTime | ArrivalTime
------- | --------- | ------------- | -----------
12952 | MUMBAI RAJDHANI | 16:25 | 08:15
12954 | AG KRANTI RJDHN | 16:50 | 09:45
19024 | FZR BCT JANTA | 13:30 | 07:25
22210 | NDLS BCT DURONTO | 23:25 | 16:15