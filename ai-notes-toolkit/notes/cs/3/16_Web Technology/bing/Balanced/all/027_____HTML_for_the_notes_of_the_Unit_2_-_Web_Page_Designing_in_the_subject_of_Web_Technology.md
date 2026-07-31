# HTML

HTML stands for Hyper Text Markup Language. It is the code that is used to structure a web page and its content. HTML consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way. For example, content could be structured within a set of paragraphs, a list of bulleted points, or using images and data tables.

## HTML Elements

An HTML element is defined by a start tag, some content, and an end tag:

```html
<tagname>Content goes here...</tagname>
```

The HTML element is everything from the start tag to the end tag:

```html
<h1>My First Heading</h1>
<p>My first paragraph.</p>
```

Some HTML elements have no content (like the `<br>` element). These elements are called empty elements. Empty elements do not have an end tag.

## HTML Attributes

HTML elements can also have attributes, which provide additional information about the element. Attributes are specified in the start tag, and usually have the form of name/value pairs:

```html
<tagname attribute="value">Content goes here...</tagname>
```

For example, the `<a>` element (which defines a hyperlink) has an attribute called `href`, which specifies the URL of the linked resource:

```html
<a href="https://www.w3schools.com">This is a link</a>
```

## HTML Document Structure

A typical HTML document has the following structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Metadata goes here -->
    <title>Page title</title>
  </head>
  <body>
    <!-- Visible content goes here -->
  </body>
</html>
```

The `<!DOCTYPE html>` declaration defines the document type, and helps browsers to display web pages correctly.

The `<html>` element is the root element of an HTML page.

The `<head>` element contains metadata (information about the document) that is not displayed on the web page.

The `<title>` element specifies the title of the document, which is shown in the browser's tab or window title.

The `<body>` element contains the visible content of the web page, such as headings, paragraphs, images, links, etc.