## a. List all the trains (sorted according to train number) that depart from a particular section.

- To list all the trains that depart from a particular section, we need to use the **section** and **train** tables from the railway database.
- The **section** table contains information about the sections of the railway network, such as the section number, the starting station, the ending station, and the distance.
- The **train** table contains information about the trains that operate on the network, such as the train number, the train name, the source station, the destination station, and the departure time.
- To list all the trains that depart from a particular section, we need to join the **section** and **train** tables on the condition that the starting station of the section matches the source station of the train.
- We also need to sort the result by the train number in ascending order, using the **ORDER BY** clause.
- The SQL query to list all the trains that depart from a particular section is:

```sql
SELECT train.train_no, train.train_name
FROM section
JOIN train
ON section.starting_station = train.source_station
WHERE section.section_no = <section number>
ORDER BY train.train_no;
```

- Here, `<section number>` is a placeholder for the section number that we want to query.
- For example, if we want to list all the trains that depart from section 1, we can use the following query:

```sql
SELECT train.train_no, train.train_name
FROM section
JOIN train
ON section.starting_station = train.source_station
WHERE section.section_no = 1
ORDER BY train.train_no;
```

- The output of this query might look something like this:

| train_no | train_name |
| -------- | ---------- |
| 101      | Rajdhani   |
| 102      | Shatabdi   |
| 103      | Duronto    |
| 104      | Garib Rath |
| 105      | Jan Shatabdi |

- This output shows that there are five trains that depart from section 1, and they are sorted by their train numbers.