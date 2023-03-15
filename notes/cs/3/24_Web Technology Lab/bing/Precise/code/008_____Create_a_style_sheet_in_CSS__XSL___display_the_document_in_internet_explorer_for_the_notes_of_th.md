### Create a style sheet in CSS/ XSL & display the document in internet explorer

1. **Cascading Style Sheets (CSS)** is a style sheet language used for describing the presentation of a document written in a markup language like HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.

2. **Extensible Stylesheet Language (XSL)** is a language for expressing stylesheets. It consists of three parts: XSL Transformations (XSLT), the XML Path Language (XPath), and XSL Formatting Objects (XSL-FO). XSL specifies the styling of an XML document by using XSLT to transform the XML document into another XML document that uses the formatting vocabulary.

3. To create a style sheet in CSS, you can use an external style sheet, an internal style sheet, or inline styles. An external style sheet is a separate file linked to an HTML document. An internal style sheet is defined in the head section of an HTML document. Inline styles are defined within the HTML element itself.

4. To create a style sheet in XSL, you can use an XSLT stylesheet. An XSLT stylesheet is an XML document that contains a set of template rules. These rules define how the elements and attributes of the source XML document are transformed into the result document.

5. To display a document with a style sheet in Internet Explorer, you can link the style sheet to the HTML document using the `link` element in the head section of the HTML document. For example, to link an external CSS style sheet, you can use the following code:
```
<head>
  <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```
6. To display an XML document with an XSLT stylesheet in Internet Explorer, you can use the `xml-stylesheet` processing instruction. For example, to link an XSLT stylesheet to an XML document, you can use the following code:
```
<?xml-stylesheet type="text/xsl" href="mystyle.xsl"?>
```
7. After linking the style sheet, you can open the HTML or XML document in Internet Explorer to see the styled document.