#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic content for the client side.
- A JSP can be used to display the current date, for example, by using the special tags `<%` and `%>` to enclose the Java code .
- The following is an example of a simple JSP that displays the current date:

```jsp
<html>
<head>
<title>Current Date</title>
</head>
<body>
<h1>Current Date</h1>
<p>The current date is: <% out.println(new java.util.Date()); %></p>
</body>
</html>
```

- The JSP is compiled into a servlet by the web container when it is first requested by a client. The servlet is then executed and the output is sent back to the client as HTML.
- A servlet is a Java class that extends the `javax.servlet.http.HttpServlet` class and overrides the `doGet` or `doPost` methods to handle HTTP requests from clients.
- The following is an example of a servlet that displays the current date:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.*;

public class CurrentDateServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Set the content type and character encoding
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream
    PrintWriter out = response.getWriter();

    // Write the HTML document
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Current Date</title>");
    out.println("</head>");
    out.println("<body>");
    out.println("<h1>Current Date</h1>");
    out.println("<p>The current date is: " + new Date() + "</p>");
    out.println("</body>");
    out.println("</html>");
  }
}
```

- A JSP is easier to write and maintain than a servlet, as it allows the separation of presentation and logic. A JSP can also use JavaBeans, custom tags, and expression language to simplify the code.
- A servlet is more efficient and scalable than a JSP, as it is compiled only once and can handle multiple requests concurrently. A servlet can also use filters, listeners, and annotations to enhance its functionality.
- A JSP and a servlet can work together to create a web application. A JSP can invoke a servlet to perform some business logic and then display the results. A servlet can forward or redirect a request to a JSP to generate the view.