# Working with Lists and Tables

## Lists

- Lists are used to display a series of related items in a web page.
- There are two types of lists in HTML: ordered lists and unordered lists.
- Ordered lists use numbers, letters, or roman numerals to indicate the order of the items. They are created with the `<ol>` tag and each item is enclosed in a `<li>` tag.
- Unordered lists use bullets, squares, or circles to indicate the items. They are created with the `<ul>` tag and each item is enclosed in a `<li>` tag.
- Lists can be nested inside other lists to create sublists. The nested list must be placed inside a `<li>` tag of the parent list.
- Lists can be styled with CSS properties such as `list-style-type`, `list-style-image`, `list-style-position`, `margin`, `padding`, `border`, etc.

## Tables

- Tables are used to display data in rows and columns in a web page.
- Tables are created with the `<table>` tag and each row is enclosed in a `<tr>` tag. Each cell in a row is enclosed in a `<td>` tag for data or a `<th>` tag for headings.
- Tables can have a caption that describes the content of the table. The caption is placed inside a `<caption>` tag immediately after the `<table>` tag.
- Tables can have a border that separates the cells. The border width can be specified with the `border` attribute of the `<table>` tag or the `border` property of CSS.
- Tables can have a spacing between the cells and a padding inside the cells. The spacing can be specified with the `cellspacing` attribute of the `<table>` tag or the `border-spacing` property of CSS. The padding can be specified with the `cellpadding` attribute of the `<table>` tag or the `padding` property of CSS.
- Tables can have different alignments for the text and the cells. The alignment can be specified with the `align` and `valign` attributes of the `<table>`, `<tr>`, `<td>`, or `<th>` tags or the `text-align` and `vertical-align` properties of CSS.
- Tables can have different widths and heights for the cells. The width and height can be specified with the `width` and `height` attributes of the `<table>`, `<tr>`, `<td>`, or `<th>` tags or the `width` and `height` properties of CSS.
- Tables can have different backgrounds for the cells. The background can be specified with the `bgcolor` attribute of the `<table>`, `<tr>`, `<td>`, or `<th>` tags or the `background-color` and `background-image` properties of CSS.
- Tables can have different borders for the cells. The border can be specified with the `border` attribute of the `<table>`, `<tr>`, `<td>`, or `<th>` tags or the `border` property of CSS. The border style, color, and width can be further customized with the `border-style`, `border-color`, and `border-width` properties of CSS.
- Tables can have different layouts for the cells. The layout can be specified with the `colspan` and `rowspan` attributes of the `<td>` or `<th>` tags to merge multiple cells horizontally or vertically. The layout can also be specified with the `<colgroup>` and `<col>` tags to define groups of columns and apply styles to them.