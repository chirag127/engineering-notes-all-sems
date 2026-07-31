### Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines the methods that a servlet must implement to interact with the servlet container and the clients.
- The servlet life cycle refers to the stages that a servlet goes through from its creation to its destruction by the servlet container.
- The servlet life cycle consists of the following phases:

  - **Loading and instantiation**: The servlet container loads the servlet class and creates an instance of the servlet object in memory. This can happen when the servlet container starts up, or when the first request for the servlet is received, or when the servlet is configured to load on startup.
  - **Initialization**: The servlet container invokes the `init()` method of the servlet object to initialize it. The `init()` method receives a `ServletConfig` object that contains the initialization parameters and the servlet context for the servlet. The `init()` method is called only once for each servlet instance.
  - **Request handling**: The servlet container invokes the `service()` method of the servlet object to handle each request that the servlet receives. The `service()` method receives a `HttpServletRequest` object and a `HttpServletResponse` object that represent the request and the response respectively. The `service()` method can delegate the request to other methods based on the HTTP method, such as `doGet()`, `doPost()`, `doPut()`, etc. The `service()` method is called multiple times for each servlet instance, once for each request.
  - **Termination**: The servlet container invokes the `destroy()` method of the servlet object to terminate it. The `destroy()` method is called only once for each servlet instance, when the servlet container is shutting down or when the servlet is removed from the service. The `destroy()` method can perform any cleanup tasks, such as releasing resources or closing connections.

- The servlet interface also defines two non-life cycle methods that are used to get information about the servlet:

  - `getServletConfig()`: This method returns the `ServletConfig` object that was passed to the `init()` method of the servlet. The `ServletConfig` object provides access to the initialization parameters and the servlet context for the servlet.
  - `getServletInfo()`: This method returns a string that contains information about the servlet, such as its name, version, author, etc. This method can be overridden by the servlet to provide custom information.