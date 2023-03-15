## TRAIN_INFO Structure Data Type

A structure data type `TRAIN_INFO` can be defined to maintain a train timetable. The structure contains the following members:

1. `Train No.`: An integer type member to store the train number.
2. `Train name`: A string type member to store the train name.
3. `Departure Time`: An aggregate type `TIME` to store the departure time of the train.
4. `Arrival Time`: An aggregate type `TIME` to store the arrival time of the train.
5. `Start station`: A string type member to store the name of the start station.
6. `End station`: A string type member to store the name of the end station.

The structure type `TIME` contains two integer members: `hour` and `minute`.

The `TRAIN_INFO` structure data type can be used to maintain a train timetable and implement various operations. For example, the timetable can be searched to find trains between two stations, or to find trains that depart or arrive at a specific time. The timetable can also be updated to add or remove trains, or to change the schedule of existing trains.