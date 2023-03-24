### Creating a Style Sheet in CSS/XSL and Displaying the Document in Internet Explorer

In the Unit 3 of the Web Technology Lab, we will learn about designing dynamic web pages using Javascript and XML. One of the important aspects of web page design is creating a style sheet. A style sheet is a collection of rules that specify how a web page should be displayed. In this unit, we will learn how to create a style sheet in CSS/XSL and display the document in Internet Explorer. 

Here are the steps to create a style sheet in CSS/XSL and display the document in Internet Explorer:

1. Create a new HTML document and save it with a .html extension. 

2. In the head section of the HTML document, create a link to the CSS/XSL file. For CSS, use the following code:

  ```html
  <link rel="stylesheet" type="text/css" href="style.css">
  ```

  For XSL, use the following code:

  ```html
  <link rel="stylesheet" type="text/xsl" href="style.xsl">
  ```

3. Create a new CSS/XSL file and save it with a .css/.xsl extension. 

4. In the CSS/XSL file, write the rules that specify how the web page should be displayed. For example, to change the color of the text to red, use the following code in CSS:

  ```css
  body {
    color: red;
  }
  ```

  In XSL, use the following code:

  ```xsl
  <xsl:template match="/">
    <html>
      <head>
        <style type="text/css">
          body {
            color: red;
          }
        </style>
      </head>
      <body>
        <xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>
  ```

5. Save the CSS/XSL file and open the HTML document in Internet Explorer. 

6. The web page should now be displayed with the styles specified in the CSS/XSL file.

In conclusion, creating a style sheet in CSS/XSL is an important aspect of web page design. By following the above steps, we can create a style sheet and display the document in Internet Explorer.