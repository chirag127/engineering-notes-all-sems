### Presenting and using XML in Web Page Designing

XML (eXtensible Markup Language) is a markup language that is used to store and transport data. It is a flexible format that can be used to create structured documents and data sets. XML can be used in web page designing to present data in a structured and organized manner.

Here is an example of how XML can be used in web page designing:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
   </book>
</catalog>
```

This XML document contains a catalog of books, with each book having its own set of elements such as author, title, genre, price, publish_date, and description. This data can be presented on a web page using various methods such as XSLT (eXtensible Stylesheet Language Transformations) or by using JavaScript to parse the XML data and generate HTML content.

Here is an example of how the above XML data can be presented on a web page using XSLT:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
  <body>
  <h2>Book Catalog</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Title</th>
      <th>Author</th>
    </tr>
    <xsl:for-each select="catalog/book">
    <tr>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="author"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
```

This XSLT stylesheet transforms the XML data into an HTML table, presenting the title and author of each book in the catalog. The resulting HTML can be embedded into a web page to present the data to the user.

In summary, XML can be a useful tool in web page designing for presenting and organizing data in a structured manner. It can be used in conjunction with other technologies such as XSLT and JavaScript to generate dynamic and interactive web pages.