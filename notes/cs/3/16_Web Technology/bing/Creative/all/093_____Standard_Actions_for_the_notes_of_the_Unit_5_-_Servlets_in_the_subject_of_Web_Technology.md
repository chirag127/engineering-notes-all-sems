# Standard Actions

Standard actions are JSP elements that use XML syntax to control the behavior of the servlet engine. They can perform tasks such as including other files, reusing JavaBeans components, forwarding requests to other pages, and invoking custom tags.

There are 12 types of standard actions in JSP:

- `<jsp:include>`: This action inserts the content of another resource (such as a file or a servlet) into the current page at request time.
- `<jsp:forward>`: This action transfers the control of the request to another resource (such as a file or a servlet) and terminates the execution of the current page.
- `<jsp:param>`: This action specifies a parameter for the `<jsp:include>` or `<jsp:forward>` actions. It can only be used as a child of these actions.
- `<jsp:plugin>`: This action generates the necessary HTML code to run an applet on the client browser. It can also provide an alternative content if the browser does not support applets.
- `<jsp:useBean>`: This action creates or locates a JavaBean component and associates it with a scripting variable that can be accessed from the page.
- `<jsp:setProperty>`: This action sets the properties of a JavaBean component using either the request parameters or the specified values.
- `<jsp:getProperty>`: This action retrieves the value of a property of a JavaBean component and displays it in the page.
- `<jsp:attribute>`: This action defines a dynamic attribute for a custom tag. It can only be used as a child of a custom tag invocation.
- `<jsp:body>`: This action defines a dynamic body for a custom tag. It can only be used as a child of a custom tag invocation.
- `<jsp:text>`: This action allows the use of literal text containing characters that would otherwise be interpreted as JSP syntax, such as `<`, `>`, or `%`.
- `<jsp:output>`: This action controls the output settings of the page, such as the content type, the buffer size, and the doctype declaration.
- `<jsp:element>`: This action creates an XML element dynamically and adds it to the page output. It can have `<jsp:attribute>` actions as children to define the element's attributes.