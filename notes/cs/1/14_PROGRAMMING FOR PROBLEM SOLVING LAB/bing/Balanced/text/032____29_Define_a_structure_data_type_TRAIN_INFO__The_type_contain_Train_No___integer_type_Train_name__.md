## 29.Define a structure data type TRAIN_INFO. The type contain Train No.: integer type Train name: string Departure Time: aggregate type TIME Arrival Time: aggregate type TIME Start station: string End station: string The structure type Time contains two integer members: hour and minute. Maintain a train timetable and implement the following operations:

- To define a structure data type TRAIN_INFO, we can use the following syntax in C:

```c
// Define the structure type TIME
struct TIME {
  int hour; // integer member for hour
  int minute; // integer member for minute
};

// Define the structure type TRAIN_INFO
struct TRAIN_INFO {
  int train_no; // integer member for train number
  char train_name[50]; // string member for train name
  struct TIME departure_time; // aggregate member for departure time
  struct TIME arrival_time; // aggregate member for arrival time
  char start_station[50]; // string member for start station
  char end_station[50]; // string member for end station
};
```

- To maintain a train timetable, we can declare an array of TRAIN_INFO structures and initialize it with some sample data:

```c
// Declare an array of TRAIN_INFO structures
struct TRAIN_INFO timetable[5];

// Initialize the array with some sample data
timetable[0].train_no = 101;
strcpy(timetable[0].train_name, "Rajdhani Express");
timetable[0].departure_time.hour = 10;
timetable[0].departure_time.minute = 15;
timetable[0].arrival_time.hour = 18;
timetable[0].arrival_time.minute = 30;
strcpy(timetable[0].start_station, "New Delhi");
strcpy(timetable[0].end_station, "Mumbai");

timetable[1].train_no = 102;
strcpy(timetable[1].train_name, "Shatabdi Express");
timetable[1].departure_time.hour = 8;
timetable[1].departure_time.minute = 45;
timetable[1].arrival_time.hour = 12;
timetable[1].arrival_time.minute = 15;
strcpy(timetable[1].start_station, "Chennai");
strcpy(timetable[1].end_station, "Bangalore");

timetable[2].train_no = 103;
strcpy(timetable[2].train_name, "Duronto Express");
timetable[2].departure_time.hour = 6;
timetable[2].departure_time.minute = 30;
timetable[2].arrival_time.hour = 14;
timetable[2].arrival_time.minute = 45;
strcpy(timetable[2].start_station, "Kolkata");
strcpy(timetable[2].end_station, "Delhi");

timetable[3].train_no = 104;
strcpy(timetable[3].train_name, "Garib Rath");
timetable[3].departure_time.hour = 9;
timetable[3].departure_time.minute = 0;
timetable[3].arrival_time.hour = 16;
timetable[3].arrival_time.minute = 0;
strcpy(timetable[3].start_station, "Hyderabad");
strcpy(timetable[3].end_station, "Pune");

timetable[4].train_no = 105;
strcpy(timetable[4].train_name, "Jan Shatabdi");
timetable[4].departure_time.hour = 7;
timetable[4].departure_time.minute = 15;
timetable[4].arrival_time.hour = 11;
timetable[4].arrival_time.minute = 30;
strcpy(timetable[4].start_station, "Ahmedabad");
strcpy(timetable[4].end_station, "Surat");
```

- To implement the following operations, we can define some functions that take the timetable array and other parameters as arguments and perform the required tasks:

  - Display the train number, train name, departure time and arrival time of all the trains.
  - Display the train number, train name, departure time and arrival time of a particular train given its train number.
  - Display the train number, train name, departure time and arrival time of all the trains that start from a given station.
  - Display the train number, train name, departure time and arrival time of all the trains that end at a given station.
  - Display the train number, train name, departure time and arrival time of all the trains that have a travel time less than a given duration.

```c
// Define a function to display the train number, train name, departure time and arrival time of all the trains
void display_all(struct TRAIN_INFO timetable[], int size) {