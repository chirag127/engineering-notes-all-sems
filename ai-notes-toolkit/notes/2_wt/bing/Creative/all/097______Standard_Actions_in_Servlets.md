#### Standard Actions in Servlets

- Standard actions are predefined tags that perform some common tasks in JSP pages.
- They start with `<jsp:` and end with `/>`.
- They can be used to include other resources, forward requests, set or get properties of JavaBeans, use plugins, etc.
- Some of the standard actions are:

  - `<jsp:include>`: This action includes the content of another resource (such as a JSP page, an HTML file, or a servlet) at the time of request processing. It can take two attributes: `page` (the relative URL of the resource to be included) and `flush` (a boolean value that indicates whether the output buffer should be flushed before including the resource). For example:

    ```jsp
    <jsp:include page="header.jsp" flush="true"/>
    ```

  - `<jsp:forward>`: This action forwards the current request to another resource (such as a JSP page, an HTML file, or a servlet) for further processing. It can take one attribute: `page` (the relative URL of the resource to be forwarded to). For example:

    ```jsp
    <jsp:forward page="error.jsp"/>
    ```

  - `<jsp:useBean>`: This action creates an instance of a JavaBean or locates an existing instance of a JavaBean in a given scope. It can take four attributes: `id` (the name of the bean instance), `class` (the fully qualified name of the bean class), `type` (the fully qualified name of the bean interface or superclass), and `scope` (the scope of the bean instance, which can be `page`, `request`, `session`, or `application`). For example:

    ```jsp
    <jsp:useBean id="user" class="com.example.User" scope="session"/>
    ```

  - `<jsp:setProperty>`: This action sets the value of a property of a JavaBean. It can take three attributes: `name` (the name of the bean instance), `property` (the name of the property to be set), and `value` (the value of the property to be set). Alternatively, it can use the `param` attribute to set the property value from a request parameter with the same name as the property. For example:

    ```jsp
    <jsp:setProperty name="user" property="name" value="Alice"/>
    <jsp:setProperty name="user" property="age" param="age"/>
    ```

  - `<jsp:getProperty>`: This action gets the value of a property of a JavaBean and writes it to the output stream. It can take two attributes: `name` (the name of the bean instance) and `property` (the name of the property to be retrieved). For example:

    ```jsp
    <p>Welcome, <jsp:getProperty name="user" property="name"/>!</p>
    <p>Your age is <jsp:getProperty name="user" property="age"/>.</p>
    ```

  - `<jsp:plugin>`: This action generates the necessary HTML code to include an applet or a Java Web Start application in a JSP page. It can take several attributes, such as `type` (the type of the plugin, which can be `applet` or `bean`), `code` (the name of the applet class or the serialized bean), `codebase` (the URL of the directory where the applet class or the bean is located), `width` and `height` (the dimensions of the applet or the bean), `align` (the alignment of the applet or the bean), `archive` (the list of JAR files containing the applet class or the bean and its dependencies), `jreversion` (the minimum version of the Java Runtime Environment required to run the applet or the bean), etc. For example:

    ```jsp
    <jsp:plugin type="applet" code="HelloApplet.class" codebase="/applets" width="300" height="200" jreversion="1.8.0"/>
    ```

- A mnemonic to remember some of the standard actions is: **IF UPS** (Include, Forward, UseBean, SetProperty, GetProperty).