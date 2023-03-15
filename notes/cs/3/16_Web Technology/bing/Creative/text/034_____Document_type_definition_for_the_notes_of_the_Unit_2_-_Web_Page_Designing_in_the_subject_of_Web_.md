### Document type definition for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- A document type definition (DTD) is a set of rules that defines the structure and the legal elements and attributes of an XML document .
- A DTD can be declared inside an XML document as an internal DTD, or as an external reference in a separate file .
- A DTD helps to ensure the validity and interoperability of XML documents by specifying the allowed syntax and semantics of the markup language .
- A DTD can also be used to declare entities, notations, and processing instructions that can be referenced in the XML document .
- A DTD is not mandatory for an XML document, but it is recommended to use one to avoid errors and inconsistencies .
- A DTD can be written in two syntaxes: SGML or XML. The XML syntax is more concise and compatible with XML parsers, while the SGML syntax is more expressive and flexible .
- A DTD consists of a prologue, an optional internal subset, and an optional external subset. The prologue contains the XML declaration and the document type declaration. The internal subset contains the DTD declarations that are embedded in the XML document. The external subset contains the DTD declarations that are stored in a separate file .
- A DTD declaration can be one of the following types: element declaration, attribute declaration, entity declaration, notation declaration, or processing instruction declaration .
- An element declaration defines the name and the content model of an XML element. The content model specifies the allowed child elements and their order and occurrence .
- An attribute declaration defines the name, the type, and the default value of an XML attribute. The type can be one of the predefined types, such as CDATA, ID, IDREF, or NMTOKEN, or a list of enumerated values .
- An entity declaration defines a named entity that can be used to replace a string of characters in the XML document. An entity can be either a general entity or a parameter entity. A general entity can be referenced by using the syntax &entity;, while a parameter entity can be referenced by using the syntax %entity; .
- A notation declaration defines a name and an identifier for a non-XML data format, such as an image or a sound file. A notation can be used to associate an external entity with a specific data format .
- A processing instruction declaration defines a name and a content for a processing instruction, which is a special instruction for the XML processor or the application that uses the XML document. A processing instruction can be used to convey information that is not part of the XML data, such as style sheets or scripts .