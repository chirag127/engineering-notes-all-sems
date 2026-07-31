A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic HTML content. A servlet is a Java class that handles HTTP requests and responses. A JSP can be converted into a servlet by a JSP engine, which is a component of a web server that supports JSP technology.

A simple example of a JSP that displays the current date is shown below:

```html
<html>
<head>
<title>Current Date</title>
</head>
<body>
<h1>The current date is:</h1>
<%= new java.util.Date() %>
</body>
</html>
```

The JSP engine translates the JSP into a servlet that looks something like this:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class CurrentDate extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException, ServletException
  {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Current Date</title>");
    out.println("</head>");
    out.println("<body>");
    out.println("<h1>The current date is:</h1>");
    out.println(new java.util.Date());
    out.println("</body>");
    out.println("</html>");
  }
}
```

The servlet is then compiled and executed by the web server, which sends the generated HTML content to the client browser.

The following diagram illustrates the process of JSP and servlet execution:

#### A First Java Server Page Example in Servlets

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Client Browser |        |  Web Server     |        |  JSP Engine     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                        |                        |
       |  HTTP request          |                        |
       |----------------------->|                        |
       |                        |                        |
       |                        |  JSP file              |
       |                        |----------------------->|
       |                        |                        |
       |                        |                        |  Servlet file
       |                        |<-----------------------|
       |                        |                        |
       |                        |  Servlet class         |
       |                        |----------------------->|
       |                        |                        |
       |                        |                        |  HTML content
       |                        |<-----------------------|
       |                        |                        |
       |  HTTP response         |                        |
       |<-----------------------|                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
```