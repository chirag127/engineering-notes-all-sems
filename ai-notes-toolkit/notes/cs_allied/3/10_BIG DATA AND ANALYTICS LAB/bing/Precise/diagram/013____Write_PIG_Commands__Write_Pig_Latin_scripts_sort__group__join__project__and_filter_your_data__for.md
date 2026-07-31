## PIG Commands

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is designed to process large data sets. Pig Latin scripts can be used to sort, group, join, project, and filter your data.

Here are some common Pig Latin commands that can be used to manipulate data:

1. **SORT**: The `ORDER BY` command is used to sort data in ascending or descending order based on one or more fields. The syntax is as follows:
```
data_ordered = ORDER data BY field [ASC|DESC];
```

2. **GROUP**: The `GROUP` command is used to group data based on one or more fields. The syntax is as follows:
```
data_grouped = GROUP data BY field;
```

3. **JOIN**: The `JOIN` command is used to join two or more data sets based on a common field. The syntax is as follows:
```
data_joined = JOIN data1 BY field1, data2 BY field2;
```

4. **PROJECT**: The `FOREACH` command is used to project specific fields from a data set. The syntax is as follows:
```
data_projected = FOREACH data GENERATE field1, field2, ...;
```

5. **FILTER**: The `FILTER` command is used to filter data based on a condition. The syntax is as follows:
```
data_filtered = FILTER data BY condition;
```

These are some of the basic Pig Latin commands that can be used to manipulate data in a BIG DATA AND ANALYTICS LAB. It is important to note that Pig Latin is a case-sensitive language and commands must be written in uppercase. Additionally, fields and conditions must be specified correctly to ensure accurate results.