## Unit 2 - Elements of HTML

HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications. HTML consists of elements that define the structure and content of a web page.

An HTML element is a piece of code that starts with an opening tag and ends with a closing tag. The opening tag has the name of the element and may have some attributes that provide additional information about the element. The closing tag has the same name as the opening tag, but with a slash (/) before it. The content of the element is everything between the opening and closing tags.

For example, the following code is an HTML element that defines a paragraph of text:

```html
<p>This is a paragraph.</p>
```

The name of the element is `p`, which stands for paragraph. The opening tag is `<p>` and the closing tag is `</p>`. The content of the element is `This is a paragraph.`

Some HTML elements do not have any content, and therefore do not need a closing tag. These are called empty or self-closing elements. For example, the following code is an HTML element that defines a line break:

```html
<br>
```

The name of the element is `br`, which stands for break. The opening tag is `<br>` and there is no closing tag. The element has no content, but it affects the layout of the web page by creating a new line.

Some common HTML elements are:

- `<html>`: The root element that contains the whole web page.
- `<head>`: The element that contains the metadata of the web page, such as the title, the character encoding, the style sheets, and the scripts.
- `<title>`: The element that defines the title of the web page, which is displayed in the browser's tab or window.
- `<body>`: The element that contains the visible content of the web page, such as text, images, links, forms, and tables.
- `<h1>` to `<h6>`: The elements that define the headings of different levels, from the most important (`<h1>`) to the least important (`<h6>`).
- `<p>`: The element that defines a paragraph of text.
- `<a>`: The element that defines a hyperlink to another web page or resource. It has an attribute called `href` that specifies the URL of the destination.
- `<img>`: The element that defines an image. It has an attribute called `src` that specifies the URL of the image file, and an attribute called `alt` that provides a text alternative for the image.
- `<ul>`: The element that defines an unordered list of items. It contains one or more `<li>` elements that define the list items.
- `<ol>`: The element that defines an ordered list of items. It contains one or more `<li>` elements that define the list items.
- `<table>`: The element that defines a table of data. It contains one or more `<tr>` elements that define the table rows, which contain one or more `<td>` elements that define the table cells. It may also contain a `<thead>` element that defines the table header, a `<tbody>` element that defines the table body, and a `<tfoot>` element that defines the table footer.