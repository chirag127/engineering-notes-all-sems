### DTD in Web Page Designing

A DTD (Document Type Definition) is a set of rules that defines the structure and the legal elements and attributes of an XML document . A DTD can be declared inside an XML document as inline or as an external reference. A DTD is important for web page designing because it specifies the version of the HTML or XHTML standard that the web page follows . A DTD can affect the display of the web page by influencing how the browser parses and renders the HTML or XHTML code.

An example of an inline DTD declaration for an HTML 4.01 document is:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>Example</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>
```

An example of an external DTD reference for an XML document is:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```