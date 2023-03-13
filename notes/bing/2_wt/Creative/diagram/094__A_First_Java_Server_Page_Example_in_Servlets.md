A Java Server Page (JSP) is a web page that contains Java code embedded in HTML tags. The JSP is compiled and executed by a Java servlet container, which is a component of a web server that supports Java servlets. A servlet is a Java class that handles HTTP requests and generates dynamic web content.

A simple JSP example is a web page that displays the current date and time. The JSP code uses a scriptlet tag (<% and %>) to insert Java code that calls the java.util.Date class and prints the date and time using the out object, which is an implicit JSP object that represents the output stream.

The following diagram illustrates the basic architecture of a JSP and servlet example:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Web Browser   |       |   Web Server    |       |   Servlet       |
|                 |       |                 |       |   Container     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |  HTTP Request        |                       |
       |--------------------->|                       |
       |                       |                       |
       |                       |  JSP Compilation     |
       |                       |--------------------->|
       |                       |                       |
       |                       |  Servlet Execution   |
       |                       |--------------------->|
       |                       |                       |
       |                       |  Dynamic Web Content |
       |  HTTP Response       |<---------------------|
       |<---------------------|                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       V                       V                       V
```