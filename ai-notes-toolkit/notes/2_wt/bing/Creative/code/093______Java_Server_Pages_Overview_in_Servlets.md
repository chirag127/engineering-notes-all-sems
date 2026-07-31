#### Java Server Pages Overview in Servlets

JavaServer Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets. JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension .

JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines. Servlets are Java classes that implement the javax.servlet.Servlet interface and run on the server. Servlets can process requests from clients, perform relevant logic, and send back responses.

The following code snippet shows a simple JSP page that prints the current date and time:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

The following code snippet shows a simple servlet that handles a GET request and forwards it to the JSP page:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // perform some logic here
        request.setAttribute("message", "Hello from servlet!");
        // forward the request to the JSP page
        request.getRequestDispatcher("hello.jsp").forward(request, response);
    }
}
```

The following code snippet shows how to access the request attribute in the JSP page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1><%= request.getAttribute("message") %></h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

JSP pages and servlets are built on top of the Java Servlets API, so they have access to all the powerful Enterprise Java APIs, including JDBC, JNDI, EJB, JAXP, etc. JSP pages and servlets are also compatible with various web frameworks, such as Spring MVC, Struts, JSF, etc.