# Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines the methods that a servlet must implement to interact with the servlet container and the clients.
- The servlet life cycle refers to the stages that a servlet goes through from its creation to its destruction by the servlet container.
- The servlet life cycle consists of the following phases:

  - **Loading and instantiation**: The servlet container loads the servlet class and creates an instance of the servlet object in memory. This happens when the servlet is first requested by a client or when the container is started.
  - **Initialization**: The servlet container invokes the `init()` method of the servlet object to initialize it. The `init()` method receives a `ServletConfig` object that contains the initialization parameters and the servlet context. The `init()` method can be used to perform any one-time tasks such as opening database connections or reading configuration files.
  - **Request handling**: The servlet container invokes the `service()` method of the servlet object to handle each HTTP request that the servlet receives. The `service()` method receives a `HttpServletRequest` object that contains the request information and a `HttpServletResponse` object that is used to send the response back to the client. The `service()` method can be used to perform any business logic, access data sources, generate dynamic content, or dispatch the request to other resources. The `service()` method can also delegate the request handling to the `doGet()`, `doPost()`, `doPut()`, `doDelete()`, or `doHead()` methods depending on the HTTP method of the request.
  - **Termination**: The servlet container invokes the `destroy()` method of the servlet object to destroy it. The `destroy()` method is called when the servlet is no longer needed, such as when the container is shut down or when the servlet is unloaded. The `destroy()` method can be used to perform any cleanup tasks such as closing database connections or releasing resources.

- The following diagram illustrates the servlet life cycle:

![Servlet Life Cycle](https://www.educba.com/wp-content/uploads/2019/12/Servlet-Life-Cycle-Methods.png)