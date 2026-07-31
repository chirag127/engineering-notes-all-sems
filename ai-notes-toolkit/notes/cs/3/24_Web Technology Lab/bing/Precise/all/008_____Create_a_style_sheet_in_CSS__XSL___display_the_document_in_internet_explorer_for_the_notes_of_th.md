# Create a style sheet in CSS/XSL & display the document in Internet Explorer

## Introduction
- Cascading Style Sheets (CSS) and Extensible Stylesheet Language (XSL) are both used to style and format documents for display on the web.
- CSS is used to style HTML documents, while XSL is used to transform XML documents into other formats, such as HTML or PDF.
- Internet Explorer is a web browser that can be used to display documents styled with CSS or transformed with XSL.

## Creating a CSS Style Sheet
1. Open a text editor and create a new file with the extension `.css`.
2. In the file, define the styles for the HTML elements you want to style. For example:
```css
body {
  font-family: Arial, sans-serif;
  font-size: 14px;
}

h1 {
  color: blue;
  font-size: 24px;
}
```
3. Save the file.

## Linking the CSS Style Sheet to an HTML Document
1. In the HTML document, add a `link` element in the `head` section to link to the CSS file. For example:
```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```
2. Save the HTML file.

## Creating an XSL Style Sheet
1. Open a text editor and create a new file with the extension `.xsl`.
2. In the file, define the XSLT template to transform the XML document. For example:
```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Example</title>
      </head>
      <body>
        <h1><xsl:value-of select="example/title"/></h1>
        <p><xsl:value-of select="example/content"/></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```
3. Save the file.

## Transforming an XML Document with XSL
1. In the XML document, add a `processing-instruction` to link to the XSL file. For example:
```xml
<?xml-stylesheet type="text/xsl" href="transform.xsl"?>
<example>
  <title>Example Title</title>
  <content>Example content.</content>
</example>
```
2. Save the XML file.

## Displaying the Document in Internet Explorer
1. Open Internet Explorer and navigate to the location of the HTML or XML file.
2. The document should be displayed with the styles defined in the CSS or XSL file.