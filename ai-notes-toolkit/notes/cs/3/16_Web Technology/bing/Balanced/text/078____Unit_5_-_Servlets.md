## Unit 5 - Servlets

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can be used to create dynamic web pages, process user input, interact with databases, and implement web services.
- Servlets are based on the Java Servlet API, which defines a set of interfaces and classes for creating and managing servlets.
- The main interface of the Java Servlet API is `javax.servlet.Servlet`, which defines the lifecycle methods and service methods of a servlet.
- The lifecycle methods are `init()`, `destroy()`, and `getServletConfig()`, which are invoked by the web container to initialize, terminate, and configure a servlet instance.
- The service methods are `service()`, `doGet()`, `doPost()`, `doPut()`, `doDelete()`, `doHead()`, `doOptions()`, and `doTrace()`, which are invoked by the web container to handle different types of HTTP requests.
- The service methods receive two parameters: a `javax.servlet.ServletRequest` object and a `javax.servlet.ServletResponse` object, which represent the HTTP request and response respectively.
- The `ServletRequest` object provides methods to access the request parameters, headers, attributes, cookies, and input stream.
- The `ServletResponse` object provides methods to set the response status, headers, content type, cookies, and output stream.
- The `ServletResponse` object also has a `getWriter()` method that returns a `java.io.PrintWriter` object, which can be used to write text data to the response output stream.
- The `ServletResponse` object also has a `getOutputStream()` method that returns a `javax.servlet.ServletOutputStream` object, which can be used to write binary data to the response output stream.
- A servlet can also use the `javax.servlet.ServletContext` object to access the web application context, which provides methods to get the web application name, path, parameters, attributes, resources, and log messages.
- A servlet can also use the `javax.servlet.http.HttpSession` object to manage the user session, which provides methods to get and set the session ID, creation time, last accessed time, attributes, and invalidate the session.
- A servlet can also use the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` objects, which are subclasses of `ServletRequest` and `ServletResponse`, to access the HTTP-specific features, such as methods, headers, cookies, and sessions.
- A servlet can also use the `javax.servlet.RequestDispatcher` object to forward or include the request and response to another servlet or JSP page, which provides methods to `forward()` and `include()`.
- A servlet can also use the `javax.servlet.ServletConfig` object to access the servlet configuration, which provides methods to get the servlet name, initialization parameters, and servlet context.
- A servlet can also use the `javax.servlet.annotation.WebServlet` annotation to specify the servlet name, URL patterns, initialization parameters, and load-on-startup order, which are used by the web container to register and configure the servlet.