 Here is the formal content written in Markdown format without any emojis or external links:

#### Joining in JDBC

1. Inner join: Returns records that have matching values in both tables.
2. Left outer join: Returns all records from the left table, and the matched records from the right table.
3. Right outer join: Returns all records from the right table, and the matched records from the left table.
4. Full outer join: Returns all records when there is a match in either left or right table.

To perform a join in JDBC:

1. Create statements for both tables specifying the join condition in the WHERE clause.
2. Create a ResultSet for the join statement.
3. Use ResultSet methods such as getString() to retrieve the data from the joined tables.

The key points to keep in mind when joining are:

1. Ensure the JOIN column names are same in both tables.
2. Clearly specify the JOIN type - INNER, LEFT OUTER etc.
3. Use aliases if the column names are ambiguous.
4. Filter the results using WHERE clause if required.