### Interface Servlet and the Servlet Life Cycle in Servlets

The Servlet interface is defined in the `javax.servlet` package and declares the methods that all servlets must implement. These methods are:

- `init(ServletConfig config)`: This method is called by the web container to initialize the servlet before it can handle any requests. The `ServletConfig` object passed as a parameter contains the initialization parameters and the servlet context for the servlet .
- `service(ServletRequest request, ServletResponse response)`: This method is called by the web container to handle each request that comes to the servlet. The `ServletRequest` and `ServletResponse` objects represent the communication between the client and the server .
- `destroy()`: This method is called by the web container to terminate the servlet and release its resources. This method is invoked only once, when the servlet is taken out of service .

The servlet life cycle consists of the following stages :

- Servlet is loaded: The web container loads the servlet class when it receives a request for the servlet or when the servlet is configured to load on startup.
- Servlet is initialized: The web container calls the `init` method of the servlet to initialize it. This method is invoked only once, when the servlet is loaded for the first time.
- Servlet is ready to service: The servlet is now ready to handle any requests that come to it. The web container calls the `service` method of the servlet for each request.
- Servlet is servicing: The servlet processes the request and generates a response. The web container sends the response back to the client.
- Servlet is not ready to service: The servlet is no longer available to handle requests. This may happen when the web container is shutting down or when the servlet is unloaded due to inactivity or configuration changes.
- Servlet is destroyed: The web container calls the `destroy` method of the servlet to terminate it and release its resources.

The following code snippet shows an example of a servlet that implements the Servlet interface and prints a message to the response:

```java
import javax.servlet.*;
import java.io.*;

public class MyServlet implements Servlet {

  // The servlet config object
  private ServletConfig config;

  // The init method
  public void init(ServletConfig config) throws ServletException {
    // Store the config object
    this.config = config;
    // Print a message to the console
    System.out.println("Servlet initialized");
  }

  // The service method
  public void service(ServletRequest request, ServletResponse response) throws ServletException, IOException {
    // Get the output stream of the response
    PrintWriter out = response.getWriter();
    // Set the content type of the response
    response.setContentType("text/html");
    // Print a message to the response
    out.println("<h1>Hello from MyServlet</h1>");
    // Close the output stream
    out.close();
  }

  // The destroy method
  public void destroy() {
    // Print a message to the console
    System.out.println("Servlet destroyed");
  }

  // The getServletConfig method
  public ServletConfig getServletConfig() {
    // Return the config object
    return config;
  }

  // The getServletInfo method
  public String getServletInfo() {
    // Return some information about the servlet
    return "MyServlet - A simple servlet example";
  }
}
```