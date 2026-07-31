### DTD in Web Page Designing

A Document Type Definition (DTD) is a set of markup declarations that define a document type for an SGML-family markup language (SGML, XML, HTML). A DTD defines the valid building blocks of an XML document. It sets the rules for the markup language, so that the structure of the document can be verified.

Here is an example of a simple DTD for an XML document that might be used for a list of people:

```xml
<!DOCTYPE people [
  <!ELEMENT people (person*)>
  <!ELEMENT person (name, email)>
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT email (#PCDATA)>
]>
```

This DTD specifies that the `people` element contains zero or more `person` elements, and that each `person` element must contain a `name` element followed by an `email` element. The `name` and `email` elements can contain parsed character data (PCDATA), which means that they can contain any text.

In web page designing, a DTD is used to define the structure and content of an HTML or XHTML document. By specifying a DTD, the web designer can ensure that the web page will be displayed correctly by web browsers that support the specified DTD. It is important to include a DTD in a web page to ensure that the page is displayed consistently across different web browsers.