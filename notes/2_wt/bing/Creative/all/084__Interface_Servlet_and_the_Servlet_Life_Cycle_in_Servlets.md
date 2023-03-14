### Interface Servlet and the Servlet Life Cycle in Servlets

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The `Servlet` interface defines the methods that all servlets must implement, such as `init()`, `service()`, `destroy()`, `getServletConfig()` and `getServletInfo()`.
- The servlet life cycle is the sequence of events that occurs from the time the servlet is loaded into the web container until it is unloaded.
- The servlet life cycle consists of the following phases:

  1. **Initialization**: The web container calls the `init()` method of the servlet to initialize it. This method is called only once when the servlet is first loaded. The `init()` method can accept a `ServletConfig` object that contains the initialization parameters and the servlet context for the servlet.
  2. **Request handling**: The web container calls the `service()` method of the servlet to handle each HTTP request that is sent to the servlet. The `service()` method can accept a `HttpServletRequest` object that contains the request information and a `HttpServletResponse` object that contains the response information. The `service()` method can delegate the request to other methods based on the HTTP method, such as `doGet()`, `doPost()`, `doPut()`, etc.
  3. **Termination**: The web container calls the `destroy()` method of the servlet to terminate it. This method is called only once when the servlet is unloaded from the web container. The `destroy()` method can perform any cleanup operations before the servlet is destroyed.

- A mnemonic to remember the servlet life cycle methods is **I See Dogs**:

  - **I**nit
  - **S**ervice
  - **D**estroy

- A diagram to illustrate the servlet life cycle is:

```
  +-----------------+       +-----------------+       +-----------------+
  | Web Container   |       | Web Container   |       | Web Container   |
  |                 |       |                 |       |                 |
  | +-------------+ |       | +-------------+ |       | +-------------+ |
  | | Servlet     | |       | | Servlet     | |       | | Servlet     | |
  | |             | |       | |             | |       | |             | |
  | | init()      | |       | | service()   | |       | | destroy()   | |
  | +-------------+ |       | +-------------+ |       | +-------------+ |
  +-----------------+       +-----------------+       +-----------------+
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         |                         |   |                      |
         +------------------------>+   +<---------------------+
                Initialization             Termination
```

- An example of a servlet that implements the `Servlet` interface and prints a message to the response is:

```java
import java.io.*;
import javax.servlet.*;

public class HelloServlet implements Servlet {

  // The servlet configuration object
  private ServletConfig config;

  // The init method is called by the web container to initialize the servlet
  public void init(ServletConfig config) throws ServletException {
    // Store the servlet configuration object
    this.config = config;
    // Print a message to the console
    System.out.println("HelloServlet initialized");
  }

  // The service method is called by the web container to handle each request
  public void service(ServletRequest request, ServletResponse response) throws ServletException, IOException {
    // Set the content type of the response
    response.setContentType("text/html");
    // Get the output stream of the response
    PrintWriter out = response.getWriter();
    // Print a message to the response
    out.println("<h1>Hello, world!</h1>");
    // Close the output stream
    out.close();
  }

  // The destroy method is called by the web container to terminate the servlet
  public void destroy() {
    // Print a message to the console
    System.out.println("HelloServlet destroyed");
  }

  // The getServletConfig method returns the servlet configuration object
  public ServletConfig getServletConfig() {
    return config;
  }

  // The getServletInfo method returns some information about the servlet
  public String getServletInfo() {
    return "A simple servlet that says hello";