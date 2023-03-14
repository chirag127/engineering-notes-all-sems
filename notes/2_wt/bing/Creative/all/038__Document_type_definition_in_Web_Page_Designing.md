### Document type definition in Web Page Designing

- A document type definition (DTD) is an instruction that tells the web browser about the markup language in which the current page is written.
- A DTD defines the structure and the legal elements and attributes of an XML document.
- A DTD can be declared inside the XML file, wrapped inside the `<!DOCTYPE>` definition, or in an external file, referenced by the `<!DOCTYPE>` definition.
- A DTD is useful for validating the XML data and ensuring that independent groups of people can agree on a standard DTD for interchanging data.
- A DTD can be written in two forms: internal or external.
- An internal DTD is declared inside the XML file, using the syntax:

```xml
<?xml version="1.0"?>
<!DOCTYPE root-element [
    <!-- DTD declarations -->
]>
<!-- XML document -->
```

- An external DTD is declared in a separate file, using the syntax:

```xml
<?xml version="1.0"?>
<!DOCTYPE root-element SYSTEM "dtd-file">
<!-- XML document -->
```

- An example of an internal DTD for a note element is:

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
    <to> Tove </to>
    <from> Jani </from>
    <heading> Reminder </heading>
    <body> Don't forget me this weekend </body>
</note>
```

- An example of an external DTD for a note element is:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to> Tove </to>
    <from> Jani </from>
    <heading> Reminder </heading>
    <body> Don't forget me this weekend! </body>
</note>
```

- And the file "note.dtd" contains the DTD:

```xml
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
```

- A DTD can also be used for HTML documents, to indicate the version or standard of HTML being used in the document.
- A DTD for HTML documents is declared using the syntax:

```html
<!DOCTYPE html>
<!-- HTML document -->
```

- A DTD for HTML documents can also specify a URL for a DTD file that defines the HTML standard, such as:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<!-- HTML document -->
```

- A mnemonic to remember the syntax of a DTD declaration is: DOCTYPE, root-element, SYSTEM or PUBLIC, and optional URL.
- A learning trick to understand the purpose of a DTD is to think of it as a blueprint or a contract that defines the rules and expectations for the XML or HTML document.