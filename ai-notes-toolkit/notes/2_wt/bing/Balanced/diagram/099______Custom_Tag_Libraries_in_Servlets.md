Custom tag libraries are a way of creating reusable components in JSP pages. They allow you to define custom actions that can be used in JSP pages, similar to HTML tags. Custom tag libraries are defined in a tag library descriptor (TLD) file, which specifies the name, attributes, and implementation class of each custom tag. Custom tag libraries can be used in JSP pages by declaring the taglib directive with the URI of the TLD file.

Here is a possible ASCII diagram for custom tag libraries in servlets:

```
+------------------+        +-----------------+
| JSP page         |        | TLD file        |
|                  |        |                 |
| <%@ taglib uri=" |------->| <taglib>        |
| /mytags.tld"     |        |   <tlib-version>|
| prefix="my" %>   |        |   <jsp-version> |
|                  |        |   <short-name>  |
| <my:hello/>      |        |   <tag>         |
|                  |        |     <name>      |
|                  |        |     <tag-class> |
+------------------+        |     <attribute> |
                            |   </tag>        |
                            | </taglib>       |
                            +-----------------+
                                   |
                                   |
                                   v
                            +-----------------+
                            | Tag class       |
                            |                 |
                            | public class    |
                            | HelloTag        |
                            | extends         |
                            | SimpleTagSupport|
                            | {               |
                            |   public void   |
                            |   doTag()       |
                            |   {             |
                            |     // tag logic|
                            |   }             |
                            | }               |
                            +-----------------+
```