### Table in Web Page Designing

- A table is a way of organizing and displaying data in rows and columns on a web page.
- A table consists of a table element and one or more row elements (tr) that contain one or more cell elements (td or th).
- A table can have a caption element that describes the purpose or content of the table.
- A table can have a thead element that contains the header row(s) of the table, a tbody element that contains the body row(s) of the table, and a tfoot element that contains the footer row(s) of the table.
- A table can have a border attribute that specifies the width of the border around the table and its cells, a cellspacing attribute that specifies the space between the cells, and a cellpadding attribute that specifies the space between the cell content and the cell border.
- A table can have a width attribute that specifies the width of the table, a height attribute that specifies the height of the table, and an align attribute that specifies the horizontal alignment of the table (left, center, or right).
- A table can have a summary attribute that provides a brief description of the table for accessibility purposes.
- A table cell can have a colspan attribute that specifies the number of columns that the cell spans, a rowspan attribute that specifies the number of rows that the cell spans, and an align attribute that specifies the horizontal alignment of the cell content (left, center, or right).
- A table cell can have a width attribute that specifies the width of the cell, a height attribute that specifies the height of the cell, and a valign attribute that specifies the vertical alignment of the cell content (top, middle, or bottom).
- A table cell can have a bgcolor attribute that specifies the background color of the cell, a background attribute that specifies the background image of the cell, and a style attribute that specifies the CSS style of the cell.
- A table header cell (th) can have a scope attribute that specifies the scope of the header cell (row, col, rowgroup, or colgroup).

- An example of a simple table is:

<table border="1" cellspacing="0" cellpadding="5">
  <caption>A simple table</caption>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Gender</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>25</td>
    <td>Female</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>30</td>
    <td>Male</td>
  </tr>
  <tr>
    <td>Charlie</td>
    <td>28</td>
    <td>Male</td>
  </tr>
</table>

- An example of a table with colspan and rowspan is:

<table border="1" cellspacing="0" cellpadding="5">
  <caption>A table with colspan and rowspan</caption>
  <tr>
    <th colspan="3">Products</th>
  </tr>
  <tr>
    <th>Category</th>
    <th>Name</th>
    <th>Price</th>
  </tr>
  <tr>
    <td rowspan="2">Fruits</td>
    <td>Apple</td>
    <td>$1</td>
  </tr>
  <tr>
    <td>Banana</td>
    <td>$0.5</td>
  </tr>
  <tr>
    <td rowspan="2">Vegetables</td>
    <td>Carrot</td>
    <td>$0.8</td>
  </tr>
  <tr>
    <td>Tomato</td>
    <td>$0.6</td>
  </tr>
</table>

- An example of a table with thead, tbody, and tfoot is:

<table border="1" cellspacing="0" cellpadding="5">
  <caption>A table with thead, tbody, and tfoot</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>25</td>
      <td>Female</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>30</td>
      <td>Male</td>
    </tr>
    <tr>
      <td>Charlie</td>
      <td>28</td>