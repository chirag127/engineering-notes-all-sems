## 29. Define a structure data type TRAIN_INFO and its operations

A structure data type is a composite data type that groups together variables of different data types. In this case, we define the structure data type TRAIN_INFO that contains the following fields:
- Train No.: an integer type
- Train name: a string
- Departure Time: an aggregate type TIME
- Arrival Time: an aggregate type TIME
- Start station: a string
- End station: a string

We also define the structure type TIME that contains two integer members: hour and minute. 

To maintain a train timetable using this structure data type, we can implement the following operations:
- Add a new train to the timetable: this operation requires the user to input the train information, including the train number, name, departure time, arrival time, start station, and end station. The information is then stored in the timetable as a new TRAIN_INFO structure.
- Remove a train from the timetable: this operation requires the user to input the train number of the train to be removed. The corresponding TRAIN_INFO structure is then removed from the timetable.
- Search for a train in the timetable: this operation requires the user to input the train number of the train to be searched for. If the train is found in the timetable, its TRAIN_INFO structure is displayed to the user.
- Display the entire timetable: this operation displays all the TRAIN_INFO structures in the timetable to the user, sorted by train number.
- Update the information of a train in the timetable: this operation requires the user to input the train number of the train to be updated, and then the user can update any of the train's information fields (train name, departure time, arrival time, start station, and end station).

By using the TRAIN_INFO structure data type and implementing these operations, we can easily maintain and manipulate a train timetable in a computer program.