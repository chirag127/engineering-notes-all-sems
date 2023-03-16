## Write Pig Latin scripts to sort, group, join, project, and filter your data.

Pig Latin is a high-level scripting language that allows you to manipulate data in Apache Pig. Pig Latin scripts consist of a series of statements that apply various operators to relations. Relations are named collections of tuples, which are ordered sets of fields. Fields can be of any type, such as int, chararray, float, etc.

Here are some examples of how to write Pig Latin scripts to sort, group, join, project, and filter your data.

### Sort

The SORT operator sorts a relation by one or more fields in ascending or descending order. The syntax is:

`sorted_relation = SORT relation BY field1 [ASC|DESC], field2 [ASC|DESC], ...;`

For example, to sort the student data by name in ascending order and then by age in descending order, you can write:

`Student_data = LOAD 'student_data.txt' USING PigStorage(',') AS (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);`

`Sorted_data = SORT Student_data BY firstname ASC, age DESC;`

### Group

The GROUP operator groups a relation by one or more fields, creating a new relation with two fields: group and bag. The group field contains the values of the fields that were grouped by, and the bag field contains all the tuples that have the same group values. The syntax is:

`grouped_relation = GROUP relation BY field1, field2, ...;`

For example, to group the student data by city, you can write:

`Grouped_data = GROUP Student_data BY city;`

### Join

The JOIN operator joins two or more relations by a common field or a set of fields. The syntax is:

`joined_relation = JOIN relation1 BY field1, relation2 BY field2, ...;`

For example, to join the student data with another relation that contains the scores of each student, you can write:

`Score_data = LOAD 'score_data.txt' USING PigStorage(',') AS (id:int, score:int);`

`Joined_data = JOIN Student_data BY id, Score_data BY id;`

### Project

The PROJECT operator selects a subset of fields from a relation. The syntax is:

`projected_relation = FOREACH relation GENERATE field1, field2, ...;`

For example, to project only the name and score of each student, you can write:

`Projected_data = FOREACH Joined_data GENERATE firstname, lastname, score;`

### Filter

The FILTER operator filters a relation by applying a condition to each tuple. The syntax is:

`filtered_relation = FILTER relation BY condition;`

For example, to filter the student data by selecting only those who have a score above 80, you can write:

`Filtered_data = FILTER Joined_data BY score > 80;`