### Handling HTTP get Requests for the notes of the Unit 5 - Servlets in the subject of Web Technology

- HTTP get requests are used to retrieve information from a web server based on the parameters specified in the URL.
- To handle HTTP get requests in a servlet, extend the HttpServlet class and override the doGet method.
- The doGet method takes two parameters: HttpServletRequest and HttpServletResponse, which represent the request and response objects respectively .
- The HttpServletRequest object provides methods to access the request headers, parameters, cookies, and other information.
- The HttpServletResponse object provides methods to set the response headers, status code, content type, and body.
- The doGet method can use the PrintWriter object obtained from the response object to write the response body .
- The doGet method can also use the RequestDispatcher object obtained from the request object to forward or include the request and response to another resource.
- The doGet method can handle HTTP head requests automatically, as they are similar to get requests but only return the response headers and not the body.
- The doGet method should be idempotent, meaning that it should not change the state of the server or have any side effects.
- The doGet method should be thread-safe, meaning that it should not use any instance variables or synchronize on the servlet object.