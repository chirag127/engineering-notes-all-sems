 Here is the content in markdown format:

### Create MS Access Database

1. Open MS Access application
2. Click on **Blank database** to create a new database
3. Enter the file name for the database and click **Create**
4. A new database will be created with a table called Table1. Rename the table to an appropriate name, e.g. `Student`
5. Add fields to the table, e.g. `StudentID`, `Name`, `Course`, `Fees`
6. Enter sample data records in the table
7. Save the database

Thus, an MS Access database is created with a table and sample data.

### Create an ODBC link

1. Open the **ODBC Data Source Administrator** control panel
2. Go to the **System DSN** tab and click **Add...**
3. Select **Microsoft Access Driver (*.mdb, *.accdb)** and click **Finish**
4. Enter a Data Source Name, e.g. `AccessDB`
5. Click **Select...** and choose the MS Access database file
6. Click **OK**

Thus, an ODBC connection is created to the MS Access database which can be used to connect from other applications.

### Compile & execute JAVA JDVC Socket

1. Import JDBC packages - `java.sql.*`
2. Load the JDBC driver - `Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");`
3. Create a connection URL in the format - `jdbc:odbc:<DSN_Name>` where DSN_Name is the ODBC data source name
4. Establish a connection - `conn = DriverManager.getConnection(url);`
5. Create a statement object - `stmt = conn.createStatement();`
6. Execute SQL queries - `rs = stmt.executeQuery("SELECT * FROM Student")`
7. Process the results - `while (rs.next()) { // fetch fields from ResultSet }`
8. Close the connections - `conn.close();`

The JAVA code can be compiled and executed to fetch data from the MS Access database using JDBC-ODBC bridge.