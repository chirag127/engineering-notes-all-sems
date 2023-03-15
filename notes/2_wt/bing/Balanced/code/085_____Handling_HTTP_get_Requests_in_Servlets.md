### Handling HTTP get Requests in Servlets

HTTP get requests are used to retrieve information from a server based on the parameters specified in the URL. To handle HTTP get requests in a servlet, you need to extend the HttpServlet class and override the doGet method. The doGet method takes two parameters: HttpServletRequest and HttpServletResponse, which represent the request and response objects respectively.

The HttpServletRequest object provides methods to access the request information, such as the query string, the headers, the cookies, etc. The HttpServletResponse object provides methods to set the response information, such as the status code, the headers, the content type, etc.

The following code snippet shows an example of a servlet that handles HTTP get requests and displays a welcome message to the user based on the name parameter in the URL.

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class WelcomeServlet extends HttpServlet {

  // Override the doGet method to handle HTTP get requests
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

    // Set the content type of the response to text/html
    response.setContentType("text/html");

    // Get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    // Get the name parameter from the request URL
    String name = request.getParameter("name");

    // If the name parameter is not null, display a welcome message
    if (name != null) {
      out.println("<h1>Welcome, " + name + "!</h1>");
    } else {
      // Otherwise, display a default message
      out.println("<h1>Welcome to my servlet!</h1>");
    }

    // Close the PrintWriter object
    out.close();
  }
}
```