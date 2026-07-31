### Interface Servlet and the Servlet Life Cycle in Servlets

- The **javax.servlet.Servlet** interface is the core interface that defines a servlet. All servlets implement this interface either directly, or more commonly, by extending a class that implements the interface, such as **javax.servlet.http.HttpServlet**.
- The Servlet interface provides a **life cycle methods** to initialize a servlet, to service requests, and to remove a servlet from the server. These Servlet interface methods are central to the life cycle of a servlet .
- The life cycle of a servlet consists of the following stages:
  - **Servlet is born**: The web container loads the servlet class and creates an instance of the servlet. This happens when the servlet is requested for the first time, or when the web container is started, or when the servlet is configured with a load-on-startup element in the web.xml file.
  - **Servlet is initialized**: The web container invokes the **init()** method of the servlet. This method is used to perform any one-time initialization tasks, such as creating database connections, initializing configuration parameters, etc. The init() method receives a **ServletConfig** object that contains the servlet's configuration information  .
  - **Servlet is ready to service**: The servlet is now ready to handle client requests. The web container creates a separate thread for each request and passes the request and response objects to the servlet .
  - **Servlet is servicing**: The web container calls the **service()** method of the servlet for each request. This method is responsible for dispatching the request to the appropriate handler method, such as **doGet()** or **doPost()** for HTTP servlets. The service() method also reads the request data, performs the business logic, and writes the response data   .
  - **Servlet is not ready to service**: The servlet may become unavailable to service requests due to various reasons, such as configuration changes, reloading, unloading, etc. The web container will notify the servlet by calling the **isUnavailable()** method of the Servlet interface. This method returns true if the servlet is unavailable, and false otherwise.
  - **Servlet is destroyed**: The web container may decide to remove the servlet from the server, either to free up memory resources, or to shut down the server, or to redeploy the web application. The web container will call the **destroy()** method of the servlet before removing it. This method is used to perform any finalization tasks, such as closing database connections, releasing resources, etc   .
- The life cycle of a servlet is illustrated in the following diagram:

```
+-----------------+     +-----------------+     +-----------------+
| Servlet is born | --> | Servlet is      | --> | Servlet is      |
|                 |     | initialized     |     | ready to service|
+-----------------+     +-----------------+     +-----------------+
                                                        |
                                                        |
                                                        V
+-----------------+     +-----------------+     +-----------------+
| Servlet is      | <-- | Servlet is      | <-- | Servlet is      |
| destroyed       |     | not ready to    |     | servicing       |
|                 |     | service         |     |                 |
+-----------------+     +-----------------+     +-----------------+
```