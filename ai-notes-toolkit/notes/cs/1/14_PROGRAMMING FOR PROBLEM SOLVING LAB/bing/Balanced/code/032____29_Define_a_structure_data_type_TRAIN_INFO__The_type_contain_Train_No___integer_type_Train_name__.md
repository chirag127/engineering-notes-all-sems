Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

## 29.Define a structure data type TRAIN_INFO. The type contain Train No.: integer type Train name: string Departure Time: aggregate type TIME Arrival Time: aggregate type TIME Start station: string End station: string The structure type Time contains two integer members: hour and minute. Maintain a train timetable and implement the following operations:

- A structure data type is a user-defined data type that can store a group of related values of different types.
- A structure data type TRAIN_INFO can be defined as follows:

```c
// Define a structure type TIME
struct TIME {
  int hour; // hour member
  int minute; // minute member
};

// Define a structure type TRAIN_INFO
struct TRAIN_INFO {
  int train_no; // train number member
  char train_name[50]; // train name member
  struct TIME departure_time; // departure time member
  struct TIME arrival_time; // arrival time member
  char start_station[50]; // start station member
  char end_station[50]; // end station member
};
```

- To maintain a train timetable, we can declare an array of TRAIN_INFO structures and initialize it with some sample data:

```c
// Declare an array of TRAIN_INFO structures
struct TRAIN_INFO timetable[5] = {
  {101, "Shatabdi Express", {9, 30}, {13, 15}, "Delhi", "Chandigarh"},
  {102, "Rajdhani Express", {17, 45}, {22, 30}, "Mumbai", "Delhi"},
  {103, "Duronto Express", {6, 00}, {10, 00}, "Chennai", "Bangalore"},
  {104, "Garib Rath", {15, 00}, {20, 00}, "Lucknow", "Delhi"},
  {105, "Jan Shatabdi", {12, 00}, {16, 00}, "Delhi", "Jaipur"}
};
```

- To implement the following operations, we can define some functions that take the timetable array and other parameters as arguments and perform the required tasks:

  - Display the train details given the train number:

  ```c
  // Define a function to display the train details given the train number
  void display_train_details(struct TRAIN_INFO timetable[], int n, int train_no) {
    // Declare a variable to store the index of the train
    int index = -1;
    // Loop through the timetable array to find the train
    for (int i = 0; i < n; i++) {
      // If the train number matches, store the index and break the loop
      if (timetable[i].train_no == train_no) {
        index = i;
        break;
      }
    }
    // If the index is not -1, display the train details
    if (index != -1) {
      printf("Train No.: %d\n", timetable[index].train_no);
      printf("Train Name: %s\n", timetable[index].train_name);
      printf("Departure Time: %02d:%02d\n", timetable[index].departure_time.hour, timetable[index].departure_time.minute);
      printf("Arrival Time: %02d:%02d\n", timetable[index].arrival_time.hour, timetable[index].arrival_time.minute);
      printf("Start Station: %s\n", timetable[index].start_station);
      printf("End Station: %s\n", timetable[index].end_station);
    }
    // Else, display an error message
    else {
      printf("Train not found.\n");
    }
  }
  ```

  - Display all the trains that depart from a given station:

  ```c
  // Define a function to display all the trains that depart from a given station
  void display_trains_from_station(struct TRAIN_INFO timetable[], int n, char station[]) {
    // Declare a variable to store the number of trains found
    int count = 0;
    // Loop through the timetable array to find the trains
    for (int i = 0; i < n; i++) {
      // If the start station matches, display the train details and increment the count
      if (strcmp(timetable[i].start_station, station) == 0) {
        printf("Train No.: %d\n", timetable[i].train_no);
        printf("Train Name: %s\n", timetable[i].train_name);
        printf("Departure Time: %02d:%02d\n", timetable[i].departure_time.hour, timetable[i

```
