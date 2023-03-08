### Aggregating data using group function

Aggregating data using group function is an essential concept in SQL that enables us to perform calculations on a set of values and return a single value as output. This feature is particularly useful when we need to summarize or analyze data in more detail. In this section, we will discuss the group functions available in Oracle/MySQL and how to use them.

#### Group functions

There are five group functions available in Oracle/MySQL, which are as follows:

- `COUNT`: This function returns the number of rows in a table, including NULL values.
- `SUM`: This function returns the sum of values in a specified column.
- `AVG`: This function returns the average of values in a specified column.
- `MAX`: This function returns the maximum value in a specified column.
- `MIN`: This function returns the minimum value in a specified column.

#### Syntax

The syntax for using group functions is as follows:

```sql
SELECT function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name;
```

In the above syntax, `function` is the group function we want to use, `column_name` is the column on which we want to perform the calculation, `table_name` is the name of the table, and `condition` is an optional clause that specifies any conditions that the rows must meet to be included in the calculation. The `GROUP BY` clause is used to group the data by the specified column.

#### Examples

Let's look at some examples to see how group functions work.

Suppose we have a table named `employee` with the following data:

| id | name | department | salary |
|----|------|------------|--------|
| 1  | John | HR         | 5000   |
| 2  | Jane | IT         | 6000   |
| 3  | Mark | IT         | 7000   |
| 4  | Mary | HR         | 5500   |
| 5  | Jack | IT         | 6500   |

If we want to find the total number of employees in each department, we can use the `COUNT` function as follows:

```sql
SELECT department, COUNT(*)
FROM employee
GROUP BY department;
```

This will give us the following output:

| department | COUNT(*) |
|------------|----------|
| HR         | 2        |
| IT         | 3        |

If we want to find the average salary of employees in each department, we can use the `AVG` function as follows:

```sql
SELECT department, AVG(salary)
FROM employee
GROUP BY department;
```

This will give us the following output:

| department | AVG(salary) |
|------------|-------------|
| HR         | 5250        |
| IT         | 6500        |

#### Advantages

- Group functions allow us to perform calculations on a set of data and return a single value as output.
- They can be used to summarize or analyze data in more detail.
- They are easy to use and can be applied to any column in a table.

#### Disadvantages

- Group functions can be computationally expensive, especially when dealing with large datasets.
- They can only be used to perform simple calculations and do not allow for complex analysis.

#### Conclusion

Group functions are a powerful feature in SQL that allow us to perform calculations on a set of data and return a single value as output. By using these functions, we can summarize and analyze data in more detail, which is essential in database management.