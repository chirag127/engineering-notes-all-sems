# Standard Actions

- Standard actions are JSP elements that use XML syntax to control the behavior of the servlet engine.
- Standard actions can perform tasks such as including a file, reusing a bean component, forwarding to another page, setting a property, etc.
- Standard actions are re-evaluated each time the page is accessed, unlike directives.
- Standard actions have a start tag and an end tag with a prefix of `jsp:` and an optional body.
- Standard actions can have named attributes with values surrounded by double quotes or single quotes.
- There are 12 types of standard actions in JSP:

  - `<jsp:include>`: Includes the content of another resource (such as a file or a servlet) at the request time.
  - `<jsp:forward>`: Forwards the request to another resource (such as a file or a servlet) and terminates the current page.
  - `<jsp:param>`: Specifies a parameter for the `<jsp:include>` or `<jsp:forward>` action.
  - `<jsp:plugin>`: Generates the necessary HTML code to run an applet in the browser.
  - `<jsp:useBean>`: Creates or locates a bean component and assigns it to a variable.
  - `<jsp:setProperty>`: Sets the value of a property of a bean component.
  - `<jsp:getProperty>`: Gets the value of a property of a bean component and writes it to the output.
  - `<jsp:expression>`: Evaluates an expression and writes the result to the output.
  - `<jsp:scriptlet>`: Contains a block of Java code that is executed when the page is requested.
  - `<jsp:declaration>`: Contains a block of Java code that declares variables or methods for the page.
  - `<jsp:directive.page>`: Provides information about the page to the servlet engine.
  - `<jsp:directive.include>`: Includes the content of another file at the translation time.

- Each servlet should have one to four actions, named `doDelete`, `doGet`, `doPost` and `doPut`, corresponding to the HTTP methods `DELETE`, `GET`, `POST` and `PUT`.
- These actions build a RESTful API that uses the full power of HTTP.
- Some standard actions, such as `<jsp:plugin>`, `<jsp:expression>`, `<jsp:scriptlet>` and `<jsp:declaration>`, are considered obsolete or unnecessary when using a proper MVC design or framework.