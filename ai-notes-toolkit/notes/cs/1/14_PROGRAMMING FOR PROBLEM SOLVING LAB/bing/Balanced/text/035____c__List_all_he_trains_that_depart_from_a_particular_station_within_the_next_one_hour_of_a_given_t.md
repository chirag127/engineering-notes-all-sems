## c. List all the trains that depart from a particular station within the next one hour of a given time.

- To list all the trains that depart from a particular station within the next one hour of a given time, one possible algorithm is as follows:

  - Input: the name of the station, the current time
  - Output: a list of trains with their departure times and destinations
  - Steps:
    - Initialize an empty list to store the output
    - Access the database of train schedules for the given station
    - For each train in the database, check if its departure time is within the next one hour of the current time
    - If yes, append the train's information to the output list
    - Sort the output list by departure time in ascending order
    - Return the output list

- For example, if the input is "New York Penn Station, 15:39", the output could be:

  - Train 1: 15:45, Boston
  - Train 2: 15:50, Washington DC
  - Train 3: 16:00, Philadelphia
  - Train 4: 16:15, Chicago
  - Train 5: 16:30, Miami
  - Train 6: 16:35, Toronto