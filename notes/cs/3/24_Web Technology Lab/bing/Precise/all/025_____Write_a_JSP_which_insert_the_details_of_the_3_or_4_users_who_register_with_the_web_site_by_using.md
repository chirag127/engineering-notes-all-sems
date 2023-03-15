# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form

1. Create a registration form in HTML that takes user input for fields such as name, email, password, etc.
2. Set up a database to store user information using JDBC or ODBC.
3. In the JSP file, import the necessary packages for database connectivity and handling.
4. Retrieve the user input from the registration form using `request.getParameter()` method.
5. Use a `PreparedStatement` to insert the user data into the database.
6. Execute the `PreparedStatement` to insert the data into the database.
7. Close the database connection.

Here is an example of a JSP file that inserts user data into a database:

```jsp
<%@ page import="java.sql.*" %>
<%
    String name = request.getParameter("name");
    String email = request.getParameter("email");
    String password = request.getParameter("password");

    Connection conn = null;
    PreparedStatement pstmt = null;

    try {
        Class.forName("com.mysql.jdbc.Driver");
        conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");

        String sql = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)";
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, name);
        pstmt.setString(2, email);
        pstmt.setString(3, password);

        pstmt.executeUpdate();
    } catch (Exception e) {
        out.println(e);
    } finally {
        if (pstmt != null) {
            pstmt.close();
        }
        if (conn != null) {
            conn.close();
        }
    }
%>
```