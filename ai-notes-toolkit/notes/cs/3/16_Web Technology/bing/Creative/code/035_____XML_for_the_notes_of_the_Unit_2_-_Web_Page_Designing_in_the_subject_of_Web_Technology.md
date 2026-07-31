### XML

XML stands for eXtensible Markup Language. It is a language that allows you to create your own tags to describe and structure data in a text format. XML is similar to HTML, but unlike HTML, XML does not have predefined tags to use. Instead, you can design your own tags to suit your needs. This makes XML a powerful and flexible way to store, transport, and share data across different platforms and applications.

Some of the basic features and rules of XML are:

- XML documents must be well-formed, meaning that they must follow the syntax rules of XML, such as having a root element, matching start and end tags, using quotes around attribute values, etc.
- XML documents can also be valid, meaning that they must conform to the semantic rules defined by an XML schema or a DTD (Document Type Definition). A schema or a DTD specifies the structure and content of an XML document, such as what elements and attributes are allowed, what data types are used, what values are valid, etc.
- XML documents start with an XML declaration, which specifies the version, encoding, and standalone status of the document. For example: `<?xml version="1.0" encoding="UTF-8"?>`
- XML elements are the building blocks of an XML document. They consist of a start tag, an end tag, and the content between them. For example: `<note>Hello</note>`
- XML elements can have attributes, which provide additional information about the element. Attributes are written inside the start tag, and have a name and a value. For example: `<note date="2023-03-15">Hello</note>`
- XML elements can be nested, meaning that they can contain other elements as their content. For example: `<note><to>John</to><from>Mary</from><message>Hello</message></note>`
- XML elements can be empty, meaning that they have no content and only a start tag. In this case, the start tag can be closed with a slash. For example: `<note/>`
- XML elements and attributes are case-sensitive, meaning that `<note>` and `<Note>` are different elements, and `date` and `Date` are different attributes.
- XML elements and attributes must follow the naming rules of XML, such as starting with a letter or underscore, not containing spaces or colons, not being a reserved word, etc.
- XML comments are used to add notes or explanations to the XML document. They are written between `<!--` and `-->`. For example: `<!-- This is a comment -->`
- XML supports special characters, such as `<`, `>`, `&`, `"`, and `'`, by using predefined entities or character references. For example: `&lt;` for `<`, `&gt;` for `>`, `&amp;` for `&`, `&quot;` for `"`, and `&apos;` for `'`.
- XML supports namespaces, which are used to avoid name conflicts when using elements or attributes from different sources. A namespace is identified by a URI (Uniform Resource Identifier), and is declared using the `xmlns` attribute. For example: `<note xmlns="http://example.com/note">Hello</note>`