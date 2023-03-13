Custom tag libraries in servlets are a way of creating reusable components that can be used in JSP pages. Custom tag libraries are defined in a tag library descriptor (TLD) file, which specifies the name, attributes, and implementation class of each custom tag. Custom tag libraries can be used in JSP pages by declaring a taglib directive with the URI and prefix of the library.

The following diagram illustrates the basic architecture of a custom tag library in servlets:

```
+------------------+        +-----------------+
| JSP page         |        | TLD file        |
|                  |        |                 |
| <%@ taglib       |        | <taglib>        |
| uri="my-lib.tld" |------->|   <tag>         |
| prefix="my" %>   |        |     <name>foo   |
|                  |        |     </name>     |
| <my:foo          |        |     <tag-class> |
| attr="value" />  |        |       FooTag    |
|                  |        |     </tag-class>|
+------------------+        |     <attribute> |
                           |       <name>attr|
                           |       </name>    |
                           |     </attribute> |
                           |   </tag>         |
                           | </taglib>        |
                           +-----------------+

                               |
                               |
                               v

                           +-----------------+
                           | Tag class       |
                           |                 |
                           | public class    |
                           | FooTag extends  |
                           | TagSupport {    |
                           |   // implement  |
                           |   // tag logic  |
                           | }               |
                           +-----------------+
```