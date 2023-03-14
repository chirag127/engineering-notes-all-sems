### Handling HTTP get Requests in Servlets

- HTTP GET requests are used to request information from a web server, such as a web page or a file.
- To handle HTTP GET requests in a servlet, you need to extend the HttpServlet class and override the doGet() method.
- The doGet() method takes two parameters: HttpServletRequest and HttpServletResponse, which represent the request and the response objects respectively.
- The HttpServletRequest object provides methods to access the request information, such as the query string, the headers, the cookies, and the parameters.
- The HttpServletResponse object provides methods to set the response information, such as the status code, the headers, the cookies, and the content.
- The doGet() method can also handle HTTP HEAD requests, which are similar to GET requests but only return the headers and not the content.
- To write the content of the response, you can use the PrintWriter object obtained from the getWriter() method of the HttpServletResponse object.
- You can also use the ServletOutputStream object obtained from the getOutputStream() method of the HttpServletResponse object, but you cannot use both at the same time.
- You should set the content type of the response using the setContentType() method of the HttpServletResponse object before writing the content.
- You should also handle any exceptions that may occur while processing the request or writing the response, and send an appropriate error message or status code.

Here is an example of a servlet that handles HTTP GET requests and returns a simple HTML page:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Hello")
public class HelloServlet extends HttpServlet {
  private static final long serialVersionUID = 1L;

  public HelloServlet() {
    super();
  }

  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Set the content type of the response
    response.setContentType("text/html");

    // Get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    // Write the HTML content
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Hello Servlet</title>");
    out.println("</head>");
    out.println("<body>");
    out.println("<h1>Hello, world!</h1>");
    out.println("</body>");
    out.println("</html>");

    // Close the PrintWriter object
    out.close();
  }
}
```