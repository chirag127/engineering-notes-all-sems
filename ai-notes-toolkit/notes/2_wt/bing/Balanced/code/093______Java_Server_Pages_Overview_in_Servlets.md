#### Java Server Pages Overview in Servlets

Java Server Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets. JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension .

JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines. Servlets are Java classes that implement the javax.servlet.Servlet interface and run on the server. Servlets can process requests, perform relevant logic, and generate responses.

The following code snippet shows a simple JSP page that prints the current date and time:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Simple JSP Page</title>
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

public class SimpleServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // perform some logic here
        // ...

        // forward the request to the JSP page
        RequestDispatcher dispatcher = request.getRequestDispatcher("/simple.jsp");
        dispatcher.forward(request, response);
    }
}
```

The JSP page and the servlet can communicate using request and response objects, as well as session and application scopes. JSP pages can also use various tags and directives to control the page behavior, such as importing packages, setting page attributes, declaring variables, and including other resources . JSP pages can also use custom tags and expression language to simplify the page development and enhance the readability.