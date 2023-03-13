Using XML processors in web page designing is a way of creating dynamic and interactive web pages that can store, transport and display data in a structured and human-readable format. XML processors are software tools that can parse, validate, transform and manipulate XML documents. XML processors can be classified into two types: XML parsers and XSLT processors.

XML parsers are responsible for reading and validating XML documents, and creating a tree-like structure that represents the elements, attributes and text nodes of the document. XML parsers can also perform operations such as searching, modifying and deleting nodes in the tree. XML parsers can be either validating or non-validating, depending on whether they check the document against a schema or a DTD (Document Type Definition).

XSLT processors are responsible for transforming XML documents into other formats, such as HTML, using a set of rules and templates defined in an XSLT stylesheet. XSLT processors can also perform operations such as sorting, filtering and grouping data in the XML document. XSLT processors can be either embedded in the browser or run on the server side.

The following diagram illustrates the basic architecture of using XML processors in web page designing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   XML Document  |     |  XSLT Stylesheet|     |  HTML Document  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        v                      v                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   XML Parser    |---->|  XSLT Processor |---->|  Web Browser    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```