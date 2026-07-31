### Implicit Objects

- Implicit objects are Java objects that are created by the servlet container during the translation phase of JSP, when JSP is converted to servlet .
- These objects can be directly used in scriptlets that go in the service method of the generated servlet.
- They are created by the container automatically, and they can be accessed using predefined variables.
- There are 9 implicit objects in JSP: out, request, response, config, session, application, page, pageContext, and exception .
- These objects are useful for accessing the information and functionality of the web application, such as the request parameters, the session attributes, the servlet context, the output stream, etc .
- Servlets do not have implicit objects, but they can access the same information and functionality by using the request and response objects that are passed as parameters to the service method.
- For example, to get the session object in a servlet, we can use the method request.getSession(), while in JSP we can use the variable session directly.