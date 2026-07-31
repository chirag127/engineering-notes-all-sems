# PIG Commands

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is used to sort, group, join, project, and filter data. Here are some common Pig commands for working with data in a BIG DATA AND ANALYTICS LAB:

1. **SORT**: The `ORDER BY` command is used to sort data in ascending or descending order. The syntax is `alias = ORDER alias BY field [ASC|DESC];`. For example, to sort data in ascending order by the first field: `A = ORDER B BY $0;`.

2. **GROUP**: The `GROUP` command is used to group data by one or more fields. The syntax is `alias = GROUP alias BY field [, field ...];`. For example, to group data by the first field: `A = GROUP B BY $0;`.

3. **JOIN**: The `JOIN` command is used to join two or more datasets based on common fields. The syntax is `alias = JOIN alias BY field [, field ...], alias BY field [, field ...];`. For example, to join two datasets on the first field: `A = JOIN B BY $0, C BY $0;`.

4. **PROJECT**: The `FOREACH` command is used to project data, i.e., to select specific fields from a dataset. The syntax is `alias = FOREACH alias GENERATE field [, field ...];`. For example, to select the first and third fields from a dataset: `A = FOREACH B GENERATE $0, $2;`.

5. **FILTER**: The `FILTER` command is used to filter data based on a condition. The syntax is `alias = FILTER alias BY condition;`. For example, to filter data where the first field is greater than 5: `A = FILTER B BY ($0 > 5);`.

These are some of the basic Pig commands that can be used to sort, group, join, project, and filter data in a BIG DATA AND ANALYTICS LAB. Remember to always test your scripts and validate your results before using them in production.