Directives in Servlets are instructions that tell the container how to handle and process certain parts of the JSP code. They affect the overall structure of the servlet class that is generated from the JSP page. There are three types of directives in JSP: page, include and taglib.

The page directive defines attributes for the entire JSP page, such as the language, content type, error page, buffer size, etc. It has the following syntax:

<%@ page attribute="value" %>

The include directive includes the content of another file at the translation time of the JSP page. It has the following syntax:

<%@ include file="filename" %>

The taglib directive declares a custom tag library that can be used in the JSP page. It has the following syntax:

<%@ taglib uri="uri" prefix="prefix" %>

The following diagram illustrates the basic architecture of a servlet that is generated from a JSP page with directives:

```
+-----------------+    +-----------------+    +-----------------+
| JSP page        |    | Servlet class   |    | Included file   |
|                 |    |                 |    |                 |
| <%@ page ... %> |    |                 |    |                 |
| <%@ include ... |    |                 |    |                 |
| %>              |    |                 |    |                 |
| <%@ taglib ...  |    |                 |    |                 |
| %>              |    |                 |    |                 |
|                 |    |                 |    |                 |
| <html>          |    |                 |    |                 |
| ...             |    |                 |    |                 |
| </html>         |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +--------------------->+                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               +--------------------->+
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               |                     |
                               +---------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |