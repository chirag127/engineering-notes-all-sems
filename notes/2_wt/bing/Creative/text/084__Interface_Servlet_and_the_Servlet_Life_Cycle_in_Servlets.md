### Interface Servlet and the Servlet Life Cycle in Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- All servlets must implement the `javax.servlet.Servlet` interface, which defines the methods to initialize a servlet, to service requests, and to remove a servlet from the server.
- These methods are known as life-cycle methods, and are called by the web container (or servlet container) that manages the servlet.
- The web container can load and instantiate a servlet when the web application is deployed, or when the first request for the servlet is received.
- The servlet life cycle mainly goes through four stages:
  - Loading and instantiation: The web container loads the servlet class and creates an instance of the servlet.
  - Initialization: The web container invokes the `init(ServletConfig)` method of the servlet, passing a `ServletConfig` object that contains initialization parameters and servlet configuration. This method is called only once for each servlet instance.
  - Request handling: The web container invokes the `service(ServletRequest, ServletResponse)` method of the servlet for each request that the servlet receives. The `ServletRequest` and `ServletResponse` objects provide access to the request and response data. The `service()` method can delegate the request to different methods based on the HTTP method, such as `doGet()`, `doPost()`, etc.
  - Destruction: The web container invokes the `destroy()` method of the servlet before removing the servlet instance from the service. This method is called only once for each servlet instance and gives the servlet an opportunity to release any resources it has allocated.
- The following diagram illustrates the servlet life cycle:

![Servlet Life Cycle](https://media.geeksforgeeks.org/wp-content/uploads/20201019194957/Servlet-Life-Cycle.png)