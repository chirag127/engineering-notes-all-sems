### Table in Web Page Designing

- A table is a way of organizing and displaying data in rows and columns on a web page.
- A table consists of a `<table>` element that contains one or more `<tr>` elements (table rows), each of which contains one or more `<td>` elements (table data cells).
- A table can also have a `<caption>` element that provides a title or description for the table, and `<thead>`, `<tbody>`, and `<tfoot>` elements that group the table rows into header, body, and footer sections.
- A table can have borders, spacing, padding, alignment, and background properties that affect its appearance and layout.
- A table can be nested inside another table to create complex layouts, but this is not recommended as it can make the code difficult to read and maintain, and can cause accessibility and responsiveness issues.
- A table can be styled with CSS to enhance its design and functionality, such as adding hover effects, alternating row colors, fixed headers, scrollable bodies, and responsive breakpoints.
- A table can be used for various purposes on a web page, such as displaying tabular data, creating forms, making comparisons, and laying out content.
- A table should be used only when the data is logically related and has a clear structure, and not for purely visual purposes. A table should also have a meaningful caption and proper headings to make it accessible and understandable for all users.

Some examples of table syntax and output are:

| Syntax | Output |
|--------|--------|
| `<table>`<br>`<tr>`<br>`<td>A</td>`<br>`<td>B</td>`<br>`</tr>`<br>`<tr>`<br>`<td>C</td>`<br>`<td>D</td>`<br>`</tr>`<br>`</table>` | A | B |<br>| C | D |
| `<table border="1">`<br>`<caption>Example table</caption>`<br>`<tr>`<br>`<th>Name</th>`<br>`<th>Age</th>`<br>`</tr>`<br>`<tr>`<br>`<td>John</td>`<br>`<td>25</td>`<br>`</tr>`<br>`<tr>`<br>`<td>Mary</td>`<br>`<td>30</td>`<br>`</tr>`<br>`</table>` | Example table<br>| Name | Age |<br>| John | 25 |<br>| Mary | 30 |
| `<table style="width: 100%;">`<br>`<tr>`<br>`<td style="background-color: yellow;">Yellow</td>`<br>`<td style="background-color: green;">Green</td>`<br>`</tr>`<br>`<tr>`<br>`<td style="background-color: blue;">Blue</td>`<br>`<td style="background-color: red;">Red</td>`<br>`</tr>`<br>`</table>` | Yellow | Green |<br>| Blue | Red |