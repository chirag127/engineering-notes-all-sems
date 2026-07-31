### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code.
- A registration form is a web page that collects user information and stores it in a database or a cache.
- To create a registration form in JSP, you need to have a table in the database that can store the user details. You also need to have a JSP file that contains the HTML code for the form and the Java code for the database connection and insertion.
- Here are the steps to create a registration form in JSP:

  1. Create a table in the database that can store the user details. For example, you can use the following SQL statement to create a table named user432 in the Oracle database:

  ```sql
  CREATE TABLE "USER432" (
    "NAME" VARCHAR2 (4000),
    "EMAIL" VARCHAR2 (4000),
    "PASS" VARCHAR2 (4000)
  )
  ```

  2. Create a JSP file that contains the HTML code for the registration form and the Java code for the database connection and insertion. For example, you can name the file as index.jsp and write the following code:

  ```jsp
  <%@ page import="java.sql.*" %>
  <html>
  <head>
  <title>Registration Form</title>
  </head>
  <body>
  <h1>Registration Form</h1>
  <form action="process.jsp">
  <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
  <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
  <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
  <input type="submit" value="register"/>
  </form>
  </body>
  </html>
  ```

  3. Create another JSP file that contains the Java code for processing the user input and inserting it into the database. For example, you can name the file as process.jsp and write the following code:

  ```jsp
  <%@ page import="java.sql.*" %>
  <%
  String name=request.getParameter("uname");
  String email=request.getParameter("uemail");
  String pass=request.getParameter("upass");
  try{
    Class.forName("oracle.jdbc.driver.OracleDriver");
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
    PreparedStatement ps=con.prepareStatement("insert into user432 values(?,?,?)");
    ps.setString(1,name);
    ps.setString(2,email);
    ps.setString(3,pass);
    int i=ps.executeUpdate();
    if(i>0){
      out.println("You are successfully registered");
    }
    else{
      out.println("Registration failed");
    }
  }
  catch(Exception e){
    e.printStackTrace();
  }
  %>
  ```

  4. Save the JSP files in the webapps folder of the Tomcat server and run the server.
  5. Open the browser and enter the URL of the index.jsp file. For example, http://localhost:8080/index.jsp
  6. Fill the registration form with the user details and click on the register button. The process.jsp file will execute and insert the user details into the database. It will also display a message indicating the success or failure of the registration.
  7. Repeat the steps 6 for 3 or 4 users who register with the web site. You can check the database table to verify the insertion of the user details.