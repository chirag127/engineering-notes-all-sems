### Document type definition for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- A document type definition (DTD) is a set of rules that defines the structure and the legal elements and attributes of an XML document .
- A DTD can be declared inside an XML document as an internal DTD, or as an external reference to a separate file .
- A DTD helps to ensure the validity and interoperability of XML documents by specifying the allowed syntax and semantics of the markup language .
- A DTD can also be used to declare entities, which are shortcuts for common text or symbols, such as `&amp;` for `&`.
- A DTD has the following syntax:

```
<!DOCTYPE root-element [
  <!-- Element declarations -->
  <!-- Attribute declarations -->
  <!-- Entity declarations -->
  <!-- Notation declarations -->
  <!-- Comments -->
  <!-- Processing instructions -->
]>
```

- The root-element is the name of the top-level element in the XML document.
- The element declarations define the names and contents of the elements in the XML document. For example:

```
<!ELEMENT note (to, from, heading, body)>
```

- The attribute declarations define the names and values of the attributes for the elements in the XML document. For example:

```
<!ATTLIST note date CDATA #IMPLIED>
```

- The entity declarations define the names and values of the entities for the XML document. For example:

```
<!ENTITY author "John Doe">
```

- The notation declarations define the names and formats of the external data referenced by the XML document. For example:

```
<!NOTATION gif SYSTEM "image/gif">
```

- The comments and processing instructions are optional and can be used to provide additional information or instructions for the XML document. For example:

```
<!-- This is a comment -->
<?xml-stylesheet href="style.css" type="text/css"?>
```

- A DTD is useful for web page designing because it allows the creation and validation of custom XML-based languages that can be used to structure and present web content .
- Some examples of XML-based languages for web page designing are XHTML, SVG, MathML, and RSS .