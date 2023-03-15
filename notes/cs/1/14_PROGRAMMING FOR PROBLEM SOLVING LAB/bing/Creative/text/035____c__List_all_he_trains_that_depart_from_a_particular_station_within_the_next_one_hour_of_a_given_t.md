## c. List all the trains that depart from a particular station within the next one hour of a given time.

- To list all the trains that depart from a particular station within the next one hour of a given time, one possible algorithm is as follows:

  - Input: station name, current time
  - Output: list of train names and departure times
  - Steps:
    - Initialize an empty list to store the output
    - Access the database of train schedules for the given station
    - For each train in the database, check if its departure time is within the next one hour of the current time
    - If yes, append the train name and departure time to the output list
    - If no, skip the train and continue the loop
    - Sort the output list by departure time in ascending order
    - Return the output list

- An example of the input and output for this algorithm is as follows:

  - Input: station name = "New York Penn Station", current time = "15:39"
  - Output: list of train names and departure times = [["Amtrak Northeast Regional 160", "15:43"], ["NJ Transit Northeast Corridor 7858", "15:47"], ["Amtrak Acela Express 2160", "15:51"], ["NJ Transit North Jersey Coast Line 3268", "15:55"], ["Amtrak Keystone Service 650", "15:59"], ["NJ Transit Northeast Corridor 7860", "16:02"], ["Amtrak Northeast Regional 162", "16:03"], ["NJ Transit Morris & Essex Line 6650", "16:07"], ["Amtrak Acela Express 2162", "16:11"], ["NJ Transit Northeast Corridor 7862", "16:17"], ["Amtrak Keystone Service 652", "16:19"], ["NJ Transit North Jersey Coast Line 3270", "16:25"], ["Amtrak Northeast Regional 164", "16:33"], ["NJ Transit Northeast Corridor 7864", "16:37"]]