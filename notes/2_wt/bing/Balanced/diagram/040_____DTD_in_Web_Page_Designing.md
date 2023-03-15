A Document Type Definition (DTD) describes the structure and the legal elements and attributes of an XML document. It is a set of markup declarations that define a type of document for the SGML family, like GML, SGML, HTML, XML. A DTD can be declared inside an XML document as inline or as an external reference.

A DTD consists of three parts: element declarations, attribute declarations, and entity declarations. Element declarations define the names and contents of the elements in an XML document. Attribute declarations define the names and values of the attributes for each element. Entity declarations define the names and values of the entities that can be used in an XML document.

A DTD can be represented as a tree structure, where each node is an element, attribute, or entity declaration. The root node is the document element, which is the name of the XML document type. The branches are the element declarations, which can have sub-branches for their child elements. The leaves are the attribute and entity declarations, which can have values or references to other entities.

Here is an example of a DTD for a simple XML document that contains a list of books:

### DTD in Web Page Designing

```
+-----------------+
| !DOCTYPE books  |
+-----------------+
        |
        |
        v
+-----------------+
| ELEMENT books   |
+-----------------+
        |
        |
        v
+-----------------+
| ELEMENT book    |
+-----------------+
        |
        |
        v
+-----------------+     +-----------------+
| ELEMENT title   |     | ELEMENT author  |
+-----------------+     +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+     +-----------------+
| ELEMENT name    |     | ELEMENT name    |
+-----------------+     +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+     +-----------------+
| ELEMENT first   |     | ELEMENT first   |
+-----------------+     +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+     +-----------------+
| ELEMENT last    |     | ELEMENT last    |
+-----------------+     +-----------------+
```
