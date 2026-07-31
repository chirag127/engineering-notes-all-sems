### Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines the methods that a servlet must implement to interact with the servlet container and the clients.
- The servlet life cycle refers to the stages that a servlet goes through from its creation to its destruction by the servlet container.
- The servlet life cycle consists of the following phases:

  - **Loading and instantiation**: The servlet container loads the servlet class and creates an instance of the servlet object in memory. This happens when the servlet is first requested or when the web application is deployed.
  - **Initialization**: The servlet container invokes the `init()` method of the servlet object to initialize it. The `init()` method receives a `ServletConfig` object that contains the initialization parameters and the servlet context. The `init()` method is called only once during the servlet life cycle.
  - **Request handling**: The servlet container invokes the `service()` method of the servlet object to handle each HTTP request that the servlet receives. The `service()` method receives a `HttpServletRequest` object and a `HttpServletResponse` object that represent the request and the response respectively. The `service()` method can delegate the request processing to other methods such as `doGet()`, `doPost()`, `doPut()`, etc. depending on the HTTP method of the request.
  - **Termination**: The servlet container invokes the `destroy()` method of the servlet object to terminate it. The `destroy()` method is called only once when the servlet is no longer needed or when the web application is undeployed. The `destroy()` method can perform any cleanup tasks such as releasing resources or closing connections.

- The following diagram illustrates the servlet life cycle:

![Servlet Life Cycle](https://www.educba.com/wp-content/uploads/2019/12/Servlet-Life-Cycle-Methods.png)