### XML schemes in Web Page Designing

XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. XML is commonly used in web page designing to store and transport data.

Here is an example of how XML can be used in web page designing:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<page>
  <title>My Web Page</title>
  <header>
    <logo src="logo.png" alt="My Logo" />
    <menu>
      <item href="index.html">Home</item>
      <item href="about.html">About</item>
      <item href="contact.html">Contact</item>
    </menu>
  </header>
  <content>
    <h1>Welcome to my web page!</h1>
    <p>This is some sample content.</p>
  </content>
  <footer>
    <p>Copyright © 2023 My Web Page</p>
  </footer>
</page>
```

This XML document defines the structure and content of a web page. The `<page>` element is the root element of the document, and it contains child elements such as `<title>`, `<header>`, `<content>`, and `<footer>` that define the different sections of the web page. The `<menu>` element contains a list of `<item>` elements that represent the navigation menu of the web page.

Using XML in web page designing allows for a clear separation of content and presentation, making it easier to maintain and update the web page. Additionally, XML data can be easily accessed and manipulated using various programming languages and tools.