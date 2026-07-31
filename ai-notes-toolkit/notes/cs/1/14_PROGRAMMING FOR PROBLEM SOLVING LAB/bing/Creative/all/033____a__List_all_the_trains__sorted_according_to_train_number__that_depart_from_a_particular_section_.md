## a. List all the trains (sorted according to train number) that depart from a particular section.

- To list all the trains that depart from a particular section, we need to use the **section** and **train** tables from the railway database.
- The **section** table contains information about the sections of the railway network, such as the section number, the starting station, the ending station, and the distance.
- The **train** table contains information about the trains that operate on the network, such as the train number, the train name, the source station, the destination station, and the departure time.
- To find the trains that depart from a particular section, we need to join the two tables on the condition that the source station of the train matches the starting station of the section.
- To sort the trains according to the train number, we need to use the **order by** clause with the train number attribute in ascending order.
- The SQL query to list all the trains that depart from a particular section (say section 1) is:

```sql
select train.train_no, train.train_name, train.source, train.destination, train.departure
from section join train
on section.start = train.source
where section.section_no = 1
order by train.train_no;
```

- The output of the query will be a table with the following columns: train_no, train_name, source, destination, departure.
- The rows of the table will be the trains that depart from section 1, sorted by train number. For example:

| train_no | train_name | source | destination | departure |
| -------- | ---------- | ------ | ----------- | --------- |
| 101      | Rajdhani   | Delhi  | Mumbai     | 08:00     |
| 102      | Shatabdi   | Delhi  | Chandigarh | 09:00     |
| 103      | Duronto    | Delhi  | Kolkata    | 10:00     |
| 104      | Garib Rath | Delhi  | Patna      | 11:00     |
| 105      | Jan Shatabdi | Delhi  | Jaipur     | 12:00     |