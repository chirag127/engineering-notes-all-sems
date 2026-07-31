### Redirecting Requests to Other Resources in Servlets

- Redirecting requests to other resources in servlets means sending the response to another web resource, such as a servlet, a JSP page, or an HTML file, instead of the original servlet that received the request.
- There are two ways to redirect requests to other resources in servlets: using the `sendRedirect()` method of the `HttpServletResponse` interface, or using the `forward()` method of the `RequestDispatcher` interface.
- The `sendRedirect()` method works on the client side, meaning that it instructs the browser to create a new request to the specified resource. The URL of the new resource is visible in the browser's address bar. The new resource can be inside or outside the server.
- The `forward()` method works on the server side, meaning that it transfers the control to the specified resource without involving the browser. The URL of the original resource remains in the browser's address bar. The new resource must be inside the same web application.
- The syntax of the `sendRedirect()` method is:

```java
response.sendRedirect(String url);
```

- The syntax of the `forward()` method is:

```java
RequestDispatcher rd = request.getRequestDispatcher(String url);
rd.forward(request, response);
```

- The advantages of using the `sendRedirect()` method are:
  - It can redirect to any resource, even outside the server.
  - It can avoid the problem of double submission, since it creates a new request.
  - It can preserve the original request parameters, since they are appended to the new URL.
- The disadvantages of using the `sendRedirect()` method are:
  - It is slower, since it involves two round trips between the client and the server.
  - It consumes more bandwidth, since it sends the entire response header and body to the client.
  - It cannot access the request attributes, since they are lost in the new request.
- The advantages of using the `forward()` method are:
  - It is faster, since it involves only one round trip between the client and the server.
  - It consumes less bandwidth, since it does not send the response header and body to the client.
  - It can access the request attributes, since they are preserved in the same request.
- The disadvantages of using the `forward()` method are:
  - It can only forward to resources within the same web application.
  - It can cause the problem of double submission, since it does not create a new request.
  - It cannot preserve the original request parameters, since they are overwritten by the new URL.

- A possible mnemonic to remember the difference between the two methods is:

  - **S**end**R**edirect: **S**low, **R**equest lost, **S**ee new URL
  - **F**orward: **F**ast, **F**ull access, **F**orget old URL

- An example of using the `sendRedirect()` method is:

```java
// In the original servlet
response.sendRedirect("https://www.google.com");
```

- An example of using the `forward()` method is:

```java
// In the original servlet
RequestDispatcher rd = request.getRequestDispatcher("/anotherServlet");
rd.forward(request, response);
```