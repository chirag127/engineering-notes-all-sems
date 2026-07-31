### Basic structure of an HTML document

HTML stands for HyperText Markup Language. It is a language that describes the structure and content of a web page. HTML consists of a series of elements that are enclosed by tags. Tags are written inside angle brackets, such as `<tag>`.

The basic structure of an HTML document consists of five elements:

- `<!DOCTYPE>`: This element declares the document type and the version of HTML used. It helps the browser to render the page correctly. The most common doctype for HTML5 is `<!DOCTYPE html>`.
- `<html>`: This element is the root element of the document. It contains all the other elements. It has an attribute called `lang` that specifies the language of the document, such as `lang="en"` for English.
- `<head>`: This element contains information about the document, such as the title, meta data, style sheets, scripts, etc. It is not visible on the web page, but it affects how the page is displayed and processed by the browser.
- `<title>`: This element is a child of the `<head>` element. It defines the title of the document, which is shown in the browser's tab or window. It is required for every HTML document.
- `<body>`: This element contains the visible content of the document, such as headings, paragraphs, images, links, etc. It is a child of the `<html>` element.

A simple HTML document example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Page Title</title>
</head>
<body>
  <h1>Heading</h1>
  <p>Paragraph</p>
  <a href="https://www.example.com">Link</a>
</body>
</html>
```

Some points to remember about the basic structure of an HTML document are:

- HTML elements are case-insensitive, but it is a good practice to write them in lowercase.
- HTML elements can have attributes that provide additional information or functionality. Attributes are written inside the start tag, after the element name, and have the format `name="value"`.
- HTML elements can be nested inside other elements, creating a hierarchical structure. The nested element is called the child element, and the element that contains it is called the parent element. Every element must have a matching closing tag, except for some self-closing elements, such as `<img>` or `<br>`.
- HTML elements can be categorized into two types: block-level and inline-level. Block-level elements occupy the entire width of the page and start on a new line, such as `<div>`, `<p>`, `<h1>`, etc. Inline-level elements occupy only the space needed by their content and do not start on a new line, such as `<span>`, `<a>`, `<img>`, etc.
- HTML elements can be further classified into semantic and non-semantic elements. Semantic elements have a meaning that describes their content or function, such as `<header>`, `<nav>`, `<article>`, etc. Non-semantic elements have no meaning and are used for styling or formatting purposes, such as `<div>`, `<span>`, `<b>`, etc. Semantic elements are preferred for better accessibility and SEO.