# Write Pig Latin Commands: Write Pig Latin scripts sort, group, join, project, and filter your data.

Pig Latin is a high-level language that allows you to process data using Pig. Pig Latin statements are composed of operators that take a relation as input and produce another relation as output. Pig Latin scripts can be executed in two modes: local mode and MapReduce mode. In local mode, Pig runs on a single machine without using Hadoop. In MapReduce mode, Pig runs on a Hadoop cluster and converts Pig Latin scripts into MapReduce jobs.

Here are some examples of how to write Pig Latin commands to sort, group, join, project, and filter your data.

## Sort

The SORT operator sorts a relation by one or more fields in ascending or descending order. The syntax is:

`sorted_relation = SORT relation BY field1 [ASC|DESC], field2 [ASC|DESC], ...;`

For example, to sort a relation called students by name in ascending order and age in descending order, you can write:

`sorted_students = SORT students BY name ASC, age DESC;`

## Group

The GROUP operator groups a relation by one or more fields and creates a nested relation for each group. The syntax is:

`grouped_relation = GROUP relation BY field1, field2, ...;`

For example, to group a relation called students by gender and major, you can write:

`grouped_students = GROUP students BY gender, major;`

## Join

The JOIN operator joins two or more relations by a common field or a condition. The syntax is:

`joined_relation = JOIN relation1 BY field1, relation2 BY field2, ... [USING 'join_type'];`

The join_type can be one of the following: 'replicated', 'skewed', 'merge', 'hash', or 'default'. The default join type is hash join, which partitions the relations by the join keys and performs a join in parallel. The other join types are used for optimizing the join performance based on the characteristics of the input data.

For example, to join a relation called students with a relation called courses by the student_id field, you can write:

`joined_students_courses = JOIN students BY student_id, courses BY student_id;`

## Project

The PROJECT operator selects a subset of fields from a relation. The syntax is:

`projected_relation = FOREACH relation GENERATE field1, field2, ...;`

For example, to select the name and age fields from a relation called students, you can write:

`projected_students = FOREACH students GENERATE name, age;`

## Filter

The FILTER operator filters a relation by a condition. The syntax is:

`filtered_relation = FILTER relation BY condition;`

The condition can be any expression that evaluates to a boolean value. You can use logical operators (AND, OR, NOT) and comparison operators (==, !=, <, >, <=, >=, matches) to construct complex conditions.

For example, to filter a relation called students by age greater than 20 and major equal to 'CS', you can write:

`filtered_students = FILTER students BY age > 20 AND major == 'CS';`