#### Directives in Servlets

Directives are instructions that tell the container how to translate and process a JSP page. They affect the overall structure and behavior of the servlet class that is generated from the JSP page. Directives can have one or more attributes that are separated by commas and act as key-value pairs. The syntax of a directive is:

```jsp
<%@ directive attribute="value" %>
```

There are three types of directives in JSP:

- **page directive**: It defines page-specific attributes such as language, session, error page, buffer size, etc. It can be used multiple times in a JSP page, but it is recommended to use it only once at the top of the page. The syntax of the page directive is:

```jsp
<%@ page attribute="value" %>
```

- **include directive**: It includes the content of another file (such as HTML, JSP, or plain text) during the translation phase. It is useful for reusing common code or header/footer sections in multiple JSP pages. The syntax of the include directive is:

```jsp
<%@ include file="filename" %>
```

- **taglib directive**: It declares a custom tag library that can be used in the JSP page. It specifies the prefix and the URI of the tag library. The syntax of the taglib directive is:

```jsp
<%@ taglib prefix="prefix" uri="uri" %>
```

For example, to use the JSTL core library, we can use the following taglib directive:

```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
```