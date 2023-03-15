#### Standard Actions in Servlets

Standard actions are JSP elements that control the behavior of the servlet engine. They use the XML syntax `<jsp:action>` to perform various tasks, such as including a file, reusing a bean component, forwarding to another page, etc. 

Some of the commonly used standard actions are:

- `<jsp:include>`: This action includes the content of another resource, such as a file or a servlet, at the time of request processing. It has two attributes: `page`, which specifies the relative URL of the resource to be included, and `flush`, which indicates whether the output buffer should be flushed before including the resource. For example:

```jsp
<jsp:include page="header.jsp" flush="true"/>
```

- `<jsp:forward>`: This action forwards the request to another resource, such as a file or a servlet, and terminates the current page. It has one attribute: `page`, which specifies the relative URL of the resource to be forwarded to. For example:

```jsp
<jsp:forward page="result.jsp"/>
```

- `<jsp:useBean>`: This action creates or locates a JavaBean object and assigns it to a variable in a specified scope. It has four attributes: `id`, which specifies the name of the variable, `class`, which specifies the fully qualified name of the bean class, `scope`, which specifies the scope of the variable (page, request, session, or application), and `type`, which specifies the type of the bean object. For example:

```jsp
<jsp:useBean id="user" class="com.example.User" scope="session"/>
```

- `<jsp:getProperty>`: This action retrieves the value of a property of a bean object and writes it to the output. It has two attributes: `name`, which specifies the name of the bean variable, and `property`, which specifies the name of the property to be retrieved. For example:

```jsp
<jsp:getProperty name="user" property="username"/>
```

- `<jsp:setProperty>`: This action sets the value of a property of a bean object. It has three attributes: `name`, which specifies the name of the bean variable, `property`, which specifies the name of the property to be set, and `value`, which specifies the value to be assigned to the property. Alternatively, the value can be obtained from a request parameter by using the attribute `param`. For example:

```jsp
<jsp:setProperty name="user" property="password" value="secret"/>
<jsp:setProperty name="user" property="email" param="email"/>
```

There are other standard actions, such as `<jsp:param>`, `<jsp:plugin>`, `<jsp:attribute>`, `<jsp:body>`, `<jsp:element>`, and `<jsp:text>`, that perform different functions. You can refer to the JSP specification or online tutorials for more details.