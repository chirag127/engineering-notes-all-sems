# Create MS Access Database, Create on ODBC link, Compile & execute JAVA JDVC Socket

## Create MS Access Database

- To create a database in Microsoft Access, follow these steps  :
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template that suits your needs.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
  - To create tables, queries, forms, reports, and other objects, use the tabs on the ribbon or the navigation pane.

## Create on ODBC link

- To create an ODBC link to connect your MS Access database to other applications, follow these steps :
  - Open the ODBC Data Source Administrator tool on your computer. You can find it in the Control Panel > Administrative Tools > Data Sources (ODBC).
  - Select the User DSN tab, and then click Add.
  - Select the Microsoft Access Driver (*.mdb, *.accdb) from the list of drivers, and then click Finish.
  - Enter a name and a description for the data source, and then click Select.
  - Browse to the location of your MS Access database file, and then click OK.
  - Click OK to save the data source.

## Compile & execute JAVA JDVC Socket

- To compile and execute a Java program that uses JDBC to connect to your MS Access database, follow these steps :
  - Write your Java code that imports the java.sql package and uses the DriverManager class to get a connection to your database. For example:

```java
import java.sql.*;
public class JDBCExample {
  public static void main(String[] args) {
    try {
      // Load the driver
      Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
      // Get the connection
      Connection con = DriverManager.getConnection("jdbc:odbc:YourDataSourceName");
      // Create a statement
      Statement stmt = con.createStatement();
      // Execute a query
      ResultSet rs = stmt.executeQuery("SELECT * FROM YourTableName");
      // Print the results
      while (rs.next()) {
        System.out.println(rs.getString(1) + " " + rs.getString(2));
      }
      // Close the resources
      rs.close();
      stmt.close();
      con.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

  - Save your Java file with a .java extension, such as JDBCExample.java.
  - Open a command prompt and navigate to the folder where your Java file is located.
  - Compile your Java file using the javac command, such as javac JDBCExample.java. This will create a .class file with the same name as your Java file.
  - Execute your Java file using the java command, such as java JDBCExample. This will run your program and display the output on the console.

: Create a database in Access - Access  (https://support.microsoft.com/en-us/office/create-a-database-in-access-f200d95b-e429-4acc-98c1-b883d4e9fc0a)
: Basic tasks for an Access desktop database - Microsoft Support (https://support.microsoft.com/en-us/office/basic-tasks-for-an-access-desktop-database-5ddb8595-497c-4366-8327-ae79d2abdc9c)
: How to Create a Database in Microsoft Access: A Step-by-Step Guide - MUO (https://www.makeuseof.com/how-to-create-database-microsoft-access/)
: How to Connect to MS Access Database in Java Using JDBC (https://www.thoughtco.com/connect-to-ms-access-database-in-java-2033993)
: How to connect to a Microsoft Access database - Apache OpenOffice Wiki (https://wiki.openoffice.org/wiki/Documentation/How_Tos/Connecting_to_Microsoft_Access)
: JDBC - ODBC Bridge Driver Example - Tutorialspoint (https://www.tutorialspoint.com/jdbc/jdbc-odbc-bridge-driver-example.htm)
: Java JDBC MS Access Database Connection Steps - Java Guides (https://www.javaguides.net/2019/08/java-jdbc-ms-access-database-connection-steps.html)