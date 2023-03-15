#### Directives in Servlets

Directives are instructions that tell the container how to translate and process a JSP page. They affect the overall structure of the servlet class that is generated from the JSP page. Directives can have one or more attributes that are separated by commas and act as key-value pairs. The syntax of a directive is:

```jsp
<%@ directive attribute="value" %>
```

There are three types of directives in JSP:

- The **page** directive defines page-specific attributes, such as the scripting language, the content type, the error page, and the import statements.
- The **include** directive includes the content of another file, such as an HTML or a JSP file, during the translation phase. This is different from the `<jsp:include>` action, which includes the content of another file during the request processing phase.
- The **taglib** directive declares a custom tag library that can be used in the JSP page. It specifies the prefix and the URI of the tag library.