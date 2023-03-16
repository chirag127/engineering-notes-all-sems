## Write Pig Latin scripts to sort, group, join, project, and filter your data

Pig Latin is a dataflow scripting language that allows you to process large amounts of data on Hadoop. You can write Pig Latin scripts to perform various operations on your data, such as sorting, grouping, joining, projecting, and filtering. Here are some examples of how to write Pig Latin scripts for these operations:

- **Sort**: You can use the ORDER BY operator to sort a relation by one or more fields in ascending or descending order. For example, the following script sorts the relation `students` by `name` in ascending order and stores the result in `sorted_students`:

```pig
students = LOAD 'students.txt' AS (name:chararray, age:int, grade:float);
sorted_students = ORDER students BY name;
```

- **Group**: You can use the GROUP or COGROUP operator to group a relation by one or more fields and create a nested relation. For example, the following script groups the relation `students` by `grade` and stores the result in `grouped_students`:

```pig
students = LOAD 'students.txt' AS (name:chararray, age:int, grade:float);
grouped_students = GROUP students BY grade;
```

- **Join**: You can use the JOIN operator to perform an inner, equijoin join of two or more relations based on common field values. Inner joins ignore null keys, so it makes sense to filter them out before the join. For example, the following script joins the relations `students` and `courses` by `student_id` and stores the result in `joined_data`:

```pig
students = LOAD 'students.txt' AS (student_id:int, name:chararray, age:int, grade:float);
courses = LOAD 'courses.txt' AS (course_id:int, course_name:chararray, student_id:int);
students = FILTER students BY student_id IS NOT NULL;
courses = FILTER courses BY student_id IS NOT NULL;
joined_data = JOIN students BY student_id, courses BY student_id;
```

- **Project**: You can use the FOREACH operator to project a relation by selecting or generating new fields. For example, the following script projects the relation `students` by selecting only the `name` and `grade` fields and stores the result in `projected_students`:

```pig
students = LOAD 'students.txt' AS (name:chararray, age:int, grade:float);
projected_students = FOREACH students GENERATE name, grade;
```

- **Filter**: You can use the FILTER operator to filter a relation by applying a condition on one or more fields. For example, the following script filters the relation `students` by selecting only the records where `grade` is greater than or equal to 80 and stores the result in `filtered_students`:

```pig
students = LOAD 'students.txt' AS (name:chararray, age:int, grade:float);
filtered_students = FILTER students BY grade >= 80;
```

These are some of the basic Pig Latin commands that you can use to sort, group, join, project, and filter your data. You can also use other operators and functions to perform more complex operations on your data. For more information, you can refer to the Pig Latin documentation.