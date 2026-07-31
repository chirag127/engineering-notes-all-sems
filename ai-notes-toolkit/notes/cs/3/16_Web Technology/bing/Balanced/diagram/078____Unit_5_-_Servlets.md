## Unit 5 - Servlets

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can be used to create dynamic web pages, process user input, communicate with databases, and implement web services.
- Servlets are based on the Java Servlet API, which defines a set of interfaces and classes for creating and managing servlets.
- The main interface of the Java Servlet API is `javax.servlet.Servlet`, which defines the lifecycle methods and the service method of a servlet.
- The lifecycle methods are `init()`, `destroy()`, and `getServletConfig()`, which are invoked by the web container to initialize, terminate, and configure a servlet instance.
- The service method is `service()`, which is invoked by the web container to process an HTTP request and generate an HTTP response. The service method can delegate the request and response objects to `doGet()`, `doPost()`, `doPut()`, `doDelete()`, etc. methods, depending on the HTTP method of the request.
- The request and response objects are instances of `javax.servlet.ServletRequest` and `javax.servlet.ServletResponse` interfaces, which provide methods to access the request parameters, headers, body, and attributes, and to set the response status, headers, body, and attributes.
- The request and response objects can be cast to `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` interfaces, which provide additional methods to handle HTTP-specific features, such as cookies, sessions, and redirections.
- To create a servlet, one can either implement the `Servlet` interface directly, or extend an abstract class that implements the `Servlet` interface, such as `javax.servlet.GenericServlet` or `javax.servlet.http.HttpServlet`.
- To deploy a servlet, one needs to register it in the web application's deployment descriptor (`web.xml` file), or use annotations (`@WebServlet` annotation) to specify the servlet name, URL pattern, initialization parameters, etc.
- To run a servlet, one needs to have a web server that supports the Java Servlet API, such as Apache Tomcat, Jetty, GlassFish, etc. The web server acts as a web container that manages the servlet instances, invokes their lifecycle and service methods, and provides them with the request and response objects.