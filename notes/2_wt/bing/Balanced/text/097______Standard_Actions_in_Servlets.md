#### Standard Actions in Servlets

- Standard actions are predefined tags that perform some common tasks in JSP pages.
- They are used to control the execution flow, include other resources, or manipulate JavaBeans components.
- They start with `<jsp:` and end with `/>`.
- Some of the standard actions are:

  - `<jsp:include>`: This action includes the content of another resource, such as a JSP page, an HTML file, or a servlet, at the request time.
  - `<jsp:forward>`: This action forwards the request to another resource, such as a JSP page, an HTML file, or a servlet, and terminates the current page.
  - `<jsp:param>`: This action specifies a parameter for the `<jsp:include>` or `<jsp:forward>` actions.
  - `<jsp:plugin>`: This action generates the necessary HTML code to include an applet or a JavaBean in the JSP page.
  - `<jsp:useBean>`: This action declares and instantiates a JavaBean component and associates it with a scope attribute.
  - `<jsp:setProperty>`: This action sets the properties of a JavaBean component using either the request parameters or the specified values.
  - `<jsp:getProperty>`: This action retrieves the property value of a JavaBean component and displays it in the JSP page.
  - `<jsp:attribute>`: This action defines a dynamic attribute for the `<jsp:element>` action.
  - `<jsp:body>`: This action defines a body for the `<jsp:element>` action or the `<jsp:declaration>`, `<jsp:expression>`, or `<jsp:scriptlet>` actions.
  - `<jsp:element>`: This action creates an XML element dynamically and adds it to the JSP page output.
  - `<jsp:text>`: This action allows the use of literal text in a JSP page without escaping the special characters.
  - `<jsp:output>`: This action controls the output settings for the JSP page, such as the buffering size, the content type, and the character encoding.
  - `<jsp:directive.page>`: This action specifies the page-level directives that affect the overall structure and behavior of the JSP page, such as the import statements, the scripting language, the error page, and the session management.
  - `<jsp:directive.include>`: This action includes the content of another file, such as a JSP page or an HTML file, at the translation time.
  - `<jsp:directive.tag>`: This action specifies the tag-level directives that affect the behavior of a custom tag, such as the tag name, the body content, and the attributes.
  - `<jsp:directive.attribute>`: This action specifies an attribute for a custom tag.
  - `<jsp:directive.variable>`: This action declares a scripting variable for a custom tag.
  - `<jsp:doBody>`: This action invokes the body of a simple tag handler or a tag file.