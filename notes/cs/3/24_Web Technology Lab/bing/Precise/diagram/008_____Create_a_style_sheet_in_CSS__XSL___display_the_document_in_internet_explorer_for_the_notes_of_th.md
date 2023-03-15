### Create a style sheet in CSS/XSL & display the document in internet explorer

#### CSS (Cascading Style Sheets)

1. CSS is a stylesheet language used to describe the presentation of a document written in a markup language like HTML.
2. CSS is used to define the visual appearance of web pages, including colors, layout, and fonts.
3. To create a style sheet in CSS, you need to create a new text file with the `.css` extension.
4. In the CSS file, you can define styles for HTML elements using selectors and declarations.
5. A selector is used to target an HTML element, and a declaration is used to define the style for that element.
6. For example, to change the color of all `<p>` elements to red, you would write the following CSS code:

```css
p {
  color: red;
}
```

7. To link the CSS file to an HTML file, you need to add a `<link>` element in the `<head>` section of the HTML file, with the `href` attribute set to the path of the CSS file.

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

#### XSL (eXtensible Stylesheet Language)

1. XSL is a language used to transform XML documents into other formats, such as HTML or PDF.
2. XSL consists of three parts: XSLT (XSL Transformations), XPath, and XSL-FO (XSL Formatting Objects).
3. To create a style sheet in XSL, you need to create a new text file with the `.xsl` extension.
4. In the XSL file, you can define templates that match elements in the XML document and specify how they should be transformed.
5. For example, to transform an XML document containing `<book>` elements into an HTML table, you would write the following XSL code:

```xml
<xsl:template match="/">
  <html>
    <body>
      <table>
        <tr>
          <th>Title</th>
          <th>Author</th>
        </tr>
        <xsl:for-each select="books/book">
          <tr>
            <td><xsl:value-of select="title"/></td>
            <td><xsl:value-of select="author"/></td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>
```

6. To apply the XSL style sheet to an XML document, you need to add a `<?xml-stylesheet?>` processing instruction to the XML document, with the `href` attribute set to the path of the XSL file.

```xml
<?xml-stylesheet type="text/xsl" href="transform.xsl"?>
```

#### Displaying the document in Internet Explorer

1. To display an HTML or XML document with an associated CSS or XSL style sheet in Internet Explorer, you simply need to open the file in the browser.
2. If the file is stored locally on your computer, you can open it by selecting `File > Open` from the menu and browsing to the file location.
3. If the file is hosted on a web server, you can open it by entering the URL of the file in the address bar of the browser.
4. Once the file is open, the browser will apply the associated style sheet and display the formatted document.
