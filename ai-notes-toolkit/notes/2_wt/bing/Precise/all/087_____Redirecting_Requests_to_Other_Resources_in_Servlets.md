### Redirecting Requests to Other Resources in Servlets

1. Servlets can redirect requests to other resources, such as another servlet, a JSP page, or an HTML file.
2. This can be done using the `sendRedirect` method of the `HttpServletResponse` object.
3. The `sendRedirect` method takes a single argument, which is the URL of the resource to which the request should be redirected.
4. The URL can be absolute or relative to the current request.
5. When the `sendRedirect` method is called, the server sends an HTTP response to the client with a status code of `302` (Found) and a `Location` header containing the URL of the new resource.
6. The client then sends a new request to the URL specified in the `Location` header, effectively redirecting the request to the new resource.
7. This process is transparent to the user, who sees only the final resource in their browser.

Example:
```java
response.sendRedirect("/newResource");
```

Advantages:
- Allows for dynamic selection of the resource to be displayed based on runtime conditions.
- Can be used to redirect the user to a login page if they are not authenticated.

Disadvantages:
- Requires an additional round trip between the client and the server.
- The original request parameters are lost and must be manually passed to the new resource if needed.

Mnemonic:
- **S**ervlets **R**edirect **R**equests using **S**end**R**edirect method of **H**ttp**S**ervlet**R**esponse object. (SRRSRHSR)