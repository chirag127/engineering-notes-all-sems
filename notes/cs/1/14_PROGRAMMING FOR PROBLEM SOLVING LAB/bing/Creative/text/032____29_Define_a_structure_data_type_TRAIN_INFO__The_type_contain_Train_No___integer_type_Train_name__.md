Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material:

## 29.Define a structure data type TRAIN_INFO. The type contain Train No.: integer type Train name: string Departure Time: aggregate type TIME Arrival Time: aggregate type TIME Start station: string End station: string The structure type Time contains two integer members: hour and minute. Maintain a train timetable and implement the following operations:

- A structure data type is a user-defined data type that can store a group of related values of different types.
- A structure data type TRAIN_INFO can be defined as follows:

```c
// Define the structure type TIME
struct TIME
{
  int hour; // hour member
  int minute; // minute member
};

// Define the structure type TRAIN_INFO
struct TRAIN_INFO
{
  int train_no; // train number member
  char train_name[20]; // train name member
  struct TIME departure_time; // departure time member
  struct TIME arrival_time; // arrival time member
  char start_station[20]; // start station member
  char end_station[20]; // end station member
};
```

- To maintain a train timetable, we can declare an array of TRAIN_INFO structures and initialize it with some sample data:

```c
// Declare an array of TRAIN_INFO structures
struct TRAIN_INFO timetable[5] = {
  {101, "Shatabdi Express", {9, 30}, {13, 15}, "Delhi", "Chandigarh"},
  {102, "Rajdhani Express", {17, 45}, {22, 30}, "Mumbai", "Delhi"},
  {103, "Duronto Express", {6, 00}, {10, 00}, "Chennai", "Bangalore"},
  {104, "Garib Rath", {15, 00}, {19, 00}, "Lucknow", "Kanpur"},
  {105, "Jan Shatabdi", {12, 00}, {16, 00}, "Jaipur", "Agra"}
};
```

- To implement the following operations, we can use some functions that take the timetable array and other parameters as arguments and perform the required tasks:

  - Display the entire timetable
  - Display the train details by train number
  - Display the train details by train name
  - Display the trains between two stations
  - Display the trains by departure time
  - Display the trains by arrival time

- Here are some examples of how these functions can be defined and used:

```c
// Define a function to display the entire timetable
void display_timetable(struct TRAIN_INFO timetable[], int size)
{
  // Display the header
  printf("Train No.\tTrain Name\tDeparture Time\tArrival Time\tStart Station\tEnd Station\n");

  // Loop through the timetable array and display each train
  for (int i = 0; i < size; i++)
  {
    printf("%d\t\t%s\t\t%d:%d\t\t%d:%d\t\t%s\t\t%s\n", timetable[i].train_no, timetable[i].train_name, timetable[i].departure_time.hour, timetable[i].departure_time.minute, timetable[i].arrival_time.hour, timetable[i].arrival_time.minute, timetable[i].start_station, timetable[i].end_station);
  }
}

// Define a function to display the train details by train number
void display_by_train_no(struct TRAIN_INFO timetable[], int size, int train_no)
{
  // Declare a flag to indicate if the train is found or not
  int found = 0;

  // Loop through the timetable array and search for the train number
  for (int i = 0; i < size; i++)
  {
    // If the train number matches, display the train details and set the flag to 1
    if (timetable[i].train_no == train_no)
    {
      printf("Train No.\tTrain Name\tDeparture Time\tArrival Time\tStart Station\tEnd Station\n");
      printf("%d\t\t%s\t\t%d:%d\t\t%d:%d\t\t%s\t\t%s\n", timetable[i].train_no, timetable[i].train_name, timetable[i].departure_time.hour, timetable[i].departure_time.minute, timetable[i].arrival_time.hour, timetable[i].arrival_time.minute, timetable[i].start_station, timetable[i].end_station);
      found = 1;
      break;
    }
  }

  // If the flag is 0, display a message that the train is not found
  if (found == 0)
  {

```
