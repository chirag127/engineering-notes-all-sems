A Document Type Definition (DTD) is a set of markup declarations that define the structure and the legal elements and attributes of an XML document. A DTD can be declared inside an XML document as an internal DTD, or in an external file as an external DTD.

### Document type definition in Web Page Designing

The following diagram illustrates the basic architecture of a DTD in web page designing:

```
+-----------------+      +-----------------+
|                 |      |                 |
|  XML Document   |      |  External DTD   |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  <!DOCTYPE ...  |----->|  <!ELEMENT ...  |
|  SYSTEM "..." > |      |  <!ATTLIST ...  |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  <root>         |      |                 |
|    <child> ...  |      |                 |
|  </root>        |      |                 |
|                 |      |                 |
+-----------------+      +-----------------+
```

The DTD declaration in the XML document specifies the root element and the location of the external DTD file. The external DTD file contains the element and attribute declarations that define the structure and the legal elements and attributes of the XML document. The XML document contains the actual data that conforms to the DTD.