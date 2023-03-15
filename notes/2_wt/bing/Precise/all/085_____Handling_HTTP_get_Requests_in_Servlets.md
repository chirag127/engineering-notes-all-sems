### Handling HTTP get Requests in Servlets

1. A servlet is a Java class that runs on a server and handles HTTP requests and responses.
2. The `doGet` method is used to handle HTTP GET requests.
3. The `doGet` method takes two arguments: an `HttpServletRequest` object and an `HttpServletResponse` object.
4. The `HttpServletRequest` object represents the request sent by the client to the server.
5. The `HttpServletResponse` object represents the response sent by the server to the client.
6. The `doGet` method is called by the servlet container when a GET request is made to the servlet.
7. The `doGet` method can be overridden to provide custom handling of GET requests.
8. The `doGet` method can use the `HttpServletRequest` object to get information about the request, such as the request parameters and headers.
9. The `doGet` method can use the `HttpServletResponse` object to set the response status, headers, and body.
10. The `doGet` method can use the `HttpServletResponse` object to send a response to the client.
11. The `doGet` method should not have any side effects, as GET requests are intended to be idempotent.
12. The `doGet` method should be used for requests that only retrieve data, not for requests that modify data.

Example:
```java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String name = request.getParameter("name");
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html><body>");
    out.println("<h1>Hello, " + name + "</h1>");
    out.println("</body></html>");
}
```