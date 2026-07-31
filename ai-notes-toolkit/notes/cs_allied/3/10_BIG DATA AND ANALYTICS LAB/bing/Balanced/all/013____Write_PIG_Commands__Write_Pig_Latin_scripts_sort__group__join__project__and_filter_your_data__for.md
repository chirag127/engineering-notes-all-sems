# Write Pig Latin scripts to sort, group, join, project, and filter your data

Pig Latin is a dataflow scripting language for processing large datasets using Apache Hadoop. Pig Latin scripts can perform various operations on the data, such as sorting, grouping, joining, projecting, and filtering. Here are some examples of how to write Pig Latin scripts for these operations:

- Sorting: To sort the data by one or more fields, use the `ORDER BY` operator. For example, to sort a relation called `students` by their name and age, you can write:

```
sorted_students = ORDER students BY name, age;
```

- Grouping: To group the data by one or more fields, use the `GROUP BY` operator. For example, to group the students by their major, you can write:

```
grouped_students = GROUP students BY major;
```

- Joining: To join two or more relations by one or more fields, use the `JOIN` operator. For example, to join the students with another relation called `courses` by their student_id, you can write:

```
joined_students_courses = JOIN students BY student_id, courses BY student_id;
```

- Projecting: To select a subset of fields from a relation, use the `FOREACH` operator with the `GENERATE` clause. For example, to project only the name and major of the students, you can write:

```
projected_students = FOREACH students GENERATE name, major;
```

- Filtering: To filter the data based on some condition, use the `FILTER` operator with the `BY` clause. For example, to filter the students who have a GPA greater than 3.5, you can write:

```
filtered_students = FILTER students BY GPA > 3.5;
```

These are some of the basic Pig Latin commands to manipulate the data. You can also use other operators and functions to perform more complex tasks, such as aggregation, transformation, and evaluation. For more details, you can refer to the official Pig Latin documentation.