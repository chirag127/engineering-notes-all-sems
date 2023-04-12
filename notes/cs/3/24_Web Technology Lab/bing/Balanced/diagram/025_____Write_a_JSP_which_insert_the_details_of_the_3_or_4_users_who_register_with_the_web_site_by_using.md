### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code and HTML tags.
- JSP can connect to a database using JDBC (Java Database Connectivity) or ODBC (Open Database Connectivity) drivers, which are APIs that enable communication between Java applications and various data sources.
- JSP can also use session tracking API, which is a mechanism that allows maintaining state information across multiple requests from the same client.
- To create a registration form in JSP, we need to have a table in the database that can store the user details, such as name, email, password, etc.
- We also need to have two JSP files: one for displaying the form and another for processing the form data and inserting it into the database.
- The following steps can be followed to write a JSP that can insert the details of the users who register with the web site:

1. Create a table in the database that can store the user details. For example, we can use the Oracle database and create a table named user432 with the following command:

```sql
CREATE TABLE "USER432" (
  "NAME" VARCHAR2 (4000),
  "EMAIL" VARCHAR2 (4000),
  "PASS" VARCHAR2 (4000)
)
```

2. Create a JSP file named index.jsp that can display the registration form. The form should have input fields for name, email, and password, and a submit button that can send the form data to another JSP file named process.jsp. The form can look like this:

```html
<form action="process.jsp">
  <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
  <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
  <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
  <input type="submit" value="register"/>
</form>
```

3. Create a JSP file named process.jsp that can process the form data and insert it into the database. The file should have the following steps:

  - Import the necessary packages for JDBC or ODBC and session tracking API.
  - Get the form data from the request object using the getParameter() method.
  - Establish a connection to the database using the DriverManager class and the getConnection() method. Provide the appropriate driver name, URL, username, and password for the database.
  - Create a statement object using the createStatement() method of the connection object.
  - Execute an SQL insert query using the executeUpdate() method of the statement object. Provide the table name and the form data as the values to be inserted.
  - Close the statement and connection objects using the close() method.
  - Create a session object using the getSession() method of the request object. Set the form data as session attributes using the setAttribute() method of the session object.
  - Display a message to the user that the registration is successful and show the session attributes using the getAttribute() method of the session object.

The process.jsp file can look like this:

```jsp
<%@ page import="java.sql.*,javax.servlet.http.*" %>
<%
  //Get the form data from the request object
  String name=request.getParameter("uname");
  String email=request.getParameter("uemail");
  String pass=request.getParameter("upass");
  
  //Establish a connection to the database
  Class.forName("oracle.jdbc.driver.OracleDriver");
  Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
  
  //Create a statement object
  Statement st=con.createStatement();
  
  //Execute an SQL insert query
  int i=st.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");
  
  //Close the statement and connection objects
  st.close();
  con.close();
  
  //Create a session object
  HttpSession session=request.getSession();
  
  //Set the form data as session attributes
  session.setAttribute("name",name);
  session.setAttribute("email",email);
  session.setAttribute("pass",pass);
  
  //Display a message to the user and show the session attributes
  out.println("

```
