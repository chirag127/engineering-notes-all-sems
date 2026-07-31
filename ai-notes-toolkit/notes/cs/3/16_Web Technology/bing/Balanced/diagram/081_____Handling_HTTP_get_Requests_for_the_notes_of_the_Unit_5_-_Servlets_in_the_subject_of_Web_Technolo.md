### Handling HTTP get Requests

- HTTP get requests are used to retrieve data from a server based on the parameters specified in the request URL.
- To handle HTTP get requests in a servlet, you need to extend the `HttpServlet` class and override the `doGet` method.
- The `doGet` method takes two parameters: `HttpServletRequest` and `HttpServletResponse`, which represent the request and response objects respectively.
- The `HttpServletRequest` object provides methods to access the request information, such as the query string, the headers, the cookies, the parameters, etc.
- The `HttpServletResponse` object provides methods to set the response information, such as the status code, the headers, the cookies, the content type, the output stream, etc.
- The `doGet` method can also handle HTTP head requests, which are similar to get requests but only return the response headers and not the body.
- The `doGet` method can throw an `IOException` or a `ServletException`, which need to be handled or declared in the method signature.
- The `doGet` method can also call other methods of the `HttpServlet` class, such as `service`, `init`, `destroy`, etc., to perform common tasks or lifecycle operations.
- The `doGet` method can also call methods of the `GenericServlet` class or the `Servlet` interface, which are the superclasses or the superinterface of the `HttpServlet` class.
- The `doGet` method can also use the `ServletContext` or the `ServletConfig` objects, which are available through the `getServletContext` or the `getServletConfig` methods of the `HttpServlet` class, to access the servlet context or the servlet configuration information.

Here is an example of a servlet that handles HTTP get requests:

```java
import javax.servlet.http.*;
import javax.servlet.*;
import java.io.*;

public class WelcomeServlet extends HttpServlet {
  // override the doGet method to handle HTTP get requests
  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException, ServletException {
    // set the content type of the response
    response.setContentType("text/html");
    // get the output stream of the response
    PrintWriter out = response.getWriter();
    // write the HTML content to the output stream
    out.println("<html>");
    out.println("<head><title>Welcome</title></head>");
    out.println("<body>");
    out.println("<h1>Welcome to the Servlet World</h1>");
    out.println("</body>");
    out.println("</html>");
    // close the output stream
    out.close();
  }
}
```