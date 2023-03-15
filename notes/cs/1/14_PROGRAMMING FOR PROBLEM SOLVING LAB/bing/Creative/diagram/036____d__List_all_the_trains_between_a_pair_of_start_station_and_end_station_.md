## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use the following steps:
  - Define the start station and the end station as variables, such as `start = "New York"` and `end = "Boston"`.
  - Create a list of trains that contains the train number, departure time, arrival time, and intermediate stations for each train, such as `trains = [[101, "08:00", "10:30", ["Newark", "New Haven"]], [102, "09:00", "11:45", ["Newark", "Providence"]], [103, "10:00", "12:15", ["Newark", "New Haven", "Providence"]]]`.
  - Loop through the list of trains and check if the start station and the end station are in the intermediate stations of each train, such as `for train in trains: if start in train[3] and end in train[3]:`.
  - If the condition is true, print the train number, departure time, and arrival time of the train, such as `print(f"Train {train[0]} departs from {start} at {train[1]} and arrives at {end} at {train[2]}.")`.
  - If the condition is false, skip the train and continue the loop, such as `else: continue`.
- Here is an example of the output for the given start station and end station:

```
Train 102 departs from New York at 09:00 and arrives at Boston at 11:45.
Train 103 departs from New York at 10:00 and arrives at Boston at 12:15.
```