### Standard Actions

- Standard actions are JSP elements that use XML syntax to control the behavior of the servlet engine.
- Standard actions can perform tasks such as including a file, reusing a bean component, forwarding to another page, setting the content type, etc.
- Standard actions are re-evaluated each time the page is accessed, unlike directives.
- Standard actions have the following general syntax: `<prefix:tagname attribute="value" />`.
- The prefix is usually `jsp`, but it can be changed by using the `xmlns` attribute in the `jsp:root` element.
- The tagname is the name of the standard action, such as `include`, `forward`, `useBean`, etc.
- The attribute is the name of a parameter that specifies some information for the action, such as `file`, `page`, `id`, `class`, etc.
- The value is the value of the attribute, usually enclosed in double quotes or single quotes.
- There are 12 types of standard actions in JSP, as follows:

  - `jsp:include`: Includes the content of another resource (such as a file or a servlet) at the time of request processing.
  - `jsp:forward`: Forwards the current request to another resource (such as a file or a servlet) and terminates the current page.
  - `jsp:param`: Specifies a name-value pair for a parameter to be passed to the `jsp:include` or `jsp:forward` action.
  - `jsp:plugin`: Generates the necessary HTML code to invoke an applet or a JavaBean component.
  - `jsp:fallback`: Specifies the content to be displayed if the browser does not support the `jsp:plugin` action.
  - `jsp:useBean`: Creates or locates a JavaBean component and associates it with a scripting variable.
  - `jsp:setProperty`: Sets the properties of a JavaBean component using either the request parameters or the specified values.
  - `jsp:getProperty`: Gets the value of a property of a JavaBean component and inserts it into the output.
  - `jsp:attribute`: Specifies the value of an attribute for a custom action or a standard action that accepts a body.
  - `jsp:body`: Specifies the body content for a custom action or a standard action that accepts a body.
  - `jsp:text`: Specifies the text content for a custom action or a standard action that accepts a body.
  - `jsp:output`: Specifies the output settings for the current JSP page, such as the content type, the buffer size, and the error page.

- Each servlet should have one to four actions, named `doDelete`, `doGet`, `doPost` and `doPut`, corresponding to the HTTP methods `DELETE`, `GET`, `POST` and `PUT`.
- These actions form a RESTful API that uses the full power of HTTP to interact with server resources.