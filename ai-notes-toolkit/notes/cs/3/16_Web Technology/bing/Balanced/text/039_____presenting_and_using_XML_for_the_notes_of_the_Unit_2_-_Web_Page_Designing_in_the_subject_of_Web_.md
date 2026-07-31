### Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- XML stands for **eXtensible Markup Language**. It is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
- XML was designed to **store and transport data**, not to display it. It is a **textual data format** with strong support via Unicode for different human languages.
- XML is **extensible** because it allows users to create their own tags and attributes to define the structure and meaning of their data. This makes XML a powerful way to store data in a format that can be stored, searched, and shared.
- XML is **dynamic** because it is used to transport the data between different applications and platforms. XML can be used to exchange data between web servers and browsers, or between different databases and software systems.
- XML is **simple**, **general**, and **usable** across the Internet. It has a simple syntax that is easy to learn and write. It is general because it can be used for any kind of data, not just for web pages. It is usable across the Internet because it is platform-independent and widely supported by many tools and languages.
- XML can be used for designing web pages in an application by using **XML stylesheets**. XML stylesheets are files that describe how to display XML data on a web page. There are two types of XML stylesheets: **XSLT** and **CSS**.
  - XSLT stands for **eXtensible Stylesheet Language Transformations**. It is a language that can transform XML data into HTML, XHTML, or other XML formats. XSLT can also perform calculations, sorting, filtering, and other operations on XML data.
  - CSS stands for **Cascading Style Sheets**. It is a language that can define the style and layout of HTML or XML elements. CSS can also control the fonts, colors, backgrounds, borders, and other aspects of the presentation of XML data.
- XML can be used for creating web pages by following these steps:
  - Create an XML file that contains the data to be displayed on the web page. Use tags and attributes that describe the structure and meaning of the data. For example, this XML file contains a note with a to, from, heading, and body elements:

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
  ```

  - Create an XML stylesheet file that defines how to display the XML data on the web page. Use XSLT or CSS to transform or style the XML data. For example, this XSLT file transforms the XML data into HTML and adds some style rules:

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
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
          <h1><xsl:value-of select="note/heading"/></h1>
          <p><xsl:value-of select="note/body"/></p>
          <p>From: <xsl:value-of select="note/from"/></p>
          <p>To: <xsl:value-of select="note/to"/></p>
        </body>
      </html>
    </xsl:template>
  </xsl:stylesheet>
  ```

  - Link the XML file and the XML stylesheet file together by using the **xml-stylesheet** processing instruction in the XML file. For example, this line links the XML file to the XSLT file:

  ```xml
  <?xml-stylesheet type="text/xsl" href="note.xsl"?>
  ```

  - Save the XML file and the