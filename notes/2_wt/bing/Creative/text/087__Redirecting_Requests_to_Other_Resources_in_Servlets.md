### Redirecting Requests to Other Resources in Servlets

- Servlets are Java programs that run on the server-side and generate dynamic responses to the client request.
- Sometimes, a servlet may need to delegate the request to another resource, such as another servlet, a JSP page, or an HTML file, that may be inside or outside the server.
- To achieve this, servlets provide two mechanisms: **forwarding** and **redirecting**.
- Forwarding is done by using the **RequestDispatcher** interface, which is obtained from the servlet context or the request object. It allows the servlet to forward the request and response objects to another resource without changing the URL in the browser.
- Redirecting is done by using the **sendRedirect()** method of the **HttpServletResponse** interface, which is inherited from the **ServletResponse** interface. It sends a temporary redirect response to the client with the specified redirect location URL, and makes the client create a new request to get to the resource. The URL in the browser changes to the new location.
- The main differences between forwarding and redirecting are:

  - Forwarding works on the server-side, while redirecting works on the client-side.
  - Forwarding preserves the original request and response objects, while redirecting creates new ones.
  - Forwarding keeps the original URL in the browser, while redirecting changes it to the new location.
  - Forwarding can access request-scope objects, while redirecting cannot.
  - Forwarding is faster and more efficient than redirecting, as it avoids an extra round-trip between the client and the server.

- Redirecting is normally used when the servlet wants to send the client to a different server or domain, or when the servlet wants to implement the Post/Redirect/Get web development pattern, which prevents duplicate form submissions.