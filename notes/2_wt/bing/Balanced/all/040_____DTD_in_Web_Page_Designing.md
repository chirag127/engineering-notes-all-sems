### DTD in Web Page Designing

- DTD stands for Document Type Definition .
- It is a set of markup declarations that define a type of document for the SGML family, such as HTML, XML, etc .
- It describes the tree structure of a document and the legal elements and attributes that can be used in it .
- It can be declared inside an XML document as internal or as an external reference .
- It is used to validate the XML document and ensure that it conforms to the rules specified by the DTD .
- It helps independent groups of people to agree on a standard DTD for interchanging data.
- It affects the display of the web page by informing the browser about the version of the HTML or XML used and how to interpret it .

#### Example of an internal DTD declaration

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

#### Example of an external DTD reference

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

#### Mnemonics and learning tricks

- DTD can be remembered as **D**efine **T**he **D**ocument.
- Internal DTD can be remembered as **I**nside **D**ocument **T**ype **D**efinition.
- External DTD can be remembered as **E**xternal **D**ocument **T**ype **D**efinition.
- The syntax of a DTD declaration can be remembered as `<!DOCTYPE root-element [ declarations ]>` for internal DTD and `<!DOCTYPE root-element SYSTEM "URI">` for external DTD.