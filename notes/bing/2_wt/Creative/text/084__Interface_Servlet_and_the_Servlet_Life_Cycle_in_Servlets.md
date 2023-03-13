### Interface Servlet and the Servlet Life Cycle in Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- All servlets must implement the `javax.servlet.Servlet` interface, which defines the methods to initialize a servlet, to service requests, and to destroy a servlet from the server .
- These methods are known as **life cycle methods**, and are called by the web container (the application that manages the servlets) at different stages of the servlet's existence .
- The life cycle of a servlet consists of the following stages :

  - **Servlet is loaded**: The web container loads the servlet class into memory when it is requested for the first time, or when the server starts up.
  - **Servlet is initialized**: The web container invokes the `init()` method of the servlet, which corresponds to the initialization phase of the servlet life cycle. The `init()` method receives a `ServletConfig` object that contains the initialization parameters and the servlet context. The `init()` method can be used to perform any one-time tasks, such as creating database connections, initializing resources, etc. The `init()` method is called only once during the servlet's lifetime  .
  - **Servlet is ready to service**: After the `init()` method completes, the servlet is ready to handle client requests. The web container creates a separate thread for each request and passes the request and response objects to the servlet.
  - **Servlet is servicing**: The web container calls the `service()` method of the servlet for each request. The `service()` method determines the type of the request (GET, POST, PUT, DELETE, etc.) and dispatches it to the appropriate handler method, such as `doGet()`, `doPost()`, etc. The handler methods can access the request parameters, headers, cookies, etc. and generate the response content, status, headers, cookies, etc. The `service()` method can be overridden by the servlet, but it is not recommended .
  - **Servlet is not ready to service**: The servlet can become unavailable to service requests for various reasons, such as being temporarily disabled, being under maintenance, or being overloaded. The web container can call the `isUnavailable()` method of the servlet to check its availability status. The servlet can also notify the web container of its unavailability by throwing an `UnavailableException`.
  - **Servlet is destroyed**: The web container invokes the `destroy()` method of the servlet, which corresponds to the destruction phase of the servlet life cycle. The `destroy()` method can be used to perform any final tasks, such as releasing resources, closing connections, etc. The `destroy()` method is called only once at the end of the servlet's lifetime, or when the web container shuts down  .

- The following diagram illustrates the servlet life cycle:

![Servlet Life Cycle](https://media.geeksforgeeks.org/wp-content/uploads/20190715175306/servlet-life-cycle.png)

- The servlet life cycle methods are central to the functioning of a servlet, and they should be implemented carefully and correctly. The servlet interface provides default implementations for these methods, but they are usually overridden by the servlet subclasses, such as `HttpServlet`, `GenericServlet`, etc. The servlet subclasses provide more convenience and flexibility for handling different types of requests and responses .