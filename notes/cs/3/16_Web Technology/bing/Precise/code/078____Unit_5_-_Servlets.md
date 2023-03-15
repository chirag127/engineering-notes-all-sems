## Unit 5 - Servlets

1. **Introduction:** Servlets are Java programs that run on a web server and handle HTTP requests and responses. They are used to create dynamic web content and can interact with databases, web services, and other resources.

2. **Servlet API:** The Servlet API is a set of Java classes and interfaces that define the contract between a servlet and the web container in which it runs. The most important classes and interfaces in the Servlet API are `Servlet`, `ServletConfig`, `ServletRequest`, `ServletResponse`, `HttpServletRequest`, `HttpServletResponse`, and `ServletContext`.

3. **Servlet Lifecycle:** The servlet lifecycle consists of the following stages: initialization, service, and destruction. During initialization, the servlet is instantiated and its `init` method is called. During the service stage, the servlet's `service` method is called to handle incoming requests. During destruction, the servlet's `destroy` method is called and the servlet is removed from service.

4. **Request and Response:** Servlets handle HTTP requests and responses. An HTTP request consists of a request line, headers, and an optional message body. An HTTP response consists of a status line, headers, and an optional message body. Servlets can read request data, set response headers, and generate response content.

5. **Session Management:** Servlets can use session management to maintain state information between requests from the same client. The most common way to implement session management is by using cookies. A cookie is a small piece of data that is sent from the server to the client and stored on the client's machine. The client sends the cookie back to the server with each subsequent request, allowing the server to associate the request with a particular session.

6. **Servlet Filters:** Servlet filters are components that can intercept and modify requests and responses. Filters can be used for a variety of purposes, such as authentication, logging, and compression. Filters are configured in the web application's deployment descriptor and are applied to requests and responses in the order in which they are defined.

7. **Conclusion:** Servlets are a powerful and flexible technology for creating dynamic web content. They provide a standard API for handling HTTP requests and responses, and support features such as session management and filtering. Servlets are widely used in web development and are an essential part of the Java EE platform.