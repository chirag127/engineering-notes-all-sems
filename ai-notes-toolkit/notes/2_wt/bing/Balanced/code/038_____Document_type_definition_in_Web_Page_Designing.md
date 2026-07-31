### Document type definition in Web Page Designing

A document type definition (DTD) is an instruction that tells the web browser about the markup language in which the current page is written. It also defines the structure and the legal elements and attributes of an XML document. A DTD can be declared inside an XML document as internal or as an external reference.

An example of an internal DTD declaration is:

```xml
<?xml version="1.0"?>
<!DOCTYPE note [
  <!ELEMENT note (to,from,heading,body)>
  <!ELEMENT to (#PCDATA)>
  <!ELEMENT from (#PCDATA)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

An example of an external DTD reference is:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "Note.dtd">
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

In HTML, the doctype declaration refers to a document type definition (DTD) that specifies the rules for the markup language. The doctype declaration is required in HTML documents to ensure that the web page is parsed the same way by different web browsers. The doctype declaration is the first line of an HTML document and it has the following syntax:

```html
<!DOCTYPE html>
```

The doctype declaration can also specify the HTML version or standard, such as HTML 4.01 or XHTML 1.0. For example:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
```

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

The doctype declaration is not an element or tag, it is an instruction to the web browser. It does not have a closing tag and it must be placed before the <html> tag. The doctype declaration is case insensitive, but it is recommended to use uppercase letters for consistency.