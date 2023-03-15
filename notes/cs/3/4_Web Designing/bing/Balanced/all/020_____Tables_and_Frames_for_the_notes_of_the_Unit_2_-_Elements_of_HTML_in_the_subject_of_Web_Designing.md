# Tables and Frames

## Tables

- A table is a way of organizing data in rows and columns.
- HTML tables are created using the `<table>` element, which contains one or more `<tr>` elements (table rows), each containing one or more `<td>` elements (table data cells).
- The `<th>` element can be used to create table headers, which are usually displayed in bold and centered.
- The `<caption>` element can be used to add a title or description to a table.
- The `<thead>`, `<tbody>` and `<tfoot>` elements can be used to group the table rows into logical sections.
- The `<col>` and `<colgroup>` elements can be used to apply styles or attributes to one or more columns of a table.
- The `<rowspan>` and `<colspan>` attributes can be used to merge two or more cells across rows or columns.
- The `<table>` element supports the following attributes:
  - `align`: specifies the horizontal alignment of the table (left, right or center).
  - `bgcolor`: specifies the background color of the table.
  - `border`: specifies the width of the border around the table (in pixels).
  - `cellpadding`: specifies the space between the cell content and the cell border (in pixels).
  - `cellspacing`: specifies the space between the cells (in pixels).
  - `frame`: specifies which sides of the table should have a border (void, above, below, hsides, vsides, lhs, rhs, box or border).
  - `rules`: specifies which parts of the table should have internal borders (none, groups, rows, cols or all).
  - `summary`: specifies a summary of the table content for accessibility purposes.
  - `width`: specifies the width of the table (in pixels or percentage).

## Frames

- A frame is a way of dividing a web page into multiple sections, each displaying a different HTML document.
- HTML frames are created using the `<frameset>` element, which contains one or more `<frame>` elements, each specifying the source URL of the document to be displayed in that section.
- The `<frameset>` element supports the following attributes:
  - `cols`: specifies the number and size of columns in the frameset (in pixels, percentage or relative units).
  - `rows`: specifies the number and size of rows in the frameset (in pixels, percentage or relative units).
- The `<frame>` element supports the following attributes:
  - `name`: specifies a name for the frame, which can be used as a target for links or forms.
  - `src`: specifies the URL of the document to be displayed in the frame.
  - `frameborder`: specifies whether the frame should have a border or not (0 or 1).
  - `marginheight`: specifies the height of the margin around the frame content (in pixels).
  - `marginwidth`: specifies the width of the margin around the frame content (in pixels).
  - `noresize`: specifies that the frame should not be resizable by the user.
  - `scrolling`: specifies whether the frame should have scrollbars or not (yes, no or auto).
- The `<noframes>` element can be used to provide alternative content for browsers that do not support frames.