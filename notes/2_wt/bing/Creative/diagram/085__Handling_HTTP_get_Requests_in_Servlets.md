Handling HTTP GET requests in servlets is a process of receiving and processing the requests from the client browser and sending back the response. The following diagram illustrates the basic architecture of a servlet that handles HTTP GET requests.

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Client        |       |  Web Server    |       |  Servlet       |
|  Browser       |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  1. Send       |       |                |       |                |
|  HTTP GET      | ----> |  2. Receive    |       |                |
|  request       |       |  request       |       |                |
|                |       |                |       |                |
|                |       |  3. Forward    |       |                |
|                |       |  request to    | ----> |  4. Receive    |
|                |       |  servlet       |       |  request       |
|                |       |                |       |                |
|                |       |                |       |  5. Process    |
|                |       |                |       |  request       |
|                |       |                |       |                |
|                |       |                |       |  6. Send       |
|                |       |                |       |  response      |
|                |       |                | <---- |  to web server |
|                |       |                |       |                |
|                |       |  7. Receive    |       |                |
|                |       |  response      |       |                |
|                |       |                |       |                |
|  8. Receive    |       |  9. Send       |       |                |
|  response      | <---- |  response      |       |                |
|                |       |  to browser    |       |                |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

The steps involved in handling HTTP GET requests in servlets are:

1. The client browser sends an HTTP GET request to the web server with the URL of the servlet and any parameters.
2. The web server receives the request and checks if the URL matches any servlet mapping in the web.xml file.
3. If the URL matches a servlet mapping, the web server forwards the request to the corresponding servlet instance. If the servlet instance does not exist, the web server creates a new one and calls its init() method.
4. The servlet receives the request and calls its service() method, which in turn calls the doGet() method. The doGet() method takes two parameters: an HttpServletRequest object and an HttpServletResponse object. The HttpServletRequest object contains the information about the request, such as the parameters, headers, cookies, etc. The HttpServletResponse object is used to send the response back to the web server.
5. The servlet processes the request and generates the response. The response can be HTML, plain text, XML, JSON, etc. The servlet can also set the response headers, cookies, status code, etc. using the HttpServletResponse object.
6. The servlet sends the response back to the web server using the HttpServletResponse object. The servlet can also call the flush() and close() methods on the HttpServletResponse object to indicate that the response is complete.
7. The web server receives the response from the servlet and checks if the response is valid and complete. If the response is valid and complete, the web server sends the response back to the client browser. If the response is invalid or incomplete, the web server sends an error message to the client browser.
8. The client browser receives the response from the web server and displays the content or the error message to the user. The client browser can also store the cookies, headers, etc. from the response for future requests.