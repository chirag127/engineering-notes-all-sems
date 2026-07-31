## Unit 2 - Elements of HTML

HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications. HTML consists of elements that define the structure and content of a web page.

An HTML element is a piece of code that starts with a start tag and ends with an end tag. The start tag and the end tag usually have the same name, except that the end tag has a forward slash (/) before the name. For example, `<p>` is the start tag and `</p>` is the end tag for a paragraph element.

Some HTML elements are self-closing, which means they do not have an end tag. They are written with a slash (/) at the end of the start tag. For example, `<img>` is a self-closing element for an image.

An HTML element can have attributes that provide additional information about the element. Attributes are written inside the start tag, after the element name. They consist of a name and a value, separated by an equal sign (=). The value is usually enclosed in quotation marks (" "). For example, `<img src="logo.png" alt="Logo">` is an image element with two attributes: src and alt.

The src attribute specifies the source (URL) of the image file, and the alt attribute specifies the alternative text to be displayed if the image cannot be loaded.

Some common HTML elements are:

- `<html>`: The root element that contains the whole web page.
- `<head>`: The element that contains the metadata (information about the web page) such as the title, the character encoding, the style sheets, and the scripts.
- `<title>`: The element that defines the title of the web page, which is displayed in the browser's tab or window.
- `<body>`: The element that contains the visible content of the web page, such as text, images, links, tables, forms, etc.
- `<h1>` to `<h6>`: The elements that define the headings of different levels, from the most important (`<h1>`) to the least important (`<h6>`).
- `<p>`: The element that defines a paragraph of text.
- `<a>`: The element that defines a hyperlink to another web page or resource. It has an attribute called href that specifies the destination (URL) of the link.
- `<img>`: The element that defines an image. It has attributes such as src, alt, width, and height that specify the source, alternative text, and dimensions of the image.
- `<ul>`: The element that defines an unordered list of items, which are marked with bullets.
- `<ol>`: The element that defines an ordered list of items, which are numbered sequentially.
- `<li>`: The element that defines a list item, which is a part of a `<ul>` or `<ol>` element.
- `<div>`: The element that defines a division or a section of the web page. It is often used to group other elements for styling or layout purposes.
- `<span>`: The element that defines a span of text within a larger text. It is often used to apply a specific style or attribute to a part of the text.
- `<table>`: The element that defines a table of data, which consists of rows and columns.
- `<tr>`: The element that defines a table row, which is a part of a `<table>` element.
- `<td>`: The element that defines a table data cell, which is a part of a `<tr>` element.
- `<th>`: The element that defines a table header cell, which is a part of a `<tr>` element. It is usually displayed in bold and centered.
- `<form>`: The element that defines a form, which is a collection of input fields, buttons, checkboxes, radio buttons, etc. that allow the user to submit information to a web server.
- `<input>`: The element that defines an input field, which is a part of a `<form>` element. It has attributes such as type, name, value, placeholder, etc. that specify the type, name, value, and appearance of the input field.
- `<button>`: The element that defines a button, which is a part of a `<form>` element. It has attributes such as type, name, value, etc. that specify the type, name, and value of the button.
- `<label>`: The element that defines a label for an input field, which is a part of a `<form>` element. It has an attribute called for that specifies the id of the input field that the label is associated with.
- `<select>`: The element that defines a drop-down list, which is a part of