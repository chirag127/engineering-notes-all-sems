#### Standard Actions in Servlets

Standard actions in Servlets are predefined tags that are used to perform common tasks. They are used to control the behavior of the servlet engine. These actions are defined by the JavaServer Pages (JSP) specification and are available to all JSP pages.

Here are the standard actions in Servlets:

1. **jsp:include**: This action is used to include the content of another resource, such as an HTML file or another JSP page, in the current JSP page. The included content is processed by the servlet engine before being included in the response.

2. **jsp:forward**: This action is used to forward the request to another resource, such as an HTML file or another JSP page. The forwarded resource is responsible for generating the response.

3. **jsp:param**: This action is used to add a parameter to the request. It is typically used in conjunction with the jsp:include or jsp:forward actions to pass additional information to the included or forwarded resource.

4. **jsp:plugin**: This action is used to include a Java applet or a JavaBean in the JSP page. The applet or bean is executed on the client side.

5. **jsp:useBean**: This action is used to create or locate a JavaBean. The bean can be used to store and retrieve data in the JSP page.

6. **jsp:setProperty**: This action is used to set the value of a property in a JavaBean. The property must have a corresponding setter method.

7. **jsp:getProperty**: This action is used to retrieve the value of a property from a JavaBean. The property must have a corresponding getter method.

These standard actions provide a convenient way to perform common tasks in JSP pages. They can be used to simplify the development of web applications and improve code reuse.