### Working with Lists and Tables

- Lists and tables are common elements in web pages that can be styled with CSS.
- Lists are used to display a series of items in an ordered or unordered way. Tables are used to display data in rows and columns.
- CSS provides various properties to control the appearance and layout of lists and tables, such as `list-style-type`, `list-style-image`, `list-style-position`, `border-collapse`, `border-spacing`, `empty-cells`, etc.
- To style a list, we can use the `ul` (unordered list), `ol` (ordered list), and `li` (list item) selectors. For example, to change the bullet style of an unordered list, we can use the `list-style-type` property:

```css
ul {
  list-style-type: square;
}
```

- To style a table, we can use the `table`, `tr` (table row), `td` (table data), `th` (table header), and `caption` selectors. For example, to add borders to a table, we can use the `border` property:

```css
table {
  border: 1px solid black;
}

td, th {
  border: 1px solid black;
}
```

- We can also use the `:nth-child()` pseudo-class to select specific rows or columns of a table and apply different styles to them. For example, to make the odd rows of a table have a gray background, we can use the following code:

```css
tr:nth-child(odd) {
  background-color: gray;
}
```

- To align the text in a table cell, we can use the `text-align` property. To align the content of a table cell vertically, we can use the `vertical-align` property. For example, to center the text and the content of a table cell, we can use the following code:

```css
td, th {
  text-align: center;
  vertical-align: middle;
}
```

- To control the width and height of a table or a table cell, we can use the `width` and `height` properties. To control the spacing between the cells of a table, we can use the `border-spacing` property. To control the padding inside the cells of a table, we can use the `padding` property. For example, to make a table have a fixed width of 500 pixels, a spacing of 10 pixels between the cells, and a padding of 5 pixels inside the cells, we can use the following code:

```css
table {
  width: 500px;
  border-spacing: 10px;
}

td, th {
  padding: 5px;
}
```

- To make a table responsive, we can use the `@media` rule to apply different styles depending on the screen size. For example, to make a table have a horizontal scroll bar when the screen width is less than 600 pixels, we can use the following code:

```css
@media (max-width: 600px) {
  table {
    overflow-x: auto;
  }
}
```