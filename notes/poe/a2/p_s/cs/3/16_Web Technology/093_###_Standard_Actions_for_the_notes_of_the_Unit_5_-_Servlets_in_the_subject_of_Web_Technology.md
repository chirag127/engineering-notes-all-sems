 Here is the content in markdown format for the given topic:

### Standard Actions for Servlets

The following are the standard actions that a Servlet can perform:

1. Read the input from the request - A Servlet can read various types of input from the request such as form data, URL parameters, headers, etc. This is done using methods like `getInputStream()`, `getParameter()`, `getHeader()`, etc. on the `HttpServletRequest` object.
2. Write the output to the response - A Servlet can write output to the response in various formats like HTML, XML, JSON, images, etc. This is done using methods like `getOutputStream()` or `getWriter()` on the `HttpServletResponse` object. The output format can be specified using methods like `setContentType()` on the response object.
3. Access resources - A Servlet can access various resources available to the web container such as database connections, JNDI, properties, file system, etc. This allows the Servlet to perform business logic and prepare dynamic responses.
4. Call other servlets/modules - A Servlet can forward control or request to other servlets/modules for completing the request. This is done using methods like `request.getRequestDispatcher()` and `forward()` or `include()` methods. This allows modularizing the application into components.

The advantages of using Servlets are:

- Platform independence - Servlets are written in Java and hence are platform independent. They can run on any server/container that supports Servlet specification.
- Modular design - Servlets allow modular design of web applications by dividing the work into multiple modules (Servlets). This improves maintainability and reusability.
- Performance - Servlets are efficient as they are compiled Java classes and the server can optimize the execution of servlets. Also, the concepts of multithreading and connection pooling can be used to handle multiple requests efficiently.

[Detailed diagrams and examples can be added here if required.]