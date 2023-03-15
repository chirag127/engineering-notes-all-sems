### Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of a web document, such as fonts, colors, margins, etc.
- CSS (Cascading Style Sheets) is a language for creating style sheets for HTML documents.
- XSL (Extensible Stylesheet Language) is a language for creating style sheets for XML documents.
- XSL can also transform XML documents into other formats, such as HTML, using XSLT (XSL Transformations).
- To create a style sheet in CSS/XSL, follow these steps:

  1. Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  2. In the file, write the rules that define the style of the elements in the web document. For example, to change the color of the headings to blue, you can write:

  ```css
  h1, h2, h3 {
    color: blue;
  }
  ```

  3. If you are creating an XSL style sheet, you also need to declare the root element that specifies the document to be an XSL style sheet. This can be either `<xsl:stylesheet>` or `<xsl:transform>`. For example:

  ```xml
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- your style rules here -->
  </xsl:stylesheet>
  ```

  4. If you are creating an XSL style sheet that transforms XML into another format, you also need to write the templates that match the elements in the XML document and output the desired result. For example, to transform an XML document that contains book titles and authors into an HTML table, you can write:

  ```xml
  <xsl:template match="/">
    <html>
      <head>
        <title>Books</title>
      </head>
      <body>
        <table border="1">
          <tr>
            <th>Title</th>
            <th>Author</th>
          </tr>
          <xsl:apply-templates select="books/book"/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="book">
    <tr>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="author"/></td>
    </tr>
  </xsl:template>
  ```

- To display the document in internet explorer, follow these steps:

  1. Save the web document (HTML or XML) and the style sheet (CSS or XSL) in the same folder on your computer.
  2. In the web document, link to the style sheet using the `<link>` element in the `<head>` section. For example, to link to a CSS style sheet named style.css, you can write:

  ```html
  <head>
    <link rel="stylesheet" type="text/css" href="style.css"/>
  </head>
  ```

  3. To link to an XSL style sheet named style.xsl, you can write:

  ```xml
  <?xml-stylesheet type="text/xsl" href="style.xsl"?>
  ```

  4. Open the web document in internet explorer and view the result. You may need to enable the option to allow active content to run in files on your computer.