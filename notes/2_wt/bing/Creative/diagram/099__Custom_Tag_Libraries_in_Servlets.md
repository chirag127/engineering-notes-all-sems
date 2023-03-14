Custom tag libraries in servlets are a way to create reusable components that can be used in JSP pages. They allow you to define custom tags that can perform various tasks, such as accessing databases, generating HTML, or invoking Java code. Custom tag libraries are composed of two parts: a tag library descriptor (TLD) file that defines the syntax and attributes of the custom tags, and one or more Java classes that implement the logic of the custom tags.

The following diagram illustrates the basic architecture of a custom tag library in servlets:

```
+------------------+      +-----------------+      +-----------------+
| JSP page         |      | TLD file        |      | Java class      |
|                  |      |                 |      |                 |
| <my:tag attr="x">|----->| <tag>           |----->| public class    |
|   ...            |      |   <name>tag</name>     |   MyTag extends |
| </my:tag>        |      |   <tag-class>   |      |   TagSupport {  |
|                  |      |     MyTag       |      |   ...           |
|                  |      |   </tag-class>  |      | }               |
+------------------+      |   <attribute>   |      +-----------------+
                          |     <name>attr</name>
                          |   </attribute>
                          | </tag>
                          +-----------------+
```

The JSP page uses the custom tag with the prefix my and the name tag. The prefix is mapped to a URI that identifies the tag library. The TLD file contains the tag definition, which specifies the name, the tag class, and the attributes of the custom tag. The tag class is a Java class that extends TagSupport or BodyTagSupport and implements the doStartTag, doEndTag, and other methods to control the tag behavior. The tag class can access the JSP page context, the request and response objects, and the tag attributes. The tag class can also invoke other JSP elements, such as expressions, scriptlets, or other custom tags.