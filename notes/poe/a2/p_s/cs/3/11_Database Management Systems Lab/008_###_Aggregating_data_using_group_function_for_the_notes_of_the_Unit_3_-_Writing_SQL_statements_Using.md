 Here is the content in markdown format for the given topic:

### Aggregating data using group function

Group functions are used to aggregate data from multiple rows into a single row. Some commonly used group functions are:

- COUNT(): Returns the number of rows that matches a specified criteria.
- SUM(): Returns the total sum of a numeric column.
- AVG(): Returns the average of a numeric column.
- MIN(): Returns the minimum value of a column.
- MAX(): Returns the maximum value of a column.

**Syntax:**
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name;

**Example:**
SELECT department, COUNT(employee_id)
FROM employees
GROUP BY department;

This will return the number of employees in each department.

**Advantages:**
- Reduces the number of rows in the result set and makes the output more readable.
- Useful for data analysis to get summary information from the table.

**Disadvantages:**
- Group functions ignore NULL values while calculating the results.
- Cannot be used in WHERE clause. Must be used in SELECT and HAVING clause.

**Applications:**
- Calculate total sales, average sale, maximum and minimum sales of a product.
- Count the number of students in each grade level.
- Find the most and least populated city.

[Detailed diagrams and codes can be added here for more clarity]

The content summarizes the key points about group functions including syntax, example, advantages, disadvantages and applications. The points are written in a formal tone with headers for easy identification. Additional details can be added as diagrams and codes for enhanced learning. Please let me know if you would like me to modify or expand the answer.