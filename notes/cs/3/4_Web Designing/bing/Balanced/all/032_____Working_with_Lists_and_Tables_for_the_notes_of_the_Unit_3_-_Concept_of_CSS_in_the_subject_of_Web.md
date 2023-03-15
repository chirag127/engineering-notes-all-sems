# Working with Lists and Tables

- Lists and tables are common elements in web design that can be styled with CSS.
- Lists are used to display a series of items in a vertical or horizontal order. There are three types of lists in HTML: ordered lists, unordered lists, and definition lists.
- Tables are used to display data in rows and columns. Tables can have a caption, a header, a footer, and a body. Tables can also be nested inside other tables.
- CSS can be used to change the appearance and layout of lists and tables, such as the color, font, size, spacing, alignment, border, background, etc.
- Some of the CSS properties that can be applied to lists and tables are:

  - `list-style-type`: specifies the type of bullet or number for list items, such as disc, circle, square, decimal, lower-alpha, etc.
  - `list-style-image`: specifies an image to use as the bullet for list items.
  - `list-style-position`: specifies the position of the list marker relative to the list item, such as inside or outside.
  - `list-style`: a shorthand property that combines the above three properties.
  - `display`: specifies how the list or table element is displayed, such as block, inline, inline-block, table, table-row, table-cell, etc.
  - `border`: specifies the width, style, and color of the border for the list or table element, or its individual sides.
  - `border-collapse`: specifies whether the borders of adjacent table cells are collapsed into a single border or separated.
  - `border-spacing`: specifies the distance between the borders of adjacent table cells when they are separated.
  - `padding`: specifies the space between the content and the border of the list or table element, or its individual sides.
  - `margin`: specifies the space outside the border of the list or table element, or its individual sides.
  - `width` and `height`: specify the width and height of the list or table element, or its individual cells.
  - `text-align` and `vertical-align`: specify the horizontal and vertical alignment of the content of the list or table element, or its individual cells.
  - `background`: specifies the background color or image for the list or table element, or its individual cells.
  - `:hover`, `:active`, and `:visited`: pseudo-classes that can be used to change the style of the list or table element, or its individual cells, when they are hovered over, clicked, or visited by the user.

- Here is an example of HTML code for a list and a table, and the corresponding CSS code to style them:

```html
<!-- HTML code for a list and a table -->
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Cherry</li>
</ul>

<table>
  <caption>Fruits and Colors</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Apple</td>
      <td>Red</td>
    </tr>
    <tr>
      <td>Banana</td>
      <td>Yellow</td>
    </tr>
    <tr>
      <td>Cherry</td>
      <td>Red</td>
    </tr>
  </tbody>
</table>
```

```css
/* CSS code to style the list and the table */
ul {
  list-style-type: none; /* remove the default bullets */
  display: inline-block; /* make the list horizontal */
  padding: 0; /* remove the default padding */
  margin: 0; /* remove the default margin */
}

li {
  display: inline-block; /* make the list items horizontal */
  margin: 10px; /* add some space between the list items */
  padding: 10px; /* add some space around the list items */
  border: 2px solid black; /* add a black border to the list items */
  background: lightgreen; /* add a light green background to the list items */
}

li:hover {
  background: green; /* change the background to green when the list item is hovered over */
  color: white; /* change the text color to white when the list item is hovered over */
}

table {
  border-collapse: collapse; /* collapse the borders of the table cells */
  width: 50%; /* set the width of the table to 50% of the parent element */
  margin: 0 auto; /* center the table horizontally */
}

caption {