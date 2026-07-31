### Handling HTTP get Requests for the notes of the Unit 5 - Servlets in the subject of Web Technology

Handling HTTP get requests is an important aspect of servlet programming. In this unit, we will learn about how to handle HTTP get requests using servlets. Here are some important points to keep in mind:

- HTTP get requests are used to retrieve data from a server. In servlet programming, we use the `doGet()` method to handle HTTP get requests.
- The `doGet()` method is part of the `HttpServlet` class, which is the base class for all servlets. It takes two parameters: a `HttpServletRequest` object and a `HttpServletResponse` object.
- The `HttpServletRequest` object contains information about the request, such as the request URL, headers, and parameters. The `HttpServletResponse` object is used to send a response back to the client.
- The `doGet()` method should be overridden in the servlet class to handle HTTP get requests. In this method, we can retrieve data from a database or any other source and send it back to the client as a response.
- We can use the `getParameter()` method of the `HttpServletRequest` object to retrieve the value of a parameter passed in the request URL. For example, if the request URL is `http://example.com/servlet?name=John`, we can retrieve the value of the `name` parameter using the following code: `String name = request.getParameter("name");`
- We can also use the `getHeader()` method of the `HttpServletRequest` object to retrieve the value of a header passed in the request. For example, if the request contains a `User-Agent` header, we can retrieve its value using the following code: `String userAgent = request.getHeader("User-Agent");`
- We can set the content type of the response using the `setContentType()` method of the `HttpServletResponse` object. For example, if we want to send back an HTML page as the response, we can set the content type as follows: `response.setContentType("text/html");`
- We can send the response back to the client using the `getWriter()` method of the `HttpServletResponse` object. For example, if we want to send back an HTML page as the response, we can use the following code:

```
PrintWriter out = response.getWriter();
out.println("<html>");
out.println("<head><title>Hello World</title></head>");
out.println("<body>");
out.println("<h1>Hello World</h1>");
out.println("</body></html>");
```

Handling HTTP get requests is a fundamental aspect of servlet programming. By following these points, you can effectively handle HTTP get requests using servlets.