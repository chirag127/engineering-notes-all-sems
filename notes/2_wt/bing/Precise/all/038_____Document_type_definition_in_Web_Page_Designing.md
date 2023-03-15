### Document type definition in Web Page Designing

- Document Type Definition (DTD) is a set of markup declarations that define a document type for SGML-family markup languages (SGML, XML, HTML).
- A DTD defines the valid building blocks of an XML document. It defines the document structure with a list of legal elements and attributes.
- A DTD can be declared inline in your XML document, or as an external reference.
- XML uses a subset of SGML DTD.
- The purpose of a DTD is to define the structure and the legal elements and attributes of an XML document.
- A DTD can be used to verify that the data being exchanged between systems conforms to a common structure and set of rules.
- DTDs are not as widely used as they once were, having been largely replaced by XML Schema and other schema languages.
- However, DTDs are still used in some applications and can be useful for defining the structure of XML documents.
- A mnemonic to remember the purpose of DTD is: **D**efines **T**he **D**ocument structure.

Here is an example of a simple DTD:

```
<!DOCTYPE note [
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
]>
```

This DTD defines a `note` element that contains four elements: `to`, `from`, `heading`, and `body`. Each of these elements can contain only parsed character data (`#PCDATA`).

Advantages of using DTDs:
- DTDs provide a way to define the structure and content of an XML document.
- DTDs can be used to validate the data in an XML document, ensuring that it conforms to a predefined structure.
- DTDs can be used to define a common data format for exchanging information between systems.

Disadvantages of using DTDs:
- DTDs are not as expressive as other schema languages, such as XML Schema.
- DTDs do not support data types or namespaces.
- DTDs are not as widely used as they once were, and support for them may be limited in some applications.