Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

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
  {101, "Rajdhani Express", {10, 15}, {18, 30}, "New Delhi", "Mumbai"},
  {102, "Shatabdi Express", {8, 00}, {12, 45}, "Chennai", "Bangalore"},
  {103, "Duronto Express", {6, 30}, {14, 00}, "Kolkata", "Delhi"},
  {104, "Garib Rath", {9, 45}, {16, 15}, "Hyderabad", "Pune"},
  {105, "Jan Shatabdi", {7, 30}, {13, 00}, "Jaipur", "Ahmedabad"}
};
```

- To implement the following operations, we can use some functions that take the timetable array and other parameters as arguments and perform the required tasks:

  - Display the train information given the train number
  - Display the train information given the train name
  - Display the train information given the start station and the end station
  - Display the train information given the departure time range
  - Display the train information given the arrival time range
  - Sort the train information by train number
  - Sort the train information by train name
  - Sort the train information by departure time
  - Sort the train information by arrival time

- Here are some examples of how these functions can be defined and used:

```c
// Display the train information given the train number
void display_by_train_no(struct TRAIN_INFO timetable[], int size, int train_no) {
  int i, found = 0;
  // Loop through the timetable array
  for (i = 0; i < size; i++) {
    // Check if the train number matches
    if (timetable[i].train_no == train_no) {
      // Display the train information
      printf("Train No.: %d\n", timetable[i].train_no);
      printf("Train Name: %s\n", timetable[i].train_name);
      printf("Departure Time: %02d:%02d\n", timetable[i].departure_time.hour, timetable[i].departure_time.minute);
      printf("Arrival Time: %02d:%02d\n", timetable[i].arrival_time.hour, timetable[i].arrival_time.minute);
      printf("Start Station: %s\n", timetable[i].start_station);
      printf("End Station: %s\n", timetable[i].end_station);
      printf("\n");
      // Set the found flag to 1
      found = 1;
      // Break the loop
      break;
    }
  }
  // If the found flag is 0, display a message
  if (found == 0) {
    printf("No train found with the given number.\n");
  }
}

// Display the train information given the train name
void display_by_train_name(struct TRAIN_INFO timetable[], int size, char train_name[]) {
  int i, found = 0;
  // Loop through the timetable array
  for (i = 0; i < size; i++) {
    // Check if the train name matches
    if (strcmp(timetable[i].train_name, train_name) == 0) {
      // Display the train information

```
