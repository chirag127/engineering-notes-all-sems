### Interface Servlet and the Servlet Life Cycle in Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- All servlets must implement the `javax.servlet.Servlet` interface, which defines the methods to initialize a servlet, to service requests, and to destroy a servlet from the server .
- These methods are known as **life cycle methods**, and are called by the web container (such as Tomcat or Jetty) at different stages of the servlet's existence.
- The life cycle of a servlet consists of the following stages :

  1. **Servlet is loaded**: The web container loads the servlet class when it receives the first request for the servlet, or when the server starts up and the servlet is configured to load on startup.
  2. **Servlet is initialized**: The web container invokes the `init()` method of the servlet, which corresponds to the initialization phase of the servlet life cycle. The `init()` method receives a `ServletConfig` object that contains the servlet's configuration information. The `init()` method is called only once during the servlet's lifetime .
  3. **Servlet is ready to service**: After the `init()` method completes, the servlet is ready to handle HTTP requests. The web container creates a separate thread for each request and passes the request and response objects to the servlet.
  4. **Servlet is servicing**: The web container calls the `service()` method of the servlet, which determines the HTTP method (such as GET, POST, PUT, DELETE, etc.) of the request and dispatches it to the corresponding handler method (such as `doGet()`, `doPost()`, `doPut()`, `doDelete()`, etc.) of the servlet. The handler method processes the request, sets the response headers and content, and writes the response back to the client .
  5. **Servlet is not ready to service**: The servlet may become unavailable to service requests due to various reasons, such as configuration changes, reloading, unloading, or errors. The web container will stop sending requests to the servlet and will invoke the `destroy()` method of the servlet.
  6. **Servlet is destroyed**: The web container invokes the `destroy()` method of the servlet, which corresponds to the destruction phase of the servlet life cycle. The `destroy()` method is called only once during the servlet's lifetime and it gives the servlet a chance to release any resources it has acquired, such as database connections, threads, etc. After the `destroy()` method completes, the web container unloads the servlet class from the memory .

- The following diagram illustrates the servlet life cycle:

```
  +-----------------+       +-----------------+       +-----------------+
  | Servlet is      |       | Servlet is      |       | Servlet is      |
  | loaded          |       | initialized     |       | ready to service|
  +-----------------+       +-----------------+       +-----------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          v                         v                         v
  +-----------------+       +-----------------+       +-----------------+
  | Servlet is      |       | Servlet is      |       | Servlet is      |
  | servicing       |       | not ready to    |       | destroyed       |
  +-----------------+       +-----------------+       +-----------------+
```

- A possible mnemonic to remember the servlet life cycle methods is **I See Dogs**:

  - **I**: `init()`
  - **S**: `service()`
  - **D**: `destroy()`