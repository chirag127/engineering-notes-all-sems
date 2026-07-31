## Unit 5 - Servlets

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can be used to create dynamic web pages, process user input, communicate with databases, and implement web services.
- Servlets are based on the Java Servlet API, which defines the interfaces and classes for writing servlets.
- The most common interface for servlets is `javax.servlet.Servlet`, which has methods for initializing, servicing, and destroying a servlet instance.
- The most common abstract class for servlets is `javax.servlet.http.HttpServlet`, which extends `Servlet` and provides methods for handling HTTP-specific requests and responses, such as `doGet`, `doPost`, `doPut`, `doDelete`, etc.
- To create a servlet, one must extend `HttpServlet` and override one or more of its methods, depending on the HTTP methods supported by the servlet.
- A servlet must also be configured in the web application deployment descriptor (`web.xml`), which specifies the servlet name, class, initialization parameters, URL mapping, load-on-startup order, security constraints, etc.
- A servlet can access the request and response objects passed as parameters to its service methods, which are instances of `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse`, respectively.
- A request object contains information about the client request, such as the request method, URI, headers, parameters, cookies, session, etc.
- A response object contains information about the server response, such as the status code, headers, cookies, etc. It also provides methods for sending data to the client, such as `sendRedirect`, `sendError`, `getWriter`, `getOutputStream`, etc.
- A servlet can also access the servlet context and the servlet config objects, which are instances of `javax.servlet.ServletContext` and `javax.servlet.ServletConfig`, respectively.
- A servlet context object represents the web application that the servlet belongs to, and provides methods for accessing shared resources, such as attributes, initialization parameters, resource paths, log files, etc.
- A servlet config object represents the configuration of a specific servlet instance, and provides methods for accessing its name, initialization parameters, and servlet context.
- A servlet can also use filters, listeners, and annotations to enhance its functionality and interact with the web container.
- Filters are Java classes that implement `javax.servlet.Filter`, and can intercept and modify requests and responses before and after they reach a servlet or a static resource.
- Listeners are Java classes that implement one or more of the `javax.servlet` event listener interfaces, and can perform actions when certain events occur in the web application lifecycle, such as servlet context initialization, session creation, attribute changes, etc.
- Annotations are Java annotations that can be used to declare and configure servlets, filters, listeners, and other web components, without using the `web.xml` file. They are defined in the `javax.servlet.annotation` package, and can be processed by the web container at deployment time.