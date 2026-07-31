# Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code.
- A registration form is a web page that allows users to enter their personal information and create an account on a website.
- To write a JSP that inserts the details of the users who register with the website, we need to follow these steps:

  - Create a database table to store the user details, such as name, email, password, etc. For example, we can use Oracle database and create a table named user432 with the following command:

    ```sql
    CREATE TABLE "USER432" (
      "NAME" VARCHAR2 (4000),
      "EMAIL" VARCHAR2 (4000),
      "PASS" VARCHAR2 (4000)
    )
    ```

  - Create a JSP page that displays the registration form with the input fields for the user details. For example, we can name the JSP page as index.jsp and write the following code:

    ```html
    <form action="process.jsp">
      <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
      <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
      <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
      <input type="submit" value="register"/>
    </form>
    ```

  - Create another JSP page that processes the user input and inserts the user details into the database table. For example, we can name the JSP page as process.jsp and write the following code:

    ```java
    <%@ page import="java.sql.*" %>
    <%
      //Get the user input from the request object
      String name = request.getParameter("uname");
      String email = request.getParameter("uemail");
      String pass = request.getParameter("upass");

      //Create a connection to the database using JDBC and ODBC
      Class.forName("oracle.jdbc.driver.OracleDriver");
      Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");

      //Create a statement object to execute SQL queries
      Statement st = con.createStatement();

      //Insert the user details into the user432 table
      int i = st.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");

      //Check if the insertion is successful
      if(i>0){
        //Display a success message
        out.println("You are successfully registered");
      }
      else{
        //Display an error message
        out.println("Registration failed");
      }

      //Close the connection and statement objects
      st.close();
      con.close();
    %>
    ```

  - Run the index.jsp page on a web server, such as Tomcat, and fill the registration form with the user details. For example, we can enter the following details for three users:

    | Name  | Email             | Password |
    | ----- | ----------------- | -------- |
    | Alice | alice@example.com | 1234     |
    | Bob   | bob@example.com   | 5678     |
    | Carol | carol@example.com | 9012     |

  - Click the register button and see the result of the process.jsp page. For example, we can see the following output:

    ```
    You are successfully registered
    ```

  - Check the database table and see the inserted user details. For example, we can see the following records in the user432 table:

    | NAME  | EMAIL             | PASS |
    | ----- | ----------------- | ---- |
    | Alice | alice@example.com | 1234 |
    | Bob   | bob@example.com   | 5678 |
    | Carol | carol@example.com | 9012 |

- This is how we can write a JSP that inserts the details of the users who register with the website by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab.