# Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines the methods that a servlet must implement to interact with the servlet container and the clients.
- The servlet life cycle refers to the stages that a servlet goes through from its creation to its destruction by the servlet container.
- The servlet life cycle consists of the following phases:

  - **Initialization**: The servlet container loads the servlet class and creates an instance of the servlet. Then, the container invokes the `init` method of the servlet, passing a `ServletConfig` object that contains the initialization parameters and the servlet context. The `init` method is called only once during the servlet's life span and can be used to perform any one-time tasks, such as establishing database connections or loading configuration files.
  - **Service**: The servlet container calls the `service` method of the servlet for each request that the servlet receives. The `service` method determines the HTTP method (such as GET, POST, PUT, DELETE, etc.) of the request and invokes the corresponding `doGet`, `doPost`, `doPut`, `doDelete`, etc. methods of the servlet. The `service` method also passes a `HttpServletRequest` object that contains the request information and a `HttpServletResponse` object that contains the response information. The `service` method can be overridden by the servlet to handle any HTTP method or to perform any common tasks for all requests.
  - **Destruction**: The servlet container calls the `destroy` method of the servlet when the servlet is no longer needed or the web application is shut down. The `destroy` method is called only once during the servlet's life span and can be used to perform any final tasks, such as releasing resources or closing connections. The `destroy` method should ensure that any threads created by the servlet are stopped and any shared data is synchronized.

- The servlet interface also defines two non-life cycle methods that are used to access the servlet configuration and the servlet context:

  - **getServletConfig**: This method returns the `ServletConfig` object that was passed to the `init` method of the servlet. The `ServletConfig` object provides access to the initialization parameters and the servlet name of the servlet.
  - **getServletContext**: This method returns the `ServletContext` object that represents the web application that the servlet belongs to. The `ServletContext` object provides access to the web application resources, parameters, attributes, and logging facilities.