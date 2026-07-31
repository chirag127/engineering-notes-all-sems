 Here is the formal content in Markdown format without any emojis or external links on the topic Aggregate Functions for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Aggregate Functions

1.  COUNT - Returns the number of rows that matches a specified criteria.
    - Syntax: COUNT(column_name)
    - Counts all the rows if no column is specified.
    - Ignores NULL values unless COUNT(DISTINCT column_name) is used.
2.  SUM - Returns the total sum of a numeric column.
    - Syntax: SUM(column_name)
    - Only works on numeric data types.
    - Ignores NULL values.
3.  AVG - Returns the average of a numeric column.
    - Syntax: AVG(column_name)
    - Only works on numeric data types.
    - Ignores NULL values.
4.  MIN - Returns the minimum value of a column.
    - Syntax: MIN(column_name)
    - Works on both numeric and character data types.
    - Ignores NULL values.
5.  MAX - Returns the maximum value of a column.
    - Syntax: MAX(column_name)
    - Works on both numeric and character data types.
    - Ignores NULL values.

The above aggregate functions are often used in conjunction with GROUP BY to summarize data.

Hope this helps!