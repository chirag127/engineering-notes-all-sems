## a. List all the trains (sorted according to train number) that depart from a particular section.

- To list all the trains that depart from a particular section, we need to use the **section** and **train** tables from the railway database.
- The **section** table contains information about the sections of the railway network, such as the section number, the starting station, the ending station, and the distance.
- The **train** table contains information about the trains, such as the train number, the name, the type, the source station, the destination station, and the departure and arrival times.
- To list all the trains that depart from a particular section, we need to join the **section** and **train** tables on the condition that the starting station of the section matches the source station of the train.
- We also need to sort the resulting table by the train number in ascending order.
- The SQL query to perform this task is:

```sql
SELECT train.train_no, train.name, train.type, train.source, train.destination, train.departure, train.arrival
FROM section
JOIN train
ON section.start = train.source
WHERE section.sec_no = <section number>
ORDER BY train.train_no;
```

- Here, `<section number>` is a placeholder for the section number that we want to query.
- For example, if we want to list all the trains that depart from section 1, we can replace `<section number>` with 1 in the query.
- The output of the query will be a table with the following columns: train_no, name, type, source, destination, departure, and arrival.
- The table will contain one row for each train that departs from section 1, and the rows will be sorted by the train number in ascending order.