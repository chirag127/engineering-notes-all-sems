### Interface Servlet and the Servlet Life Cycle in Servlets

The Servlet interface is defined in the `javax.servlet` package and declares the methods that all servlets must implement. These methods are:

- `init(ServletConfig config)`: This method is called by the web container to initialize the servlet before it can handle any requests. The `ServletConfig` object passed as a parameter contains the initialization parameters and the servlet context for the servlet .
- `service(ServletRequest request, ServletResponse response)`: This method is called by the web container to process a request from a client and generate a response. The `ServletRequest` and `ServletResponse` objects represent the HTTP request and response messages respectively .
- `destroy()`: This method is called by the web container to terminate the servlet and release its resources. This method is invoked only once when the servlet is unloaded from the server .

The Servlet interface also defines two other methods that are not part of the servlet life cycle, but provide information about the servlet:

- `getServletConfig()`: This method returns the `ServletConfig` object that was passed to the `init` method.
- `getServletInfo()`: This method returns a string containing information about the servlet, such as its name, author, version, etc.

The servlet life cycle can be summarized as follows :

- The web container loads the servlet class and creates an instance of the servlet.
- The web container calls the `init` method to initialize the servlet.
- The web container calls the `service` method to handle requests from clients and generate responses.
- The web container calls the `destroy` method to terminate the servlet and release its resources.

The following code snippet shows an example of a servlet that implements the Servlet interface and prints a message to the response:

```java
import javax.servlet.*;
import java.io.*;

public class MyServlet implements Servlet {

  // The servlet configuration object
  private ServletConfig config;

  // The init method is called by the web container to initialize the servlet
  public void init(ServletConfig config) throws ServletException {
    // Store the servlet configuration object
    this.config = config;
    // Print a message to the console
    System.out.println("Servlet initialized");
  }

  // The service method is called by the web container to process a request and generate a response
  public void service(ServletRequest request, ServletResponse response) throws ServletException, IOException {
    // Set the content type of the response
    response.setContentType("text/html");
    // Get the output stream of the response
    PrintWriter out = response.getWriter();
    // Print a message to the response
    out.println("<h1>Hello from MyServlet</h1>");
    // Close the output stream
    out.close();
  }

  // The destroy method is called by the web container to terminate the servlet and release its resources
  public void destroy() {
    // Print a message to the console
    System.out.println("Servlet destroyed");
  }

  // The getServletConfig method returns the servlet configuration object
  public ServletConfig getServletConfig() {
    return config;
  }

  // The getServletInfo method returns a string containing information about the servlet
  public String getServletInfo() {
    return "MyServlet - A simple servlet example";
  }
}
```