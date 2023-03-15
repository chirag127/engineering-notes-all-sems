### Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- XML stands for **eXtensible Markup Language**.
- XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
- XML is used for designing the web pages in an application. It is dynamic because it is used to transport the data not for displaying the data.
- XML is different from HTML, which is another markup language for creating web pages. HTML has predefined tags to use, while XML allows you to define your own tags designed specifically for your needs.
- XML is a powerful way to store data in a format that can be stored, searched, and shared.
- XML documents have a simple structure that consists of the following elements:
  - A prolog that declares the XML version, the encoding, and the document type definition (DTD) or schema.
  - A root element that contains all other elements in the document.
  - Elements that have a start tag, an end tag, and some content. Elements can have attributes, which are name-value pairs inside the start tag. Elements can also have child elements, which are nested inside the parent element.
  - Comments that start with `<!--` and end with `-->`. Comments can appear anywhere in the document and are ignored by the XML parser.
  - Processing instructions that start with `<?` and end with `?>`. Processing instructions can contain any information for the application that processes the XML document, such as style sheets or scripts.
  - Character data (CDATA) sections that start with `<![CDATA[` and end with `]]>`. CDATA sections can contain any text that is not parsed by the XML parser, such as special characters or markup.
- XML documents can be validated against a DTD or a schema, which define the rules and constraints for the structure and content of the document. A DTD is a set of declarations that specify the elements, attributes, entities, and notations that are allowed in the document. A schema is a set of definitions that describe the elements, attributes, types, and relationships that are allowed in the document. A schema can be written in XML Schema, Relax NG, or other languages.
- XML documents can be transformed, formatted, and displayed using style sheets or other tools. A style sheet is a set of rules that define how to present the XML document. A style sheet can be written in XSLT, CSS, or other languages. A tool is a program or a library that can process the XML document and perform various tasks, such as parsing, validating, querying, transforming, or rendering. A tool can be written in Java, Python, or other languages.