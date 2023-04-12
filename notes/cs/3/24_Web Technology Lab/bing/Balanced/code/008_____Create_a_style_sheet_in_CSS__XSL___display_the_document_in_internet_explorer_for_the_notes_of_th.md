# Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a set of rules that defines how to format and present an XML document.
- CSS (Cascading Style Sheets) is a language for defining style rules for HTML and XML documents.
- XSL (Extensible Stylesheet Language) is a language for transforming and formatting XML documents.
- XSL consists of three parts: XSLT, XPath, and XSL-FO.
- XSLT (XSL Transformations) is a language for transforming XML documents into other formats, such as HTML, XML, or plain text.
- XPath (XML Path Language) is a language for selecting nodes and values from an XML document.
- XSL-FO (XSL Formatting Objects) is a language for defining the layout and presentation of XML documents.
- To create a style sheet in CSS/XSL, you need to follow these steps:

  1. Create an XML document that contains the data and structure of your web page.
  2. Create a CSS file that defines the style rules for your web page, such as fonts, colors, margins, etc.
  3. Create an XSL file that defines the transformation rules for your web page, such as how to select and display the data from the XML document, how to apply the CSS style rules, etc.
  4. Link the XML document to the XSL file using the `<?xml-stylesheet?>` processing instruction, which specifies the type, href, and media attributes of the XSL file.
  5. Link the XSL file to the CSS file using the `<xsl:import>` or `<xsl:include>` element, which specifies the href attribute of the CSS file.
  6. Save the XML, XSL, and CSS files in the same folder or directory.
  7. Open the XML file in Internet Explorer, which will apply the XSL transformation and display the web page according to the CSS style rules.

- Here is an example of an XML document that contains some notes for Unit 3:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="notes.xsl"?>
<notes>
  <unit>
    <title>Design dynamic web pages using Javascript and XML</title>
    <topics>
      <topic>
        <name>Javascript</name>
        <description>Javascript is a scripting language that can be embedded in HTML documents to add interactivity and functionality to web pages.</description>
      </topic>
      <topic>
        <name>XML</name>
        <description>XML is a markup language that can be used to store and exchange structured data.</description>
      </topic>
      <topic>
        <name>AJAX</name>
        <description>AJAX is a technique that uses Javascript and XML to communicate with a server and update a web page without reloading it.</description>
      </topic>
    </topics>
  </unit>
</notes>
```

- Here is an example of a CSS file that defines some style rules for the web page:

```css
body {
  font-family: Arial, sans-serif;
  background-color: lightblue;
}

h1 {
  color: white;
  background-color: navy;
  text-align: center;
}

h2 {
  color: navy;
  margin-left: 20px;
}

p {
  margin-left: 40px;
}
```

- Here is an example of an XSL file that defines the transformation rules for the web page:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Import the CSS file -->
  <xsl:import href="notes.css"/>
  <!-- Output method is HTML -->
  <xsl:output method="html"/>
  <!-- Template for the root element -->
  <xsl:template match="/">
    <!-- Create the HTML document -->
    <html>
      <head>
        <title>Notes for Unit 3</title>
      </head>
      <body>
        <!-- Apply the template for the unit element -->
        <xsl:apply-templates select="notes/unit"/>
      </body>
    </html>
  </xsl:template>
  <!-- Template for the unit element -->

```
