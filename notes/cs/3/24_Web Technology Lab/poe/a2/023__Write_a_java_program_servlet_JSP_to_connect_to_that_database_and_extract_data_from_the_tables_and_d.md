 Here is the formal content written in Markdown format without any emojis or external links:

### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab.

1. Import the required packages - Import java.sql.* to connect to the database and handle SQL exceptions.
2. Load the driver - Load the driver for the specific database (MySQL, Oracle, etc.) using Class.forName().
3. Get the connection - Get the connection to the database using DriverManager.getConnection() by passing the URL, username and password.
4. Create the statement - Create the Statement or PreparedStatement object to query the database.
5. Execute the query - Execute the SQL query using executeQuery() to get the results or executeUpdate() to modify the data.
6. Process the results - Retrieve the results from the query using ResultSet and display or store them in variables.
7. Close the connection - Finally, close the connection using close() to free up the resources.

The above steps can be implemented in a Java program, servlet or JSP to connect to the database and extract and display the data from the tables for the given notes. Appropriate database credentials and queries must be used to fetch the required data. The extracted data can be displayed in a table format or string format based on the requirements.