# Redirecting Requests to Other Resources

- Sometimes, a servlet may need to delegate the request processing to another resource, such as another servlet, a JSP page, or an HTML file.
- This can be done by using two methods: **forward** and **sendRedirect**.
- Both methods are available in the **HttpServletResponse** interface, which is passed as a parameter to the **doGet** or **doPost** methods of the servlet.
- The difference between the two methods is that **forward** transfers the control to another resource within the same server, while **sendRedirect** instructs the client browser to make a new request to another resource, which can be on a different server.
- The syntax of the two methods are:

```java
// forward method
void forward(ServletRequest request, ServletResponse response) throws ServletException, IOException

// sendRedirect method
void sendRedirect(String location) throws IOException
```

- To use the **forward** method, the servlet needs to obtain a **RequestDispatcher** object from the **ServletContext** or the **ServletRequest** object, and then call the **forward** method on it, passing the request and response objects as arguments.
- For example:

```java
// get the request dispatcher object
RequestDispatcher rd = request.getRequestDispatcher("/anotherServlet");

// forward the request and response to another servlet
rd.forward(request, response);
```

- To use the **sendRedirect** method, the servlet simply calls the method on the response object, passing the URL of the new resource as an argument.
- For example:

```java
// send a redirect response to the client browser
response.sendRedirect("https://www.example.com/index.html");
```

- Some advantages and disadvantages of the two methods are:

| Method | Advantages | Disadvantages |
| --- | --- | --- |
| forward | - Faster and more efficient, as it does not involve the client browser. | - The URL in the browser does not change, which may confuse the user. |
| | - The request and response objects are preserved and can be accessed by the new resource. | - The new resource must be on the same server as the original servlet. |
| sendRedirect | - The URL in the browser changes, which reflects the new resource. | - Slower and less efficient, as it involves the client browser. |
| | - The new resource can be on a different server than the original servlet. | - The request and response objects are lost and cannot be accessed by the new resource. |