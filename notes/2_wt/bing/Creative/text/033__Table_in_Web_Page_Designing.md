### Table in Web Page Designing

A table in web page designing is a way of displaying and describing data in the form of rows and columns. A table can be used for various purposes, such as presenting tabular data, creating page layouts, or formatting content. A table consists of the following elements:

- `<table>`: Defines the start and end of a table.
- `<tr>`: Defines a table row, which can contain one or more table cells.
- `<td>`: Defines a table data cell, which can contain any HTML content, such as text, images, lists, links, etc.
- `<th>`: Defines a table header cell, which is usually bold and centered, and can be used to label the columns or rows of a table.
- `<caption>`: Defines a table caption, which is a short description of the table's purpose or content, and is usually displayed above or below the table.
- `<colgroup>`: Defines a group of one or more columns in a table, which can be used to apply common formatting or styling to the columns.
- `<col>`: Defines a column within a `<colgroup>` element, which can be used to specify the width, alignment, or span of the column.
- `<thead>`: Defines the header section of a table, which can contain one or more rows of header cells.
- `<tbody>`: Defines the body section of a table, which can contain one or more rows of data cells.
- `<tfoot>`: Defines the footer section of a table, which can contain one or more rows of footer cells.

Here is an example of a simple HTML table that displays some information about planets:

<table>
  <caption>Planets of the Solar System</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Moons</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mercury</td>
      <td>Terrestrial</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Venus</td>
      <td>Terrestrial</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Earth</td>
      <td>Terrestrial</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Mars</td>
      <td>Terrestrial</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Jupiter</td>
      <td>Jovian</td>
      <td>79</td>
    </tr>
    <tr>
      <td>Saturn</td>
      <td>Jovian</td>
      <td>82</td>
    </tr>
    <tr>
      <td>Uranus</td>
      <td>Jovian</td>
      <td>27</td>
    </tr>
    <tr>
      <td>Neptune</td>
      <td>Jovian</td>
      <td>14</td>
    </tr>
  </tbody>
</table>

To create a table in web page designing, you need to use the HTML table elements and optionally apply some CSS styles to enhance the appearance and functionality of the table. Some of the common CSS properties that can be used to style tables are:

- `border`: Defines the border style, width, and color of the table and its cells.
- `padding`: Defines the space between the content and the border of the table cells.
- `margin`: Defines the space around the table element.
- `width`: Defines the width of the table or its columns.
- `height`: Defines the height of the table or its rows.
- `text-align`: Defines the horizontal alignment of the text in the table cells.
- `vertical-align`: Defines the vertical alignment of the content in the table cells.
- `background-color`: Defines the background color of the table or its cells.
- `color`: Defines the text color of the table or its cells.
- `font-family`: Defines the font family of the text in the table or its cells.
- `font-size`: Defines the font size of the text in the table or its cells.
- `font-weight`: Defines the font weight of the text in the table or its cells.

Here is an example of a CSS stylesheet that applies some styles to the table in the previous example:

<style>