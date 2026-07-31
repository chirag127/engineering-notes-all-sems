### Java Program to Extract Data from Database Tables

In this section, we will discuss how to write a Java program or servlet or JSP to connect to a database and extract data from the tables. This is an important topic covered in the Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab.

#### Step 1: Import Required Packages

Before writing the program, we need to import the required packages. The packages required for connecting to the database and extracting data are `java.sql.*` and `javax.servlet.*`.

```java
import java.sql.*;
import javax.servlet.*;
```

#### Step 2: Load the Driver

To connect to the database, we need to load the driver for the respective database. For example, to connect to a MySQL database, we need to load the MySQL driver.

```java
Class.forName("com.mysql.jdbc.Driver");
```

#### Step 3: Establish Connection

After loading the driver, we need to establish a connection to the database using the `getConnection()` method of the `DriverManager` class. We need to pass the database URL, username, and password as parameters to this method.

```java
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/db_name", "username", "password");
```

#### Step 4: Create Statement

Once the connection is established, we can create a statement object using the `createStatement()` method of the `Connection` interface.

```java
Statement stmt = con.createStatement();
```

#### Step 5: Execute Query

After creating the statement object, we can execute the SQL query using the `executeQuery()` method of the `Statement` interface. The result of the query is stored in a `ResultSet` object.

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM table_name");
```

#### Step 6: Display Results

Finally, we can loop through the `ResultSet` object and display the results using the `getString()` or `getInt()` method of the `ResultSet` interface.

```java
while(rs.next()){
    out.print(rs.getInt(1)+" "+rs.getString(2)+" "+rs.getString(3));
}
```

#### Conclusion

In this section, we discussed how to write a Java program or servlet or JSP to connect to a database and extract data from the tables. We covered the steps involved in establishing a connection, creating a statement, executing a query, and displaying the results. This is an important topic that is covered in the Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab.