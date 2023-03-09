### Built-in Functions for the Notes of Unit 5 - Structured Query Language (SQL) in the subject of Basics of Database Management System

Structured Query Language (SQL) is a powerful tool used for managing and manipulating data stored in relational databases. One of the key features of SQL is the use of built-in functions that enable users to perform various operations on data. In this section, we will discuss some of the most commonly used built-in functions in SQL.

#### 1. Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. The most commonly used aggregate functions in SQL are:

- COUNT(): This function returns the number of rows that match a specified condition.
- SUM(): This function returns the sum of a set of values.
- AVG(): This function returns the average of a set of values.
- MIN(): This function returns the minimum value in a set of values.
- MAX(): This function returns the maximum value in a set of values.

#### 2. String Functions

String functions are used to manipulate character strings. The most commonly used string functions in SQL are:

- CONCAT(): This function is used to concatenate two or more strings together.
- SUBSTRING(): This function is used to extract a substring from a larger string.
- LENGTH(): This function returns the length of a string.
- UPPER(): This function converts all characters in a string to uppercase.
- LOWER(): This function converts all characters in a string to lowercase.

#### 3. Date Functions

Date functions are used to manipulate and perform calculations on dates and times. The most commonly used date functions in SQL are:

- NOW(): This function returns the current date and time.
- DATE(): This function extracts the date from a given date/time value.
- YEAR(): This function returns the year from a given date value.
- MONTH(): This function returns the month from a given date value.
- DAY(): This function returns the day of the month from a given date value.

#### Advantages of Built-in Functions

- Built-in functions make it easy to perform various operations on data without the need for complex coding.
- They help to ensure consistency and accuracy in data manipulation.
- Built-in functions can be used to create more complex queries and generate more meaningful output.

#### Disadvantages of Built-in Functions

- Overuse of built-in functions can lead to slower query performance.
- Built-in functions may not always be the most efficient way to manipulate data, especially with large datasets.

#### Examples

Here are some examples of how built-in functions can be used in SQL:

- SELECT COUNT(*) FROM customers; (returns the total number of customers in the database)
- SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees; (returns a list of employees' full names)
- SELECT DATE_FORMAT(order_date, '%m/%d/%Y') AS formatted_date FROM orders; (returns a list of formatted order dates)

#### Applications

Built-in functions are used in a wide range of applications, including:

- Data analysis and reporting
- Business intelligence
- Web development
- Mobile app development

In conclusion, built-in functions are an essential aspect of SQL and play a critical role in data manipulation and analysis. By understanding how to use these functions, users can generate more meaningful output and gain valuable insights into their data.