### Directives for the notes of the Unit 5 - Servlets in the subject of Web Technology

- A servlet is a Java program that runs on a web server and handles HTTP requests and responses.
- A servlet can perform various tasks, such as generating dynamic web content, processing user input, interacting with databases, and implementing business logic.
- A servlet is managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- A servlet container is responsible for loading, initializing, executing, and destroying servlets, as well as managing their life cycle and communication.
- To create a servlet, one needs to extend the `javax.servlet.http.HttpServlet` class and override its methods, such as `doGet`, `doPost`, `doPut`, `doDelete`, etc., to handle different HTTP methods.
- A servlet can also implement the `javax.servlet.Servlet` interface directly, but this requires more coding and is less convenient.
- A servlet can access the request and response objects, which are instances of the `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse` classes, respectively.
- The request object contains information about the client's request, such as the URL, parameters, headers, cookies, session, etc.
- The response object contains information about the server's response, such as the status code, headers, cookies, content type, etc.
- A servlet can use the request and response objects to read and write data, set headers and cookies, redirect or forward requests, etc.
- A servlet can also use the `javax.servlet.ServletConfig` and `javax.servlet.ServletContext` objects, which are provided by the servlet container, to access initialization parameters and shared resources, respectively.
- A servlet can also use the `javax.servlet.http.HttpSession` object, which is created by the servlet container, to store and retrieve data across multiple requests from the same client.
- A servlet can also use the `javax.servlet.RequestDispatcher` object, which is obtained from the request or context objects, to forward or include requests to other servlets or web pages.
- A servlet can also use the `javax.servlet.Filter` interface, which is implemented by classes that can intercept and modify requests and responses before or after they reach the servlet.
- A servlet can also use the `javax.servlet.annotation` package, which contains annotations that can simplify the configuration and deployment of servlets, such as `@WebServlet`, `@WebFilter`, `@WebInitParam`, etc.
- A servlet can also use the `javax.servlet.jsp` package, which contains classes and interfaces that support the integration of servlets and JavaServer Pages (JSP), which are web pages that contain Java code and HTML tags.
- A servlet can also use the `javax.servlet.AsyncContext` and `javax.servlet.AsyncListener` interfaces, which enable the servlet to handle requests asynchronously, without blocking the thread, and to receive notifications about the completion or timeout of the asynchronous operation.