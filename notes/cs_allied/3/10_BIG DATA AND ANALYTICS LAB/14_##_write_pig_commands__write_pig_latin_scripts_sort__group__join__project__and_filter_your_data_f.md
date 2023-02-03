## Write PIG Commands: Write Pig Latin scripts sort, group, join, project, and filter your data. for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

Pig is a high-level platform for creating MapReduce programs in Apache Hadoop. Pig Latin is a data flow language used to write Pig scripts, which are used to process large datasets in Hadoop. Pig Latin provides a simple and concise way to process and analyze data, and provides several built-in operations for sorting, grouping, joining, projecting, and filtering data.

Here are some examples of Pig Latin scripts for sorting, grouping, joining, projecting, and filtering data:

1. Sorting data: You can sort data in Pig Latin using the ORDER BY clause. For example:

```
data = LOAD 'data.txt' AS (name:chararray, age:int);
sorted_data = ORDER data BY age;
DUMP sorted_data;
```

2. Grouping data: You can group data in Pig Latin using the GROUP clause. For example:

```
data = LOAD 'data.txt' AS (name:chararray, age:int);
grouped_data = GROUP data BY age;
DUMP grouped_data;
```

3. Joining data: You can join data in Pig Latin using the JOIN clause. For example:

```
data1 = LOAD 'data1.txt' AS (id:int, name:chararray);
data2 = LOAD 'data2.txt' AS (id:int, age:int);
joined_data = JOIN data1 BY id, data2 BY id;
DUMP joined_data;
```

4. Projecting data: You can project data in Pig Latin using the FOREACH clause. For example:

```
data = LOAD 'data.txt' AS (name:chararray, age:int);
projected_data = FOREACH data GENERATE name, age;
DUMP projected_data;
```

5. Filtering data: You can filter data in Pig Latin using the FILTER clause. For example:

```
data = LOAD 'data.txt' AS (name:chararray, age:int);
filtered_data = FILTER data BY age > 30;
DUMP filtered_data;
```

In conclusion, Pig Latin is a data flow language used to write Pig scripts, which are used to process large datasets in Hadoop. Pig Latin provides several built-in operations for sorting, grouping, joining, projecting, and filtering data, and can be used to perform these operations in a simple and concise way.
