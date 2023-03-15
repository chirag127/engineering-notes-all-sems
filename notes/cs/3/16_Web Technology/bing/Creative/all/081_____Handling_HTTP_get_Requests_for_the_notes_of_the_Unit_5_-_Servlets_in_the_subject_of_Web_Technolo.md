# Handling HTTP get Requests for the notes of the Unit 5 - Servlets in the subject of Web Technology

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can process GET requests by overriding the `doGet` method of the `HttpServlet` class.
- The `doGet` method takes two parameters: an `HttpServletRequest` object and an `HttpServletResponse` object.
- The `HttpServletRequest` object represents the request from the client, and provides methods to access the request parameters, headers, cookies, etc.
- The `HttpServletResponse` object represents the response to the client, and provides methods to set the response status, headers, cookies, etc.
- The `doGet` method can also use the `getWriter` method of the `HttpServletResponse` object to obtain a `PrintWriter` object, which can be used to write the response body as text or HTML.
- The `doGet` method can also use the `getServletContext` method of the `HttpServlet` class to obtain a `ServletContext` object, which represents the web application context and provides methods to access the web application resources, attributes, etc.
- The `doGet` method can also use the `getRequestDispatcher` method of the `HttpServletRequest` or `ServletContext` object to obtain a `RequestDispatcher` object, which can be used to forward the request to another servlet or JSP page, or to include the output of another servlet or JSP page in the response.
- The `doGet` method can also use the `sendRedirect` method of the `HttpServletResponse` object to redirect the client to another URL.
- The `doGet` method can also use the `sendError` method of the `HttpServletResponse` object to send an error status and message to the client.
- The `doGet` method can also use the `getServletConfig` method of the `HttpServlet` class to obtain a `ServletConfig` object, which represents the servlet configuration and provides methods to access the servlet initialization parameters, etc.
- The `doGet` method can also use the `getInitParameter` method of the `ServletConfig` or `ServletContext` object to obtain the value of a specific initialization parameter.
- The `doGet` method can also use the `getServletName` method of the `ServletConfig` object to obtain the name of the servlet.
- The `doGet` method can also use the `getServletInfo` method of the `HttpServlet` class to obtain the information about the servlet, such as author, version, etc.
- The `doGet` method can also use the `log` method of the `HttpServlet` class to write a message to the servlet log file.