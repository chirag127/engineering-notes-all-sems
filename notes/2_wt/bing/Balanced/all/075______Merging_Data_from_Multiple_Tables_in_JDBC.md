#### Merging Data from Multiple Tables in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- Sometimes, we may need to retrieve data from multiple tables that are related to each other by some common fields or attributes. For example, we may have a table of students, a table of courses, and a table of enrollments, and we want to find out which students are taking which courses.
- To merge data from multiple tables in JDBC, we can use one of the following approaches:

  - **Using SQL joins**: A join is a SQL operation that combines the rows of two or more tables based on a common field or condition. There are different types of joins, such as inner join, outer join, natural join, cross join, etc. Depending on the type of join, we can get different results from the merged tables. For example, an inner join will only return the rows that match in both tables, while an outer join will also include the rows that do not match in either table. To use SQL joins in JDBC, we need to write a SQL query that specifies the join condition and the fields we want to select from the merged tables, and then execute the query using a Statement or PreparedStatement object. We can then use a ResultSet object to iterate over the rows of the merged data. For example, the following code snippet shows how to use an inner join to get the names and courses of the students who are enrolled in some courses:

  ```java
  // Assume we have a Connection object named conn
  String sql = "SELECT s.name, c.title FROM student s INNER JOIN enrollment e ON s.id = e.student_id INNER JOIN course c ON e.course_id = c.id";
  Statement stmt = conn.createStatement();
  ResultSet rs = stmt.executeQuery(sql);
  while (rs.next()) {
    String name = rs.getString("name");
    String title = rs.getString("title");
    System.out.println(name + " is taking " + title);
  }
  rs.close();
  stmt.close();
  ```

  - **Using ResultSet objects**: Another way to merge data from multiple tables in JDBC is to use multiple ResultSet objects, each representing the data from one table, and then combine them in the Java code. For example, we can use one ResultSet object to get the data from the student table, another ResultSet object to get the data from the enrollment table, and another ResultSet object to get the data from the course table. Then, we can use a loop or a map to match the rows from the different tables based on the common fields, such as the student id and the course id. This approach may require more memory and processing time than using SQL joins, but it may also give us more flexibility and control over the merged data. For example, the following code snippet shows how to use multiple ResultSet objects to get the names and courses of the students who are enrolled in some courses:

  ```java
  // Assume we have a Connection object named conn
  String sql1 = "SELECT id, name FROM student";
  String sql2 = "SELECT student_id, course_id FROM enrollment";
  String sql3 = "SELECT id, title FROM course";
  Statement stmt1 = conn.createStatement();
  Statement stmt2 = conn.createStatement();
  Statement stmt3 = conn.createStatement();
  ResultSet rs1 = stmt1.executeQuery(sql1);
  ResultSet rs2 = stmt2.executeQuery(sql2);
  ResultSet rs3 = stmt3.executeQuery(sql3);
  // Create a map to store the student names by id
  Map<Integer, String> studentMap = new HashMap<>();
  while (rs1.next()) {
    int id = rs1.getInt("id");
    String name = rs1.getString("name");
    studentMap.put(id, name);
  }
  // Create a map to store the course titles by id
  Map<Integer, String> courseMap = new HashMap<>();
  while (rs3.next()) {
    int id = rs3.getInt("id");
    String title = rs3.getString("title");
    courseMap.put(id, title);
  }
  // Loop through the enrollment table and match the student and course ids
  while (rs2.next()) {
    int studentId = rs2.getInt("student_id");
    int courseId = rs2.getInt("course_id");
    String name = studentMap.get(studentId);
    String title = courseMap.get(courseId);
    System.out.println(name + " is taking " + title);
  }
  rs1.close();
  rs2.close();
  rs3.close();
  stmt1.close();
  stmt2.close