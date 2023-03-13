### Interface Servlet and the Servlet Life Cycle in Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- All servlets must implement the `javax.servlet.Servlet` interface, which defines the methods to initialize a servlet, to service requests, and to destroy a servlet from the server .
- These methods are known as life-cycle methods, and are called in a specific order by the web container.
- The life cycle of a servlet consists of the following stages :

  1. **Servlet is loaded**: The web container loads the servlet class when it receives a request for the servlet or when the servlet is configured to load on startup.
  2. **Servlet is initialized**: The web container invokes the `init()` method of the servlet to initialize it. The `init()` method receives a `ServletConfig` object that contains the servlet configuration and initialization parameters. The `init()` method is called only once during the servlet life cycle  .
  3. **Servlet is ready to service**: After the `init()` method completes, the servlet is ready to handle incoming requests. The web container creates a separate thread for each request and passes the request and response objects to the servlet.
  4. **Servlet is servicing**: The web container calls the `service()` method of the servlet to process the request and generate the response. The `service()` method determines the HTTP method (such as GET, POST, PUT, etc.) of the request and calls the corresponding `doGet()`, `doPost()`, `doPut()`, etc. methods of the servlet. The `service()` method is called for each request during the servlet life cycle  .
  5. **Servlet is not ready to service**: The servlet may become unavailable to service requests due to various reasons, such as unhandled exceptions, configuration errors, or manual unloading. The web container will return an error message to the client when the servlet is not ready to service.
  6. **Servlet is destroyed**: The web container invokes the `destroy()` method of the servlet to destroy it and release its resources. The `destroy()` method is called only once at the end of the servlet life cycle, usually when the web container is shutting down or when the servlet is removed from the web application  .

- The following diagram illustrates the servlet life cycle:

```
  +-----------------+     +-----------------+     +-----------------+
  | Servlet is      |     | Servlet is      |     | Servlet is      |
  | loaded          |     | initialized     |     | ready to service|
  +-----------------+     +-----------------+     +-----------------+
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          v                       v                       v
  +-----------------+     +-----------------+     +-----------------+
  | Servlet is      |     | Servlet is      |     | Servlet is      |
  | servicing       |     | not ready to    |     | destroyed       |
  +-----------------+     +-----------------+     +-----------------+
```

- A possible mnemonic to remember the servlet life cycle methods is **I See D**:

  - **I**nit()
  - **S**ervice()
  - **D**estroy()