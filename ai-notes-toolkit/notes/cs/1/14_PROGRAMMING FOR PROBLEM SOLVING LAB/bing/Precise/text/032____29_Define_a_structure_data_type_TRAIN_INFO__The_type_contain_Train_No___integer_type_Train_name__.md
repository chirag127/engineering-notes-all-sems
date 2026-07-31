## TRAIN_INFO Structure Data Type

A structure data type is a user-defined data type that groups together variables of different data types under a single name. The `TRAIN_INFO` structure data type can be defined to contain information about a train, including its train number, train name, departure time, arrival time, start station, and end station.

Here is an example of how the `TRAIN_INFO` structure data type can be defined:

```c
typedef struct {
    int train_no;
    char train_name[50];
    struct TIME departure_time;
    struct TIME arrival_time;
    char start_station[50];
    char end_station[50];
} TRAIN_INFO;
```

The `TIME` structure data type is an aggregate type that contains two integer members: `hour` and `minute`. It can be defined as follows:

```c
typedef struct {
    int hour;
    int minute;
} TIME;
```

Using these structure data types, a train timetable can be maintained and the following operations can be implemented:
- Add a new train to the timetable
- Remove a train from the timetable
- Update the information of a train in the timetable
- Search for a train in the timetable by its train number or train name
- Display the timetable in a user-friendly format

These operations can be implemented using functions that take the `TRAIN_INFO` structure data type as an argument and manipulate the data accordingly. For example, the `add_train` function can take a `TRAIN_INFO` structure as an argument and add it to the timetable. The `remove_train` function can take a train number as an argument and remove the corresponding train from the timetable. The `update_train` function can take a `TRAIN_INFO` structure as an argument and update the information of the corresponding train in the timetable. The `search_train` function can take a train number or train name as an argument and search for the corresponding train in the timetable. The `display_timetable` function can display the timetable in a user-friendly format.