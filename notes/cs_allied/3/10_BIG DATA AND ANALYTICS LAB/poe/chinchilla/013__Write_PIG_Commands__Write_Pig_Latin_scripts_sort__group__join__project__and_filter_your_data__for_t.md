## Write PIG Commands: Write Pig Latin scripts sort, group, join, project, and filter your data.

Pig Latin is a high-level language used to analyze large datasets in Apache Hadoop. Here are some Pig Latin commands that can be used to sort, group, join, project, and filter your data:

1. Sort: The `ORDER BY` command can be used to sort the data in ascending or descending order. For example, `ORDER BY age ASC` will sort the data by age in ascending order.

2. Group: The `GROUP BY` command can be used to group the data based on a particular column. For example, `GROUP BY gender` will group the data by gender.

3. Join: The `JOIN` command can be used to join two or more datasets based on a common column. For example, `JOIN A BY id, B BY id` will join the datasets A and B based on the id column.

4. Project: The `FOREACH` command can be used to project only the required columns from the dataset. For example, `FOREACH data GENERATE name, age` will select only the name and age columns from the dataset.

5. Filter: The `FILTER` command can be used to filter the data based on a particular condition. For example, `FILTER age > 18` will filter out all the records where the age is less than or equal to 18.

These Pig Latin commands can be combined to perform complex data analysis tasks. By using these commands, you can process large datasets more efficiently and get the desired output in a shorter amount of time.