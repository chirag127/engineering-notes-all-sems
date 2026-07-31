Directives in Servlets are instructions that tell the container how to process and manage certain parts of the JSP code. They affect the overall structure of the servlet class that is generated from the JSP file. There are three types of directives in JSP: page, include and taglib.

The page directive defines attributes for the entire JSP page, such as the language, content type, error page, buffer size, etc. It has the following syntax:

<%@ page attribute="value" %>

The include directive includes the content of another file at the translation time of the JSP page. It is useful for reusing common code or HTML fragments. It has the following syntax:

<%@ include file="filename" %>

The taglib directive declares a custom tag library that can be used in the JSP page. It defines a prefix for the tag and a URI for the tag library descriptor. It has the following syntax:

<%@ taglib prefix="prefix" uri="uri" %>

A possible diagram for the directives in servlets is:

```
+-----------------+       +-----------------+       +-----------------+
| JSP Page        |       | JSP Page        |       | JSP Page        |
|                 |       |                 |       |                 |
| <%@ page ... %> |       | <%@ include ... |       | <%@ taglib ...  |
|                 |       | %>              |       | %>              |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+-----------------+       +-----------------+       +-----------------+
| Servlet Class   |       | Servlet Class   |       | Servlet Class   |
|                 |       |                 |       |                 |
| page attributes |       | included file   |       | custom tag      |
|                 |       | content         |       | library         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```