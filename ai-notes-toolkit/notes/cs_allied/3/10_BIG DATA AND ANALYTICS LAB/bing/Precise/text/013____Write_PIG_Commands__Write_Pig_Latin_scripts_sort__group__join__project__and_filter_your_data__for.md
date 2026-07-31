## PIG Commands

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is designed to process large data sets. Pig Latin scripts can be used to sort, group, join, project, and filter data.

Here are some common Pig Latin commands for sorting, grouping, joining, projecting, and filtering data:

1. **SORT**: The `ORDER BY` command is used to sort data in ascending or descending order based on one or more fields. For example, to sort data in ascending order based on the first field, use the following command: `data_sorted = ORDER data BY $0;`

2. **GROUP**: The `GROUP` command is used to group data based on one or more fields. For example, to group data based on the first field, use the following command: `data_grouped = GROUP data BY $0;`

3. **JOIN**: The `JOIN` command is used to join two or more data sets based on a common field. For example, to join two data sets `data1` and `data2` based on the first field, use the following command: `data_joined = JOIN data1 BY $0, data2 BY $0;`

4. **PROJECT**: The `FOREACH` command is used to project specific fields from a data set. For example, to project the first and third fields from a data set, use the following command: `data_projected = FOREACH data GENERATE $0, $2;`

5. **FILTER**: The `FILTER` command is used to filter data based on a condition. For example, to filter data based on the value of the first field being greater than 10, use the following command: `data_filtered = FILTER data BY $0 > 10;`

These are some of the basic Pig Latin commands that can be used to sort, group, join, project, and filter data in a BIG DATA AND ANALYTICS LAB. Remember to always test your scripts and validate your results before using them in a production environment.