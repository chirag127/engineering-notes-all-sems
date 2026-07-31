A DTD (Document Type Definition) is a set of rules that defines the structure and the legal elements and attributes of an XML document. A DTD can be declared internally or externally to the XML document. A DTD can be used to validate the XML document against the rules specified in the DTD.

A possible ASCII diagram for DTD in web page designing is:

```
+---------------------+      +---------------------+
|                     |      |                     |
|    XML Document     |      |    DTD Document     |
|                     |      |                     |
+---------------------+      +---------------------+
|                     |      |                     |
|  <?xml version="1.0"|      |  <!ELEMENT book     |
|  encoding="UTF-8"?> |      |  (title,author,     |
|                     |      |  price)>            |
|  <!DOCTYPE book     |      |                     |
|  SYSTEM "book.dtd"> |      |  <!ELEMENT title    |
|                     |      |  (#PCDATA)>         |
|  <book>             |      |                     |
|    <title>XML       |      |  <!ELEMENT author   |
|    Tutorial</title> |      |  (#PCDATA)>         |
|    <author>John     |      |                     |
|    Doe</author>     |      |  <!ELEMENT price    |
|    <price>9.99      |      |  (#PCDATA)>         |
|    </price>         |      |                     |
|  </book>            |      |                     |
|                     |      |                     |
+---------------------+      +---------------------+
          |                           ^
          |                           |
          |                           |
          |                           |
          +---------------------------+
              Validation using DTD
```