 Here is the content in markdown format without any feeling or friendliness:

### Design and implement a simple servlet book query with the help of JDBC & SQL

1. Import the required packages - `import java.sql.*;`
2. Register the driver - `Class.forName("com.mysql.jdbc.Driver");`
3. Create a connection - `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");`
4. Create a statement object - `Statement st = con.createStatement();`
5. Execute the SQL query - `ResultSet rs = st.executeQuery("select * from books");`
6. Process the results -
```
while (rs.next()) {
    String bookName = rs.getString("book_name");
    //Display book name
}
```
7. Close all the connections - `con.close(); st.close(); rs.close();`

The servlet will make use of the JDBC APIs to connect to the database, execute the SQL query to fetch book details and display them. No emotions or external links are included. The content is written in markdown format as per the given instructions.