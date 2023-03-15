## TRAIN_INFO Structure Data Type

The `TRAIN_INFO` structure data type is used to maintain a train timetable. It contains the following members:

1. `Train No.`: An integer type member that represents the train number.
2. `Train name`: A string type member that represents the train name.
3. `Departure Time`: An aggregate type `TIME` member that represents the departure time of the train.
4. `Arrival Time`: An aggregate type `TIME` member that represents the arrival time of the train.
5. `Start station`: A string type member that represents the starting station of the train.
6. `End station`: A string type member that represents the ending station of the train.

The `TIME` structure type contains two integer members: `hour` and `minute`. These members represent the hour and minute components of the time, respectively.

Using the `TRAIN_INFO` structure data type, a train timetable can be maintained and the following operations can be implemented:

- Adding a new train to the timetable.
- Removing a train from the timetable.
- Updating the information of a train in the timetable.
- Searching for a train in the timetable.
- Displaying the timetable.