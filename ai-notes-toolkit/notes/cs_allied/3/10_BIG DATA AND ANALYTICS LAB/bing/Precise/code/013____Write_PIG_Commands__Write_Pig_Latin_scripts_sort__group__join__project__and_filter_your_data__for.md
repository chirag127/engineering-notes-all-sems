## PIG Commands

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is designed to process large data sets. Here are some common Pig Latin commands used to sort, group, join, project, and filter data:

1. **SORT**: The `ORDER BY` command is used to sort data in ascending or descending order based on one or more fields. For example, to sort data in ascending order based on the first field: `data = ORDER data BY $0;`

2. **GROUP**: The `GROUP` command is used to group data based on one or more fields. For example, to group data based on the first field: `grouped_data = GROUP data BY $0;`

3. **JOIN**: The `JOIN` command is used to join two or more data sets based on a common field. For example, to join two data sets based on the first field: `joined_data = JOIN data1 BY $0, data2 BY $0;`

4. **PROJECT**: The `FOREACH` command is used to project specific fields from a data set. For example, to project the first and third fields from a data set: `projected_data = FOREACH data GENERATE $0, $2;`

5. **FILTER**: The `FILTER` command is used to filter data based on a condition. For example, to filter data where the first field is greater than 10: `filtered_data = FILTER data BY ($0 > 10);`
