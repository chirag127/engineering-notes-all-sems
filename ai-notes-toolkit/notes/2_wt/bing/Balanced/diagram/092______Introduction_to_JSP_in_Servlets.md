#### Introduction to JSP in Servlets

JSP stands for Java Server Pages. It is a server-side technology that lets you build dynamic web applications that work on any platform. JSP can use all Java APIs, including the JDBC API, which lets them connect to enterprise databases .

Servlets are the Java programs that run on the Java-enabled web server or application server. They are used to handle the request obtained from the web server, process the request, produce the response, then send a response back to the web server.

JSP is an extension to Servlet because it provides more functionality than servlet such as expression language, JSTL, etc. A JSP page consists of HTML tags and JSP tags. JSP is HttpServlet specific, meaning we cannot use JSP for other purposes than to create web applications or more specific dynamic web pages .

The following diagram shows how JSP and Servlet work together to create dynamic web applications:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Browser     |      |    Web Server  |      |    Database    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |  HTTP Request        |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      |  JSP/Servlet Engine  |
       |                      |--------------------->|
       |                      |                      |
       |                      |  JDBC API            |
       |                      |--------------------->|
       |                      |                      |
       |                      |  SQL Query           |
       |                      |--------------------->|
       |                      |                      |
       |                      |  SQL Result          |
       |                      |<---------------------|
       |                      |                      |
       |                      |  JDBC API            |
       |                      |<---------------------|
       |                      |                      |
       |                      |  JSP/Servlet Engine  |
       |                      |<---------------------|
       |                      |                      |
       |  HTTP Response       |                      |
       |<---------------------|                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
```

: https://www.javatpoint.com/jsp-tutorial
: https://www.educba.com/servlet-jsp/
: https://akashmjain.medium.com/introduction-to-jsp-and-servlet-69d31be1b2a6
: https://www.geeksforgeeks.org/introduction-to-jsp/
: https://w3schools.in/jsp/intro
: https://www.geeksforgeeks.org/introduction-java-servlets/