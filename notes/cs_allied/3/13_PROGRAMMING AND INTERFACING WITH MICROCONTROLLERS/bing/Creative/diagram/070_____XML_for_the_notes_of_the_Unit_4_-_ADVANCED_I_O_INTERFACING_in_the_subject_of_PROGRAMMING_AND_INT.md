# XML

XML stands for eXtensible Markup Language. It is a language that allows you to define your own tags and structure your data in a way that is easy to store, search, and share. XML is similar to HTML, but it has some differences:

- XML tags are not predefined. You can create your own tags according to your needs.
- XML is case-sensitive. You must use the same case for opening and closing tags.
- XML must be well-formed. This means that every opening tag must have a matching closing tag, and the tags must be nested properly.
- XML can be validated against a schema or a DTD. This means that you can specify the rules and constraints for your XML document, such as the allowed elements, attributes, and data types.

## XML Syntax

An XML document consists of the following parts:

- An XML declaration. This is an optional line that specifies the XML version, the encoding, and the standalone attribute. It must be the first line of the document, and it must start with `<?xml` and end with `?>`. For example: `<?xml version="1.0" encoding="UTF-8"?>`
- A root element. This is the main element that contains all other elements. It must be the only element at the top level of the document, and it must have a name. For example: `<note>`
- Child elements. These are the elements that are nested inside the root element or other elements. They can have names, attributes, and text content. For example: `<to>Tove</to>`
- End tags. These are the tags that close the elements. They must have the same name as the opening tags, and they must start with `</` and end with `>`. For example: `</note>`
- Comments. These are the lines that are ignored by the XML parser. They can be used to add notes or explanations to the XML document. They must start with `<!--` and end with `-->`. For example: `<!-- This is a comment -->`

## XML Example

Here is an example of a well-formed and valid XML document that represents a note:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

This XML document has the following structure:

- The XML declaration specifies the XML version, the encoding, and the standalone attribute.
- The root element is `<note>`, which contains four child elements: `<to>`, `<from>`, `<heading>`, and `<body>`.
- Each child element has a name and a text content. For example, the `<to>` element has the name "to" and the text content "Tove".
- Each element has a matching end tag. For example, the `<note>` element has the end tag `</note>`.
- There are no comments in this XML document, but they could be added anywhere outside the elements.