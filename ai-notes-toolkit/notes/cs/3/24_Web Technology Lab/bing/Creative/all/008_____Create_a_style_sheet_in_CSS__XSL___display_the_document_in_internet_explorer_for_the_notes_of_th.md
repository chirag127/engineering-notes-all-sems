# Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language for styling HTML and XML documents.
- XSL (eXtensible Stylesheet Language) is a language for transforming XML documents into other formats, such as HTML, PDF, or plain text.
- To create a style sheet in CSS/XSL, you need to follow these steps:

  1. Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  2. In the style sheet file, use the appropriate syntax and rules to define the style properties and values for the elements and attributes of the XML document.
  3. Save the style sheet file in the same folder as the XML document, or in a different location that can be accessed by the XML document.
  4. In the XML document, add a reference to the style sheet file using the <link> element (for CSS) or the <?xml-stylesheet?> processing instruction (for XSL) in the <head> section of the document.
  5. Example of a CSS style sheet file (style.css):

```css
/* This is a comment */
h1 {
  color: blue;
  font-size: 24px;
}

p {
  font-family: Arial, sans-serif;
  margin: 10px;
}
```

  6. Example of an XSL style sheet file (style.xsl):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- This is a comment -->
  <xsl:output method="html"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Example of XSL Transformation</title>
      </head>
      <body>
        <h1><xsl:value-of select="book/title"/></h1>
        <p>Author: <xsl:value-of select="book/author"/></p>
        <p>Price: <xsl:value-of select="book/price"/></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

  7. Example of an XML document (book.xml) that references the style sheet files:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/css" href="style.css"?>
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
<book>
  <title>XML for Beginners</title>
  <author>John Smith</author>
  <price>19.99</price>
</book>
```

- To display the document in internet explorer, you need to follow these steps:

  1. Open the internet explorer browser and navigate to the folder where the XML document is located.
  2. Double-click on the XML document file to open it in the browser.
  3. The browser will apply the style sheet files to the XML document and display the transformed output in HTML format.
  4. You can also right-click on the XML document file and select "Open with" and choose internet explorer from the list of programs.