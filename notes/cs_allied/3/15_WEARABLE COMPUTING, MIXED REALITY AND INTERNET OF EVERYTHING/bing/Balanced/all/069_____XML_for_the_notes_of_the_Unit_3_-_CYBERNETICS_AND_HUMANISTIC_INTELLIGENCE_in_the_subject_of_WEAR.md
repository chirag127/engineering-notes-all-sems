# XML

XML stands for eXtensible Markup Language. It is a language that allows you to define your own tags and structure your data in a way that is easy to store, search, and share. XML is similar to HTML, but it has some differences:

- XML tags are not predefined. You can create your own tags according to your needs.
- XML is case-sensitive. You must use the same case for opening and closing tags.
- XML must be well-formed. This means that every opening tag must have a matching closing tag, and that tags must be properly nested and closed.
- XML can be validated against a schema or a DTD. This means that you can specify the rules and constraints for your XML document, such as what elements and attributes are allowed, and what values are valid.

## XML Syntax

An XML document consists of the following parts:

- An XML declaration. This is an optional line that specifies the version, encoding, and standalone status of the XML document. It must be the first line of the document, and it must start with `<?xml` and end with `?>`. For example: `<?xml version="1.0" encoding="UTF-8"?>`
- A root element. This is the main element that contains all other elements in the document. There can be only one root element, and it must enclose all other elements. For example: `<note> ... </note>`
- Child elements. These are the elements that are nested inside the root element or other elements. They can have attributes, text, or other child elements. For example: `<to> Tove </to>`
- Attributes. These are name-value pairs that provide additional information about an element. They must be enclosed in quotation marks, and they must appear inside the start tag of the element. For example: `<book title="The Lord of the Rings" author="J.R.R. Tolkien"/>`
- Text. This is the content of the element, which can be plain text or character data. Character data is text that contains special characters, such as `<`, `>`, or `&`, that must be escaped using predefined entities, such as `&lt;`, `&gt;`, or `&amp;`. For example: `<message> Hello &amp; welcome! </message>`
- Comments. These are notes or annotations that are ignored by the XML parser. They must start with `<!--` and end with `-->`. For example: `<!-- This is a comment -->`

## XML Example

Here is an example of a well-formed and valid XML document that represents a note:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to> Tove </to>
  <from> Jani </from>
  <heading> Reminder </heading>
  <body> Don't forget me this weekend! </body>
</note>
```