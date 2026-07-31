A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic HTML content. A JSP can also use Java Servlets, which are Java classes that handle HTTP requests and responses. A JSP can invoke a servlet by using a special tag called <jsp:include> that specifies the servlet's URL.

Here is an example of a simple JSP that displays the current date and time by using a servlet called DateServlet:

#### A First Java Server Page Example in Servlets

```html
<html>
<head>
<title>A Simple JSP Example</title>
</head>
<body>
<h1>A Simple JSP Example</h1>
<p>This is a simple JSP that displays the current date and time by using a servlet.</p>
<jsp:include page="/DateServlet" />
</body>
</html>
```

The DateServlet is a Java class that extends the HttpServlet class and overrides the doGet method. The doGet method writes the current date and time to the response output stream:

```java
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class DateServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Set the content type and charset
    response.setContentType("text/html;charset=UTF-8");

    // Get the output stream
    PrintWriter out = response.getWriter();

    // Get the current date and time
    Date date = new Date();
    String dateString = date.toString();

    // Write the date and time to the output stream
    out.println("<p>The current date and time is: " + dateString + "</p>");
  }
}
```

The JSP and the servlet need to be deployed on a web server that supports JSP and servlets, such as Tomcat. The JSP can be accessed by using the web server's URL and the JSP's file name, for example:

http://localhost:8080/simple.jsp

The output of the JSP will look something like this:

![JSP output](https://i.imgur.com/7fQZ3aD.png)