 Here is the formal content written in Markdown format without any emojis or external links:

#### CO 5 Examine various SQL queries from MySQL database K4, K5

1. **SELECT QUERY**: Used to retrieve data from the database. It can retrieve all the columns or few specific columns. Some examples:

- SELECT * FROM table_name; - Retrieves all (*) columns from a table
- SELECT column1, column2 FROM table_name; - Retrieves specific columns from a table
- SELECT DISTINCT column1 FROM table_name; - Retrieves only distinct (different) values from a column

2. **WHERE CLAUSE**: Used to filter the records/rows from a database table. It extracts only those records that fulfill a specified condition. Some examples:

- SELECT * FROM table_name WHERE column_name = value; - Retrieves rows where a specific column matches a particular value
- SELECT * FROM table_name WHERE column_name <> value; - Retrieves rows where a specific column does not match a particular value
- SELECT * FROM table_name WHERE column_name > value; - Retrieves rows where a specific column is greater than a particular value

3. **GROUP BY CLAUSE**: Used to group the result-set by one or more columns. It is often used with aggregate functions like COUNT, MAX, MIN, SUM, AVG etc. Example:

- SELECT column_name, aggregate_function(column_name) FROM table_name GROUP BY column_name;

4. **ORDER BY CLAUSE**: Used to sort the result-set in ascending or descending order according to one or more columns. Example:

- SELECT * FROM table_name ORDER BY column1, column2; - Sorts the records according to column1 and then column2 (both in ascending order)
- SELECT * FROM table_name ORDER BY column1 DESC, column2 ASC; - Sorts the records according to column1 in descending order and column2 in ascending order