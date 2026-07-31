### Implicit Objects

- Implicit objects are Java objects that are created by the servlet container during the translation phase of JSP, when JSP is converted to servlet .
- These objects can be directly used in scriptlets that go in the service method of the generated servlet.
- They are created by the container automatically, and they can be accessed using predefined variables.
- There are 9 implicit objects in JSP: out, request, response, config, session, application, page, pageContext, and exception .
- The implicit objects are instances of different Java classes or interfaces that provide various functionalities to the JSP page .
- The implicit objects are not available in servlets, but they can be accessed programmatically by using the request and response objects.
- The implicit objects are useful for accessing the information about the client request, the server response, the servlet configuration, the session management, the application context, the current page, the page context, and the exception handling.