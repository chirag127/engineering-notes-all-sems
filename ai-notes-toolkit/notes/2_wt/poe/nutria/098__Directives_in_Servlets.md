
#### Directives in Servlets

1. **ServletConfig**: This object is used to pass initialization parameters to a servlet. It is created by the web container when the servlet is initialized.

2. **ServletContext**: This object is used to communicate with the servlet's environment. It is created when the web application is deployed and is shared by all servlets in the web application.

3. **RequestDispatcher**: This object is used to forward requests from a servlet to another resource (servlet, JSP file, or HTML file) on the server.

4. **ServletRequest**: This object is used to encapsulate the information associated with an HTTP request. It is created by the web container and passed to a servlet's service method.

5. **ServletResponse**: This object is used to encapsulate the information associated with an HTTP response. It is created by the servlet and passed to the web container.