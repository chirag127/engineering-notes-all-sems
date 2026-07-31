## Unit 5 - Servlets

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can be used to create dynamic web pages, process user input, interact with databases, and implement web services.
- Servlets are compiled into bytecode and loaded by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- Servlets follow a request-response model, where each servlet has a `service` method that receives an `HttpServletRequest` object and an `HttpServletResponse` object as parameters, and performs the business logic based on the request, and sends back the response.
- Servlets can be configured and initialized using annotations or deployment descriptors (XML files).
- Servlets have a life cycle that consists of three phases: initialization, service, and destruction.
  - Initialization: The servlet container calls the `init` method of the servlet once, when it is first loaded or requested. The `init` method can be used to perform any one-time tasks, such as loading configuration parameters or establishing database connections.
  - Service: The servlet container calls the `service` method of the servlet for each request it receives. The `service` method can delegate the request to other methods, such as `doGet`, `doPost`, `doPut`, `doDelete`, etc., depending on the HTTP method of the request. The `service` method can also set the response headers, status code, and body, and send the response back to the client.
  - Destruction: The servlet container calls the `destroy` method of the servlet once, when it is unloaded or the web server is shut down. The `destroy` method can be used to perform any cleanup tasks, such as closing database connections or releasing resources.
- Servlets can communicate with other servlets or web components using various mechanisms, such as request attributes, request parameters, session attributes, cookies, URL rewriting, hidden fields, etc.
- Servlets can also use filters and listeners to intercept and modify requests and responses, and to perform certain actions when certain events occur in the web application.
- Servlets can be tested and debugged using tools such as Eclipse, NetBeans, Tomcat, JUnit, etc.

Some mnemonics and learning tricks for servlets are:

- To remember the life cycle methods of servlets, use the acronym **ISD** (init, service, destroy).
- To remember the HTTP methods that servlets can handle, use the acronym **GPOD** (get, post, put, delete).
- To remember the common communication mechanisms between servlets, use the acronym **CRUSH** (cookies, request attributes, URL rewriting, session attributes, hidden fields).