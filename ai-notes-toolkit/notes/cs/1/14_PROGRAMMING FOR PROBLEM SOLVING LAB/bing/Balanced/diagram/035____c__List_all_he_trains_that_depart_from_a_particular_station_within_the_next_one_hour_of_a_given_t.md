## c. List all the trains that depart from a particular station within the next one hour of a given time.

To list all the trains that depart from a particular station within the next one hour of a given time, we need to follow these steps:

- Define the station name and the given time as input variables.
- Access the train schedule database and query for all the records that match the station name as the departure station.
- Filter the records by comparing the departure time with the given time and selecting only those that are within the next one hour.
- Sort the records by the departure time in ascending order.
- Display the records as a table with columns such as train number, train name, destination, departure time, and status.

Here is an example of the output table for the station name "New Delhi" and the given time "15:39:03" on 15 March 2023:

| Train Number | Train Name | Destination | Departure Time | Status |
| ------------ | ---------- | ----------- | -------------- | ------ |
| 12002 | Bhopal Shatabdi | Bhopal | 15:40:00 | On Time |
| 12450 | Goa Sampark Kranti | Madgaon | 15:45:00 | Delayed by 10 min |
| 12952 | Mumbai Rajdhani | Mumbai Central | 16:00:00 | On Time |
| 12302 | Kolkata Rajdhani | Howrah | 16:10:00 | On Time |
| 12616 | Grand Trunk Express | Chennai Central | 16:20:00 | On Time |
| 12414 | Jammu Tawi Express | Jammu Tawi | 16:30:00 | On Time |
| 12926 | Paschim Express | Bandra Terminus | 16:35:00 | On Time |
| 12264 | Pune Duronto | Pune | 16:40:00 | On Time |