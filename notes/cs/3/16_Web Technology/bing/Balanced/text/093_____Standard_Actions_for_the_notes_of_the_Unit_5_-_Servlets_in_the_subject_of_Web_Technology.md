### Standard Actions

- Standard actions are JSP elements that use XML syntax to control the behavior of the servlet engine.
- Standard actions can perform tasks such as including a file, reusing a bean component, forwarding to another page, setting a response status, etc.
- Standard actions are re-evaluated each time the page is accessed, unlike directives.
- Standard actions have the following general syntax: `<prefix:tagname attribute="value" />`.
- The prefix is usually `jsp`, but it can be changed by using the `xmlns` attribute in the root element of the JSP page.
- The tagname is the name of the standard action, such as `include`, `forward`, `useBean`, etc.
- The attribute is the name of a parameter that specifies some information for the standard action, such as `file`, `page`, `id`, `class`, etc.
- The value is the value of the attribute, usually enclosed in double quotes or single quotes.
- There are 12 types of standard actions in JSP, as follows:

  - `<jsp:include>`: Includes the content of another resource (such as a file or a servlet) at the time of request processing.
  - `<jsp:forward>`: Forwards the current request to another resource (such as a file or a servlet) for further processing.
  - `<jsp:param>`: Specifies a name-value pair as a parameter for the `<jsp:include>` or `<jsp:forward>` actions.
  - `<jsp:plugin>`: Generates the necessary HTML code to invoke an applet or a JavaBean component in the browser.
  - `<jsp:fallback>`: Specifies the content to be displayed in the browser if the `<jsp:plugin>` action fails.
  - `<jsp:useBean>`: Creates or reuses a JavaBean component and associates it with an id attribute.
  - `<jsp:setProperty>`: Sets the properties of a JavaBean component created by the `<jsp:useBean>` action.
  - `<jsp:getProperty>`: Gets the properties of a JavaBean component created by the `<jsp:useBean>` action and displays them in the output.
  - `<jsp:attribute>`: Specifies a dynamic attribute value for a custom action or a standard action that accepts a body, such as `<jsp:element>` or `<jsp:body>`.
  - `<jsp:body>`: Specifies the body content for a custom action or a standard action that accepts a body, such as `<jsp:element>` or `<jsp:plugin>`.
  - `<jsp:element>`: Creates an XML element dynamically and adds it to the output.
  - `<jsp:text>`: Specifies text data that may contain characters that are otherwise interpreted as JSP syntax, such as `<`, `>`, `%`, etc.

- Each servlet should have one to four actions, named `doDelete`, `doGet`, `doPost` and `doPut`.
- These actions correspond to the HTTP methods `DELETE`, `GET`, `POST` and `PUT`, and they build a RESTful API.
- The `doGet` action is used to handle requests that only retrieve data, such as displaying a web page or an image.
- The `doPost` action is used to handle requests that modify data, such as submitting a form or uploading a file.
- The `doPut` action is used to handle requests that create or replace data, such as creating a new resource or updating an existing one.
- The `doDelete` action is used to handle requests that delete data, such as removing a resource or a record.
- The servlet engine invokes the appropriate action based on the HTTP method of the request.