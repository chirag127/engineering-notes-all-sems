### Redirecting Requests to Other Resources

- Sometimes, a servlet may need to delegate the request to another resource, such as another servlet, a JSP page, or an HTML file, on the same or a different server.
- This can be done by using two methods: `sendRedirect()` and `forward()`.
- `sendRedirect()` method:
  - It is defined in the `HttpServletResponse` interface.
  - It instructs the client browser to send a new request to the specified URL.
  - The URL can be relative or absolute, and can refer to any resource on the same or a different server.
  - The original request and response objects are discarded, and a new request and response are created.
  - The new URL is visible in the browser address bar, and the browser history is updated.
  - It is useful for redirecting to external resources, or when the response has already been committed.
- `forward()` method:
  - It is defined in the `RequestDispatcher` interface, which can be obtained from the `ServletRequest` or `ServletContext` objects.
  - It transfers the control of the request to another resource on the same server, without the client's knowledge.
  - The URL remains the same in the browser address bar, and the browser history is not updated.
  - The original request and response objects are preserved, and can be accessed by the destination resource.
  - It is useful for redirecting to internal resources, or when the response has not been committed.