# Implicit Objects

- Implicit objects are Java objects that are created by the web container and are available to all the JSP pages.
- They are also called pre-defined or built-in objects.
- They are used to access the information related to a particular request, page, or application.
- They are also used to perform some common tasks such as writing data to the output stream, setting the content type, dispatching requests, etc.
- There are nine implicit objects in JSP:

  - **request**: It represents the HTTP request object and provides methods to get the request parameters, headers, cookies, etc.
  - **response**: It represents the HTTP response object and provides methods to set the response status, headers, cookies, etc.
  - **out**: It represents the JSP output stream and provides methods to write data to the response.
  - **session**: It represents the HTTP session object and provides methods to store and retrieve data across multiple requests from the same client.
  - **application**: It represents the web application context and provides methods to store and retrieve data across all the requests from all the clients.
  - **config**: It represents the servlet configuration object and provides methods to get the initialization parameters and the servlet context.
  - **pageContext**: It represents the page context object and provides methods to access the other implicit objects, page attributes, and page scope.
  - **page**: It represents the current JSP page and is equivalent to `this` keyword in Java.
  - **exception**: It represents the exception object that is thrown by the JSP page and is only available in the error pages.