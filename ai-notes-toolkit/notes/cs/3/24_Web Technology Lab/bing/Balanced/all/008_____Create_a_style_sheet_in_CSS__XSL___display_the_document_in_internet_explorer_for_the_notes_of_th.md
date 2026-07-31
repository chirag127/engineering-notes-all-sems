# Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language that can be used to style XML documents by applying rules to elements based on their names, attributes, or positions.
- XSL (Extensible Stylesheet Language) is a language that can be used to transform XML documents into other formats, such as HTML, by applying templates to elements based on their names, attributes, or patterns.
- To create a style sheet in CSS/ XSL, you need to follow these steps:

  - Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  - In the first line of the file, declare the document to be a style sheet by using the <xsl:stylesheet> or <xsl:transform> element, and specify the version and namespace of XSL. For example:

    ```xml
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    ```

  - In the style sheet, define the rules or templates that you want to apply to the XML document. For CSS, you can use selectors and properties to style elements. For example:

    ```css
    h1 {
      color: blue;
      font-size: 24px;
    }
    ```

    For XSL, you can use <xsl:template> elements to match elements and output the desired content. For example:

    ```xml
    <xsl:template match="title">
      <h1><xsl:value-of select="."/></h1>
    </xsl:template>
    ```

  - Save the file and link it to the XML document by using the <?xml-stylesheet?> processing instruction. For example:

    ```xml
    <?xml version="1.0"?>
    <?xml-stylesheet type="text/css" href="style.css"?>
    <book>
      <title>Web Technology Lab</title>
      <author>Sydney</author>
    </book>
    ```

- To display the document in internet explorer, you need to follow these steps:

  - Open the XML document in internet explorer by using the File > Open menu or by dragging and dropping the file into the browser window.
  - The browser will apply the style sheet to the document and render it accordingly. You can view the source code of the document by using the View > Source menu or by right-clicking on the document and selecting View Source.
  - You can also use the F12 Developer Tools to inspect the elements and styles of the document by using the Tools > F12 Developer Tools menu or by pressing F12 on the keyboard.