#### A First Java Server Page Example in Servlets

A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic content. A JSP can also use Java Servlets, which are Java classes that handle HTTP requests and responses. A JSP can invoke a servlet by using a special tag called `<jsp:include>` that specifies the servlet's URL.

Here is an example of a simple JSP that displays the current date and time by using a servlet called `DateServlet`:

```html
<html>
<head>
<title>A Simple JSP Example</title>
</head>
<body>
<h1>A Simple JSP Example</h1>
<p>The current date and time is:</p>
<!-- This tag includes the output of the DateServlet -->
<jsp:include page="/DateServlet" />
</body>
</html>
```

The `DateServlet` is a Java class that extends the `HttpServlet` class and overrides the `doGet` method to write the date and time to the response output stream:

```java
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class DateServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Set the content type to text/html
    response.setContentType("text/html");

    // Get the output stream to write the response
    PrintWriter out = response.getWriter();

    // Get the current date and time
    Date date = new Date();

    // Write the date and time to the output stream
    out.println("<p>" + date.toString() + "</p>");
  }
}
```

To run this example, we need to have a web server that supports JSP and servlets, such as Apache Tomcat. We also need to compile the `DateServlet` class and place it in the `WEB-INF/classes` directory of the web application. We also need to register the servlet in the `WEB-INF/web.xml` file by using the `<servlet>` and `<servlet-mapping>` tags:

```xml
<web-app>
  <servlet>
    <servlet-name>DateServlet</servlet-name>
    <servlet-class>DateServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>DateServlet</servlet-name>
    <url-pattern>/DateServlet</url-pattern>
  </servlet-mapping>
</web-app>
```

Finally, we need to place the JSP file in the web application's root directory and access it from a web browser. The browser will send a request to the web server, which will invoke the JSP and the servlet, and send back the generated HTML content to the browser. The browser will display the current date and time as shown below:

![A Simple JSP Example](https://i.imgur.com/9X0Yf0g.png)