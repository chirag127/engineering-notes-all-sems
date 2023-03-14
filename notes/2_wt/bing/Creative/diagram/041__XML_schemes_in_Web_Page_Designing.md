XML schemes in Web Page Designing are used to describe the structure and data types of XML documents. They are also known as XML Schema Definition (XSD) and are an alternative to Document Type Definition (DTD). XML schemes use XML syntax and can define elements, attributes, sequences, complex types, simple types, restrictions, patterns, and namespaces. They can also validate the correctness of data and support data conversion.

### XML schemes in Web Page Designing

The following diagram illustrates the basic architecture of a XML scheme in Web Page Designing:

```
+-----------------+         +-----------------+
| XML document    |         | XML scheme      |
|                 |         |                 |
| +-------------+ |         | +-------------+ |
| | Root element| |         | | Root element| |
| +-------------+ |         | +-------------+ |
|       |         |         |       |         |
|       |         |         |       |         |
| +-------------+ |         | +-------------+ |
| | Child element| |         | | Complex type| |
| +-------------+ |         | +-------------+ |
|       |         |         |       |         |
|       |         |         |       |         |
| +-------------+ |         | +-------------+ |
| | Attribute   | |         | | Simple type | |
| +-------------+ |         | +-------------+ |
|                 |         |                 |
+-----------------+         +-----------------+
```

The XML document contains the data that is structured according to the XML scheme. The XML scheme defines the elements and attributes that can appear in the document, their order, data types, default and fixed values, and namespaces. The XML scheme can also reference other schemes or import them. The XML document can be validated against the XML scheme to check if it conforms to the rules and constraints specified by the scheme. The XML scheme can also be transformed using XSLT or manipulated using the XML DOM.