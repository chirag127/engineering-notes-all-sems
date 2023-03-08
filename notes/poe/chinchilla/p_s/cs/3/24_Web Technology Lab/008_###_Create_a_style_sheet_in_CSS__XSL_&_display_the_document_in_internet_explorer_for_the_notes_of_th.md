### Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

Creating a style sheet in CSS or XSL is an important aspect of designing dynamic web pages using Javascript and XML. The style sheet helps in defining the layout, fonts, colors, and other visual elements of a web page. Displaying the document in Internet Explorer requires the use of proper syntax and code.

Here are some important points to remember while creating a style sheet in CSS or XSL:

1. CSS stands for Cascading Style Sheets and is used for defining the layout of a web page. XSL (Extensible Stylesheet Language) is used for defining the layout of an XML document.

2. A style sheet can be created using a text editor like Notepad or a specialized tool like Adobe Dreamweaver.

3. The syntax for defining a style in CSS is as follows:

```css
selector {
  property: value;
}
```

4. The syntax for defining a style in XSL is as follows:

```xsl
<xsl:template match="/">
  <html>
    <head>
      <style type="text/css">
        selector {
          property: value;
        }
      </style>
    </head>
    <body>
      ...
    </body>
  </html>
</xsl:template>
```

5. The style sheet can be linked to an HTML or XML document using the `<link>` tag.

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

6. To display the document in Internet Explorer, the HTML or XML document needs to be opened in the browser. The style sheet will be automatically applied to the document.

In conclusion, creating a style sheet in CSS or XSL is an important aspect of designing dynamic web pages using Javascript and XML. Displaying the document in Internet Explorer requires the proper syntax and code. By following the above points, you can create an attractive and readable web page with ease.