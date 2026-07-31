## 29. Define a structure data type TRAIN_INFO

The data structure type TRAIN_INFO contains the following members:

- Train No.: integer type
- Train name: string
- Departure Time: aggregate type TIME
- Arrival Time: aggregate type TIME
- Start station: string
- End station: string

The structure type TIME contains two integer members: hour and minute.

To maintain a train timetable and implement the following operations, we can use the following functions:

1. **add_train():** This function will add a new train to the timetable. It will take the train number, train name, departure time, arrival time, start station, and end station as input parameters and add them to the timetable.

2. **delete_train():** This function will delete a train from the timetable. It will take the train number as input parameter and delete the corresponding train from the timetable.

3. **search_train():** This function will search for a train in the timetable. It will take the train number as input parameter and return the corresponding train details if found.

4. **update_train():** This function will update the details of a train in the timetable. It will take the train number as input parameter and update the corresponding train details.

5. **display_timetable():** This function will display the current timetable of all the trains in the system.

By using these functions, we can maintain a train timetable and perform various operations on it. This data structure is helpful for managing and organizing the train schedules efficiently.