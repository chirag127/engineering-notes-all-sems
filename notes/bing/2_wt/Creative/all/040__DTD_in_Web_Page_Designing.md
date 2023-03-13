### DTD in Web Page Designing

- DTD stands for Document Type Definition. It is an instruction to the web browser about what version of HTML the page is written in. It ensures that the web page is parsed the same way by different web browsers.
- A DTD defines the structure and the legal elements and attributes of an XML document. XML documents can use a DTD to verify that they are valid.
- There are two types of DTDs: internal and external. An internal DTD is declared inside the XML document, while an external DTD is declared in a separate file and referenced by the XML document.
- An example of an internal DTD declaration is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
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

- An example of an external DTD declaration is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "Note.dtd">
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

- The external DTD file "Note.dtd" contains the same DTD declaration as the internal one.
- In HTML 4.01, there are three types of DTDs: strict, transitional, and frameset. They differ in the level of support for deprecated elements and attributes that are expected to be phased out as CSS support grows.
- An example of a strict DTD declaration is:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <title>Example</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```

- An example of a transitional DTD declaration is:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <title>Example</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <font color="red">This is deprecated</font>
</body>
</html>
```

- An example of a frameset DTD declaration is:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
<html>
<head>
  <title>Example</title>
</head>
<frameset cols="25%,75%">
  <frame src="menu.html">
  <frame src="content.html">
</frameset>
</html>
```

- In HTML5, there is only one type of DTD declaration, which is:

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

- This DTD declaration tells the browser to render the page in standards mode, which means it follows the HTML5 specification.
- The advantages of using a DTD are:
  - It helps to ensure the validity and consistency of the XML or HTML document.
  - It helps to avoid errors and bugs in the web page rendering.
  - It helps to improve the interoperability and compatibility of the web page across different browsers and platforms.
  - It helps to facilitate the data exchange and integration between different applications and systems.
- The disadvantages of using a DTD are:
  - It adds extra complexity and overhead to the XML or HTML document.
  - It may not cover all the possible variations and extensions of the XML or HTML document.
  - It may not be updated or maintained to reflect the latest standards and best practices of the XML or HTML document.
- A mnemonic to remember the difference between the three types of HTML 4.