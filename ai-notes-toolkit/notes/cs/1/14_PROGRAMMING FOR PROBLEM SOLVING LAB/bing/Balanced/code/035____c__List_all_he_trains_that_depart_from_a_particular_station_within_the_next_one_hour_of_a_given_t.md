## c. List all the trains that depart from a particular station within the next one hour of a given time.

- To list all the trains that depart from a particular station within the next one hour of a given time, one possible algorithm is:

  - Input: station name, current time
  - Output: a list of train names, destinations, and departure times
  - Steps:
    - Initialize an empty list to store the output
    - Access the database of train schedules for the given station
    - For each train in the database, check if its departure time is within the next one hour of the current time
    - If yes, append the train name, destination, and departure time to the output list
    - Sort the output list by departure time in ascending order
    - Return the output list

- For example, if the input is station name = "New York Penn Station", current time = "15:39", the output list could be:

  - Train name: Acela Express, Destination: Boston South Station, Departure time: 15:45
  - Train name: Northeast Regional, Destination: Washington Union Station, Departure time: 15:55
  - Train name: Empire Service, Destination: Albany-Rensselaer, Departure time: 16:00
  - Train name: Keystone Service, Destination: Harrisburg, Departure time: 16:05
  - Train name: Maple Leaf, Destination: Toronto Union Station, Departure time: 16:15
  - Train name: Pennsylvanian, Destination: Pittsburgh, Departure time: 16:25
  - Train name: Vermonter, Destination: St. Albans, Departure time: 16:35