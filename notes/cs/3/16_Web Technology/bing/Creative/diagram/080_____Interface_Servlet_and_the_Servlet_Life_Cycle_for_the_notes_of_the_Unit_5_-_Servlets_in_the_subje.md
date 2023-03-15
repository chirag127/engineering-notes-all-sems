### Interface Servlet and the Servlet Life Cycle

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface and runs on a web server to handle HTTP requests and responses.
- The servlet interface defines five methods that correspond to the different phases of a servlet's life cycle: `init`, `service`, `destroy`, `getServletConfig`, and `getServletInfo`.
- The servlet life cycle consists of the following stages:

  1. **Servlet is loaded**: The web container loads the servlet class into memory, either when the web server starts up or when the first request for the servlet is received.
  2. **Servlet is initialized**: The web container invokes the `init` method of the servlet, passing a `ServletConfig` object that contains initialization parameters and servlet configuration information. The `init` method is called only once during the servlet's life cycle and can be used to perform one-time initialization tasks.
  3. **Servlet is ready to service**: The servlet is now ready to handle HTTP requests from clients. The web container creates a new thread for each request and calls the `service` method of the servlet, passing a `HttpServletRequest` object that contains the request information and a `HttpServletResponse` object that is used to send the response back to the client. The `service` method can delegate the request to other methods such as `doGet`, `doPost`, `doPut`, etc. depending on the HTTP method of the request.
  4. **Servlet is servicing**: The servlet processes the request and generates a response, which is sent back to the client through the `HttpServletResponse` object. The servlet can also access other resources such as databases, files, or other servlets to perform its task.
  5. **Servlet is not ready to service**: The servlet can become unavailable to service requests for various reasons, such as being temporarily disabled, being reloaded, or being shut down by the web container. The web container will reject any new requests for the servlet and wait for the existing requests to complete.
  6. **Servlet is destroyed**: The web container invokes the `destroy` method of the servlet to release any resources that the servlet is holding and to perform any finalization tasks. The `destroy` method is called only once during the servlet's life cycle and can be used to perform cleanup tasks. The servlet object is then eligible for garbage collection.

- The following diagram illustrates the servlet life cycle:

```
+----------------+      +----------------+      +----------------+
| Servlet is     |      | Servlet is     |      | Servlet is     |
| loaded         |      | initialized    |      | ready to       |
|                |      |                |      | service        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
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
       +---------------------->+                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              |                       |
                              +---------------------->+----------------------+
                                                     | Servlet is          |
                                                     | servicing           |
                                                     |                     |
                                                     +----------------------+
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |
                                                           |