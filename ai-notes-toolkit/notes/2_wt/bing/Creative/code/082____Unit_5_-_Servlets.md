## Unit 5 - Servlets

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. Servlets can be used to create dynamic web pages, process user input, communicate with databases, and more.

To create a servlet, you need to:

- Extend the `javax.servlet.http.HttpServlet` class and override its `doGet` or `doPost` methods (or both) to handle GET or POST requests respectively.
- Annotate the servlet class with `@WebServlet` and specify the URL pattern that maps to the servlet.
- Compile the servlet class and place it in the `WEB-INF/classes` directory of your web application.
- Deploy the web application to a web server that supports servlets, such as Tomcat or Jetty.

For example, the following servlet class prints a simple message to the browser:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<h1>Hello, world!</h1>");
  }
}
```

To test the servlet, you can run the web server and access the URL `http://localhost:8080/hello` in your browser. You should see the message "Hello, world!" displayed on the page.