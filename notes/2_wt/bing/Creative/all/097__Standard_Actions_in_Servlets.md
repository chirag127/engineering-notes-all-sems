#### Standard Actions in Servlets

- Standard actions are predefined tags that perform some common tasks in servlets.
- They are used to control the flow of execution, include other resources, or customize the generated output.
- They start with the prefix `jsp:` and follow the syntax `<jsp:action_name attribute="value" />`.
- Some of the standard actions are:

  - `<jsp:include>`: This action includes the content of another resource, such as a HTML file, a JSP page, or a servlet, at the request time. It can pass parameters to the included resource using nested `<jsp:param>` tags. For example:

    ```jsp
    <jsp:include page="header.html" />
    <h1>Welcome to my website</h1>
    <jsp:include page="footer.html">
      <jsp:param name="year" value="2023" />
    </jsp:include>
    ```

  - `<jsp:forward>`: This action forwards the current request to another resource, such as a HTML file, a JSP page, or a servlet. It can pass parameters to the forwarded resource using nested `<jsp:param>` tags. The original request and response objects are passed to the forwarded resource. For example:

    ```jsp
    <%
      String name = request.getParameter("name");
      if (name == null || name.isEmpty()) {
        // forward to an error page if name is missing
        out.println("Name is required");
        %>
        <jsp:forward page="error.jsp" />
        <%
      } else {
        // forward to a welcome page if name is present
        %>
        <jsp:forward page="welcome.jsp">
          <jsp:param name="name" value="<%= name %>" />
        </jsp:forward>
        <%
      }
    %>
    ```

  - `<jsp:plugin>`: This action generates the necessary HTML code to include an applet or a JavaBean component in the output. It can specify the type, code, codebase, archive, width, height, align, and params attributes for the applet or the component. For example:

    ```jsp
    <jsp:plugin type="applet" code="Clock.class" codebase="/applets" width="200" height="200">
      <jsp:params>
        <jsp:param name="bgcolor" value="yellow" />
        <jsp:param name="fgcolor" value="black" />
      </jsp:params>
    </jsp:plugin>
    ```

  - `<jsp:useBean>`: This action creates or locates a JavaBean component and assigns it to a variable in a specified scope. It can specify the id, class, type, scope, and beanName attributes for the bean. For example:

    ```jsp
    <jsp:useBean id="user" class="com.example.User" scope="session" />
    <%
      // set the properties of the user bean
      user.setName("Alice");
      user.setEmail("alice@example.com");
    %>
    ```

  - `<jsp:setProperty>`: This action sets the properties of a JavaBean component using either the request parameters or the specified values. It can specify the name, property, param, and value attributes for the property. For example:

    ```jsp
    <jsp:useBean id="user" class="com.example.User" scope="session" />
    <jsp:setProperty name="user" property="*" />
    <!-- this sets all the properties of the user bean that match the request parameters -->
    <jsp:setProperty name="user" property="age" value="25" />
    <!-- this sets the age property of the user bean to 25 -->
    ```

  - `<jsp:getProperty>`: This action gets the value of a property of a JavaBean component and writes it to the output. It can specify the name and property attributes for the property. For example:

    ```jsp
    <jsp:useBean id="user" class="com.example.User" scope="session" />
    <p>Name: <jsp:getProperty name="user" property="name" /></p>
    <p>Email: <jsp:getProperty name="user" property="email" /></p>
    <p>Age: <jsp:getProperty name="user" property="age" /></p>
    ```