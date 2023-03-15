### Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines five methods that correspond to the different phases of a servlet's life cycle:
  - `init(ServletConfig config)`: This method is invoked by the servlet container when the servlet is loaded into memory, usually in response to the first request that the servlet receives. The `ServletConfig` object passed as a parameter contains initialization parameters and a reference to the servlet context. The `init` method can be used to perform any one-time tasks, such as opening database connections or reading configuration files .
  - `service(ServletRequest request, ServletResponse response)`: This method is invoked by the servlet container for each request that the servlet receives. The `ServletRequest` and `ServletResponse` objects passed as parameters represent the HTTP request and response objects, respectively. The `service` method can be used to process the request, generate dynamic content, and send the response back to the client .
  - `destroy()`: This method is invoked by the servlet container when the servlet is unloaded from memory, usually when the web server is shut down or the servlet is removed from the web application. The `destroy` method can be used to perform any cleanup tasks, such as closing database connections or releasing resources .
  - `getServletConfig()`: This method returns the `ServletConfig` object that was passed to the `init` method. It can be used to access the initialization parameters and the servlet context.
  - `getServletInfo()`: This method returns a string that contains information about the servlet, such as its name, version, and author. It can be used to provide metadata about the servlet.
- The servlet life cycle can be summarized as follows:
  - The servlet is born when the servlet container loads it into memory.
  - The servlet is initialized when the servlet container invokes the `init` method.
  - The servlet is ready to service when the `init` method completes successfully.
  - The servlet is servicing when the servlet container invokes the `service` method for each request.
  - The servlet is not ready to service when the servlet container decides to unload it from memory, either due to inactivity or low memory.
  - The servlet is destroyed when the servlet container invokes the `destroy` method.
- The following diagram illustrates the servlet life cycle:

```
+----------------+     +----------------+     +----------------+
| Servlet is     |     | Servlet is     |     | Servlet is     |
| born           |     | initialized    |     | ready to       |
|                |     |                |     | service        |
|                |     |                |     |                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |<-----------------+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       +--------------------->+--------------------->+----------------->+
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |
       |                      |                      |                  |<-----------------+
       |                      |                      |                  |                  |
       |                      |                      |                  |                  |
       |