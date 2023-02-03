### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

Program to Illustrate JDBC Connectivity in Web Technology Lab:

In web technology lab, JDBC (Java Database Connectivity) is a Java API used to connect to databases and perform database operations. JDBC provides a standard way to access databases, and is used to connect to a wide range of databases, including relational databases, NoSQL databases, and cloud databases.

The following is a simple program that illustrates JDBC connectivity in a web technology lab:

```
import java.sql.*;

public class JDBCExample {
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/test";

   static final String USER = "username";
   static final String PASS = "password";

   public static void main(String[] args) {
   Connection conn = null;
   Statement stmt = null;
   try{
      Class.forName("com.mysql.jdbc.Driver");
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);

      System.out.println("Creating statement...");
      stmt = conn.createStatement();
      String sql;
      sql = "SELECT id, first, last, age FROM Employees";
      ResultSet rs = stmt.executeQuery(sql);

      while(rs.next()){
         int id  = rs.getInt("id");
         int age = rs.getInt("age");
         String first = rs.getString("first");
         String last = rs.getString("last");

         System.out.print("ID: " + id);
         System.out.print(", Age: " + age);
         System.out.print(", First: " + first);
         System.out.println(", Last: " + last);
      }
      rs.close();
      stmt.close();
      conn.close();
   }catch(SQLException se){
      se.printStackTrace();
   }catch(Exception e){
      e.printStackTrace();
   }finally{
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }
   }
   System.out.println("Goodbye!");
}
}
```

In this program, the JDBC driver is loaded, and a connection is established with the database using the `DriverManager.getConnection` method. A statement is created using the `conn.createStatement` method, and a SQL query is executed using the `stmt.executeQuery` method. The results of the query are retrieved using the `ResultSet` object, and are displayed on the console.

In conclusion, JDBC is an important component of web technology lab, and is used to connect to databases and perform database operations. The above program illustrates how to use JDBC to connect to a database, execute a SQL query, and retrieve the results of the query.
