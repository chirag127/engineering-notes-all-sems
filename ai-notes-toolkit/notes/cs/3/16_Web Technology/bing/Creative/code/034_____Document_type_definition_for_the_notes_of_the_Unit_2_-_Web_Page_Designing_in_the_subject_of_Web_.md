# Document type definition for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- A document type definition (DTD) is a set of rules that defines the structure and content of an XML or HTML document.
- A DTD specifies the elements, attributes, entities, and notations that are allowed in a document, and how they can be combined.
- A DTD can be declared either internally or externally to the document. An internal DTD is written inside the document, while an external DTD is written in a separate file and referenced by the document.
- A DTD helps to ensure the validity and interoperability of web documents, as it allows browsers and other applications to check if the document conforms to the expected format.
- A DTD can be written in two syntaxes: SGML or XML. SGML is the older and more complex syntax, while XML is the newer and simpler syntax. XML DTDs are more widely used for web documents.
- A DTD starts with a document type declaration, which identifies the root element and the DTD source of the document. For example, the following declaration indicates that the document has a root element named html and uses an external DTD file named html5.dtd:

```xml
<!DOCTYPE html SYSTEM "html5.dtd">
```

- A DTD consists of element declarations, attribute declarations, entity declarations, and notation declarations. Each declaration defines a specific aspect of the document structure or content.
- An element declaration defines the name, content model, and occurrence of an element in the document. For example, the following declaration indicates that the element named p can contain any character data (#PCDATA) and can appear zero or more times (*) in the document:

```xml
<!ELEMENT p (#PCDATA)*>
```

- An attribute declaration defines the name, type, default value, and usage of an attribute for an element. For example, the following declaration indicates that the element named img has an attribute named src, which is of type CDATA (character data), has no default value (#IMPLIED), and is required (REQUIRED) for the element:

```xml
<!ATTLIST img src CDATA #IMPLIED REQUIRED>
```

- An entity declaration defines a name and a value for a piece of text or data that can be reused in the document. For example, the following declaration indicates that the entity named copy has a value of © (the copyright symbol):

```xml
<!ENTITY copy "©">
```

- A notation declaration defines a name and a source for a non-XML data format that can be embedded in the document. For example, the following declaration indicates that the notation named gif has a source of image/gif (the MIME type for GIF images):

```xml
<!NOTATION gif SYSTEM "image/gif">
```

- A DTD can also include comments, processing instructions, and conditional sections. Comments are used to add explanatory notes or remarks to the DTD. Processing instructions are used to provide instructions to the application that processes the document. Conditional sections are used to include or exclude parts of the DTD based on some conditions.
- For example, the following DTD snippet shows a comment, a processing instruction, and a conditional section:

```xml
<!-- This is a comment -->
<?xml-stylesheet type="text/css" href="style.css"?>
<![INCLUDE [<!ENTITY author "John Doe">]]>
```

- A DTD is an important component of web page designing, as it helps to define the syntax and semantics of the web document. A DTD can also facilitate the validation, transformation, and presentation of the web document.