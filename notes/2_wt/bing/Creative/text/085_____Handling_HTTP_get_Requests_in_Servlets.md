### Handling HTTP get Requests in Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can handle different types of HTTP requests, such as GET, POST, PUT, DELETE, etc. by overriding the corresponding methods of the `javax.servlet.http.HttpServlet` class.
- The `doGet` method is used to handle HTTP GET requests, which are typically used to request information from the server or to send query parameters.
- The `doGet` method has two parameters: `HttpServletRequest request` and `HttpServletResponse response`. These objects represent the incoming request and the outgoing response, respectively.
- The `request` object provides methods to access the request information, such as the request URI, the query string, the headers, the cookies, the parameters, etc.
- The `response` object provides methods to set the response information, such as the status code, the headers, the cookies, the content type, the output stream, etc.
- To handle an HTTP GET request, the servlet should perform the following steps:
  - Obtain the request information from the `request` object and process it as needed.
  - Set the response information using the `response` object, such as the content type, the headers, the cookies, etc.
  - Write the response content to the output stream using the `response.getWriter()` or `response.getOutputStream()` methods.
  - Close the output stream and flush the buffer.
- The following code snippet shows an example of a servlet that handles HTTP GET requests and returns a simple HTML page:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
    // Get the name parameter from the request
    String name = request.getParameter("name");
    if (name == null) {
      name = "World";
    }

    // Set the content type and the character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream and write the response content
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Hello Servlet</title>");
    out.println("</head>");
    out.println("<body>");
    out.println("<h1>Hello, " + name + "!</h1>");
    out.println("</body>");
    out.println("</html>");

    // Close the output stream and flush the buffer
    out.close();
  }
}
```