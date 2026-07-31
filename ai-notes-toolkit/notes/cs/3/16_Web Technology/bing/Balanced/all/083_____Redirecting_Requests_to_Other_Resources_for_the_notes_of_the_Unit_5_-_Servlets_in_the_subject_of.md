# Redirecting Requests to Other Resources

- Sometimes, a servlet may need to redirect the request to another resource, such as another servlet, a JSP page, or an HTML file.
- There are two ways to redirect a request in servlets: using the `sendRedirect()` method of the `HttpServletResponse` interface, or using the `forward()` method of the `RequestDispatcher` interface.
- Both methods have different advantages and disadvantages, and they work differently on the client and server side.

## sendRedirect() Method

- The `sendRedirect()` method of the `HttpServletResponse` interface can be used to redirect the response to another resource, i.e. it may be a servlet, JSP or HTML file.
- It works on the client side because it uses the URL bar of the browser to make another request. Hence, it can work inside and outside the server.
- The syntax of the `sendRedirect()` method is:

```java
public void sendRedirect(String url) throws IOException
```

- The `url` parameter can be either relative or absolute. If it is relative, it is resolved to the current request URL. If it is absolute, it is used as it is.
- The `sendRedirect()` method has some drawbacks, such as:

  - It consumes more network bandwidth and processing time, as it involves two requests and responses.
  - It loses the original request parameters and attributes, as it creates a new request object.
  - It exposes the redirected URL to the client, which may not be desirable in some cases.

## forward() Method

- The `forward()` method of the `RequestDispatcher` interface can be used to forward the request to another resource within the same server.
- It works on the server side because it uses the same request and response objects. Hence, it cannot work outside the server.
- The syntax of the `forward()` method is:

```java
public void forward(ServletRequest request, ServletResponse response) throws ServletException, IOException
```

- The `request` and `response` parameters are the same objects that are passed to the original servlet. The `RequestDispatcher` object can be obtained from the `request` object using the `getRequestDispatcher()` method, or from the `ServletContext` object using the `getNamedDispatcher()` method.
- The `forward()` method has some advantages, such as:

  - It consumes less network bandwidth and processing time, as it involves only one request and response.
  - It preserves the original request parameters and attributes, as it uses the same request object.
  - It hides the forwarded URL from the client, which may be desirable in some cases.