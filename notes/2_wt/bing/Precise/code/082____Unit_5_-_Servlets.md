## Unit 5 - Servlets

A servlet is a Java program that runs on a web server and handles HTTP requests and responses. Here is an example of a simple servlet that responds to a GET request with a "Hello, World!" message:

```java
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloWorldServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        response.getWriter().println("<h1>Hello, World!</h1>");
    }
}
```

This servlet extends the `HttpServlet` class, which provides methods for handling HTTP requests. The `doGet` method is called when the servlet receives a GET request. In this example, the servlet sets the content type of the response to "text/html" and writes a "Hello, World!" message to the response using the `getWriter` method of the `HttpServletResponse` object.
