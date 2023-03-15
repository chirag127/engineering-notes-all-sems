### Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language for styling HTML and XML documents.
- XSL (eXtensible Stylesheet Language) is a language for transforming XML documents into other formats, such as HTML, PDF, or plain text.
- To create a style sheet in CSS, you need to use the `<style>` element inside the `<head>` element of your HTML or XML document, or use the `<link>` element to reference an external CSS file.
- To create a style sheet in XSL, you need to use the `<xsl:stylesheet>` or `<xsl:transform>` element as the root element of your XSL file, and use the `<xsl:template>` element to define the rules for transforming the XML document.
- To display the document in internet explorer, you need to save the XML and XSL files with the .xml and .xsl extensions, respectively, and use the `<?xml-stylesheet?>` processing instruction in the XML file to link to the XSL file.
- Alternatively, you can use a server-side script, such as PHP or ASP, to transform the XML document using the XSL file and send the output to the browser as HTML.

Example:

XML file (notes.xml):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="notes.xsl"?>
<notes>
  <note>
    <title>Introduction to Javascript</title>
    <content>Javascript is a scripting language that runs in the browser and can manipulate the HTML document.</content>
  </note>
  <note>
    <title>Introduction to XML</title>
    <content>XML is a markup language that defines a set of rules for encoding data in a human-readable and machine-readable format.</content>
  </note>
</notes>
```

XSL file (notes.xsl):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" doctype-system="about:legacy-compat"/>
  <xsl:template match="/">
    <html>
      <head>
        <style>
          h1 {
            color: blue;
          }
          p {
            font-family: Arial;
          }
        </style>
      </head>
      <body>
        <h1>Notes for Unit 3 - Design dynamic web pages using Javascript and XML</h1>
        <xsl:apply-templates select="notes/note"/>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="note">
    <h2><xsl:value-of select="title"/></h2>
    <p><xsl:value-of select="content"/></p>
  </xsl:template>
</xsl:stylesheet>
```

Output (in internet explorer):

![Output](https://i.imgur.com/0tJZz0y.png)