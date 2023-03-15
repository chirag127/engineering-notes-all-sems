#### Standard Actions in Servlets

- Standard actions are JSP elements that use the construct `<prefix:tagname>` in XML syntax to control the behavior of the servlet engine.
- Standard actions can perform tasks such as dynamically inserting a file, reusing the beans components, forwarding the user to another page, etc.
- Standard actions are re-evaluated each time the page is accessed, unlike directives.
- There are 12 types of standard actions in JSP, as follows:

  - `<jsp:include>`: Includes the content of another resource (such as a file or a servlet) at the request time.
  - `<jsp:forward>`: Forwards the request to another resource (such as a file or a servlet) and terminates the current page.
  - `<jsp:param>`: Specifies a parameter for the `<jsp:include>` or `<jsp:forward>` action.
  - `<jsp:plugin>`: Generates the browser-specific code to include an applet or a bean.
  - `<jsp:fallback>`: Specifies the content to be displayed if the browser does not support the `<jsp:plugin>` action.
  - `<jsp:useBean>`: Creates or locates a bean object and assigns it to a variable in a specified scope.
  - `<jsp:setProperty>`: Sets the properties of a bean object using either the request parameters or the specified values.
  - `<jsp:getProperty>`: Gets the value of a property of a bean object and writes it to the output stream.
  - `<jsp:attribute>`: Defines a dynamic attribute for a custom action or a standard action that accepts dynamic attributes.
  - `<jsp:body>`: Defines a body for a custom action or a standard action that accepts a body.
  - `<jsp:text>`: Defines a template text for a custom action or a standard action that accepts a body.
  - `<jsp:expression>`: Evaluates an expression and writes the result to the output stream.

- Each standard action element consists of a start tag, `<prefix:tagname>`, and an end tag of the same name, `</prefix:tagname>`.
- The start tag may contain named attributes, separated from their corresponding value by equal signs.
- The value is typically surrounded by double quotes or by single quotes.
- Each servlet should have one to four actions, named `doDelete`, `doGet`, `doPost` and `doPut`.
- These names correspond to the HTTP method names `DELETE`, `GET`, `POST` and `PUT`.
- Together they build a RESTful API that uses the full power of HTTP.