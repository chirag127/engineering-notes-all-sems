### Servlet Overview and Architecture

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can be used to create dynamic web applications that generate HTML, XML, JSON, or other types of content.
- A servlet implements the `javax.servlet.Servlet` interface, which defines the lifecycle methods and the service method for processing requests.
- A servlet is managed by a servlet container, which is a component of a web server that provides services such as request dispatching, security, concurrency, and session management.
- A servlet container also compiles, loads, instantiates, initializes, and destroys servlets according to the servlet lifecycle.
- A servlet can be configured using annotations or deployment descriptors, which specify the servlet name, URL mapping, initialization parameters, and other properties.
- A servlet can access the request and response objects, which are instances of `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse`, respectively.
- A request object contains information about the client request, such as the HTTP method, the URI, the headers, the parameters, the cookies, and the input stream.
- A response object contains information about the server response, such as the status code, the headers, the cookies, and the output stream.
- A servlet can use the request and response objects to read and write data, set headers and cookies, redirect or forward requests, and handle errors and exceptions.
- A servlet can also access the servlet context and the servlet config objects, which are instances of `javax.servlet.ServletContext` and `javax.servlet.ServletConfig`, respectively.
- A servlet context object represents the web application and provides methods to access shared resources, such as attributes, parameters, and resources.
- A servlet config object represents the servlet instance and provides methods to access initialization parameters and the servlet context.
- A servlet can also use the session object, which is an instance of `javax.servlet.http.HttpSession`, to store and retrieve data across multiple requests from the same client.
- A session object is created by the servlet container when a client first accesses the web application and is identified by a unique session ID.
- A session object can be invalidated by the servlet or by the servlet container when it expires or when the web application is undeployed.

The following diagram shows the servlet architecture:

![servlet architecture](https://www.tutorialspoint.com/servlets/images/servlet-architecture.jpg)

Source: https://www.tutorialspoint.com/servlets/servlets_overview.htm