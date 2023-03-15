 Here is the formal content on the topic "Document type definition in Web Page Designing" written in Markdown format without any emojis or external links:

### Document type definition in Web Page Designing

1. A document type definition (DTD) is a set of markup declarations that define a document type for an SGML-family markup language (GML, SGML, XML, HTML). A DTD defines the valid building blocks of an XML document. It defines the document structure with a list of valid elements and attributes.

2. A DTD can be declared inline inside an XML document, or as an external reference. The external DTD is preferred as it can be used by multiple XML documents. The DTD is defined inside a DOCTYPE declaration which is included in the XML declaration at the start of the document.

3. The benefits of a DTD are:

- It defines the structure of an XML document and validates that each document follows the structure.
- It acts as a contract between the document and its processing application.
- It enables the processing application to check for errors and ensure conformance.
- It serves as documentation for the structure and syntax of the elements and attributes of an XML document.

4. A DTD can use element declarations to declare elements, attribute declarations to declare attributes, entity declarations to declare entities, and notation declarations to declare notations. It uses a specific syntax with declarations of elements, attributes, entities, and notations within brackets. A basic example of an external DTD is:

<!DOCTYPE note SYSTEM "note.dtd">

<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>