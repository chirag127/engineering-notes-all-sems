Document type definition (DTD) is an instruction that tells the web browser about the markup language in which the current page is written . It also defines the structure and the legal elements and attributes of an XML document . A DTD can be declared inside an XML document as internal or as an external reference .

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

The DOCTYPE declaration is the first line of an HTML document and it specifies the version of HTML or the standard of HTML that is being used in the document . The DOCTYPE declaration also determines the rendering mode of the web browser, which affects how the web page is displayed .

An example of a DOCTYPE declaration for HTML5 is:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Example</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```