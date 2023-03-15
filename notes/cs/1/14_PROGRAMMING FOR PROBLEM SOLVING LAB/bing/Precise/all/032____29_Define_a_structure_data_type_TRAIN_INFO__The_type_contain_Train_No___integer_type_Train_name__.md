## TRAIN_INFO Structure Data Type

A structure data type `TRAIN_INFO` can be defined to store information about a train. The structure can contain the following members:

1. `Train No.`: An integer type member to store the train number.
2. `Train name`: A string type member to store the train name.
3. `Departure Time`: An aggregate type `TIME` to store the departure time of the train.
4. `Arrival Time`: An aggregate type `TIME` to store the arrival time of the train.
5. `Start station`: A string type member to store the name of the start station.
6. `End station`: A string type member to store the name of the end station.

The structure type `TIME` contains two integer members: `hour` and `minute` to represent the time in hours and minutes.

A train timetable can be maintained using an array of `TRAIN_INFO` structures. The following operations can be implemented on the train timetable:

1. **Add a train**: A new train can be added to the timetable by creating a new `TRAIN_INFO` structure and adding it to the array of `TRAIN_INFO` structures.
2. **Search for a train**: A train can be searched in the timetable by its train number or train name.
3. **Update train information**: The information of a train can be updated by modifying the corresponding `TRAIN_INFO` structure in the array of `TRAIN_INFO` structures.
4. **Delete a train**: A train can be deleted from the timetable by removing the corresponding `TRAIN_INFO` structure from the array of `TRAIN_INFO` structures.
5. **Display train information**: The information of all the trains or a specific train can be displayed by accessing the corresponding `TRAIN_INFO` structures in the array of `TRAIN_INFO` structures.