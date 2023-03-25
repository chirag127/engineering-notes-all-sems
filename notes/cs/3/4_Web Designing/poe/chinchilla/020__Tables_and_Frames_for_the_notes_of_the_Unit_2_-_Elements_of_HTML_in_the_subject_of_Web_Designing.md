### Tables and Frames

Tables and frames are important elements in HTML for displaying data and organizing content. In this section, we will discuss the basics of tables and frames in HTML.

#### Tables

Tables in HTML are used to display data in rows and columns. The basic structure of a table consists of the following elements:

- `<table>`: This tag is used to create the table element.
- `<tr>`: This tag is used to create a row in the table.
- `<td>`: This tag is used to create a cell in the table.

The following is an example of a basic HTML table:

```html
<table>
  <tr>
    <td>Cell 1</td>
    <td>Cell 2</td>
  </tr>
  <tr>
    <td>Cell 3</td>
    <td>Cell 4</td>
  </tr>
</table>
```

In the above example, we have created a table with two rows and two columns. Each cell contains some text (Cell 1, Cell 2, etc.).

Apart from the basic structure, tables in HTML have several attributes that can be used to customize their appearance and behavior. Some of the most commonly used attributes are:

- `border`: Specifies the border width around the table.
- `cellpadding`: Specifies the space between the cell content and the cell border.
- `cellspacing`: Specifies the space between cells.
- `width`: Specifies the width of the table.

#### Frames

Frames in HTML are used to divide a web page into multiple sections, each with its own content. Frames are created using the `<frame>` tag. The basic structure of a frame consists of the following elements:

- `<frameset>`: This tag is used to create the frame set element.
- `<frame>`: This tag is used to create a frame in the frame set.

The following is an example of a basic HTML frame set:

```html
<frameset cols="25%,75%">
  <frame src="menu.html">
  <frame src="content.html">
</frameset>
```

In the above example, we have created a frame set with two frames. The first frame contains a menu, and the second frame contains the main content.

Apart from the basic structure, frames in HTML have several attributes that can be used to customize their appearance and behavior. Some of the most commonly used attributes are:

- `cols`: Specifies the width of each column in the frame set.
- `rows`: Specifies the height of each row in the frame set.
- `border`: Specifies the border width around each frame.
- `frameborder`: Specifies whether to display a border around each frame.

Note: Frames are not recommended for modern web design as they have several drawbacks, including accessibility issues and problems with search engine optimization. It is recommended to use CSS layout techniques instead.