### Document type definition in Web Page Designing

A Document Type Definition (DTD) is a set of markup declarations that define a document type for an SGML-family markup language (SGML, XML, HTML). A DTD defines the valid building blocks of an XML document. It sets the rules for the markup language, so that the structure of an XML document can be verified for correctness.

Here is an example of a DTD declaration in an XML document:

```xml
<!DOCTYPE note [
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
]>
```

This DTD specifies that the `note` element must contain the elements `to`, `from`, `heading`, and `body` in that order. The `#PCDATA` keyword indicates that the elements can contain parsed character data.

In HTML, the `<!DOCTYPE>` declaration is used to specify the version of HTML that the page is written in. For example, the following declaration specifies that the page is written in HTML5:

```html
<!DOCTYPE html>
```

This declaration must be the first line in the HTML document, before the `<html>` tag. It is not an HTML tag, but an instruction to the web browser about what version of HTML the page is written in. This helps the browser to render the page correctly.