### Document type definition in Web Page Designing

- A document type definition (DTD) is a set of rules that defines the structure and syntax of a markup language, such as HTML or XML.
- A DTD specifies what elements, attributes, entities, and notations are allowed in a document, and how they are organized and nested.
- A DTD can be declared either internally or externally to a document. An internal DTD is embedded within the document itself, while an external DTD is referenced by a URL or a file path.
- A DTD can be used to validate a document against the rules of the markup language, and to ensure that the document is well-formed and consistent.
- A DTD can also be used to provide default values for attributes, declare entities for special characters or common phrases, and define notations for non-XML data, such as images or multimedia.
- A DTD can be written in two syntaxes: SGML or XML. SGML is the older and more complex syntax, while XML is the newer and simpler syntax. XML DTDs are more widely used and supported than SGML DTDs.
- A DTD starts with a document type declaration, which identifies the name of the document type and the location of the DTD. For example, the following declaration indicates that the document is an HTML document and the DTD is located at the URL http://www.w3.org/TR/html4/strict.dtd:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

- A DTD consists of a series of declarations that define the elements, attributes, entities, and notations of the document type. For example, the following declarations define an element called title, an attribute called lang, an entity called copy, and a notation called gif:

```dtd
<!ELEMENT title (#PCDATA)>
<!ATTLIST title lang CDATA #IMPLIED>
<!ENTITY copy "&copy;">
<!NOTATION gif SYSTEM "image/gif">
```

- A DTD can also include comments, conditional sections, and parameter entities. Comments are used to add notes or explanations to the DTD, and start and end with `<!--` and `-->`. Conditional sections are used to include or exclude parts of the DTD based on certain conditions, and start and end with `<![` and `]>`. Parameter entities are used to define reusable chunks of DTD code, and start and end with `%` and `;`. For example, the following DTD uses a comment, a conditional section, and a parameter entity:

```dtd
<!-- This is a comment -->
<!ENTITY % heading "h1|h2|h3|h4|h5|h6">
<![INCLUDE [
<!ELEMENT %heading; (#PCDATA)>
<!ATTLIST %heading; align (left|center|right) #IMPLIED>
]]>
```