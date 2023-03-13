### Handling HTTP get Requests in Servlets

HTTP GET requests are used to retrieve information from a web server, such as a web page, an image, or a file. A servlet is a Java class that runs on a web server and can handle HTTP requests and generate HTTP responses.

To handle HTTP GET requests in a servlet, you need to extend the HttpServlet class and override the doGet method. The doGet method takes two parameters: an HttpServletRequest object and an HttpServletResponse object. The HttpServletRequest object contains information about the request, such as the URL, the headers, the parameters, and the cookies. The HttpServletResponse object is used to send information back to the client, such as the status code, the headers, the content type, and the body.

The following diagram illustrates the basic architecture of a servlet for handling HTTP GET requests:

```
  +----------------+       +----------------+       +----------------+
  |                |       |                |       |                |
  |     Client     |       |     Server     |       |     Servlet    |
  |                |       |                |       |                |
  +----------------+       +----------------+       +----------------+
        |                       |                       |
        |  HTTP GET request    |                       |
        |--------------------->|                       |
        |                       |                       |
        |                       |  Invoke doGet method  |
        |                       |--------------------->|
        |                       |                       |
        |                       |  Return HTTP response |
        |                       |<---------------------|
        |                       |                       |
        |  HTTP response       |                       |
        |<---------------------|                       |
        |                       |                       |
        |                       |                       |
```

The steps involved in handling HTTP GET requests in a servlet are:

1. The client sends an HTTP GET request to the server, specifying the URL of the servlet.
2. The server receives the request and invokes the service method of the servlet. The service method determines the HTTP method of the request and calls the corresponding method of the servlet. In this case, it calls the doGet method.
3. The doGet method of the servlet receives the HttpServletRequest and HttpServletResponse objects as parameters. It can use the HttpServletRequest object to access the information about the request, such as the parameters, the headers, and the cookies. It can use the HttpServletResponse object to set the information about the response, such as the status code, the headers, the content type, and the body. It can also use the PrintWriter object obtained from the getWriter method of the HttpServletResponse object to write the content of the response.
4. The doGet method of the servlet returns the HTTP response to the server, which then sends it back to the client.
5. The client receives the HTTP response and displays the content of the response.