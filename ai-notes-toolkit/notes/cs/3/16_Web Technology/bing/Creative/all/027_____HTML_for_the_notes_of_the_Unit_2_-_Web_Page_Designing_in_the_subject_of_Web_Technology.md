# HTML

HTML stands for Hyper Text Markup Language. It is the code that is used to structure a web page and its content. HTML consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way.

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

Some HTML elements have no content (like the `<br>` element). These elements are called empty elements or self-closing elements. Empty elements do not have an end tag.

## HTML Attributes

HTML elements can also have attributes, which provide additional information about the element. Attributes are specified in the start tag, and usually have the form of name/value pairs:

```html
<tagname attribute="value">Content goes here...</tagname>
```

For example, the `<a>` element (which defines a hyperlink) has an attribute called `href`, which specifies the URL of the linked resource:

```html
<a href="https://www.w3schools.com">This is a link</a>
```

Some attributes are required for certain elements, while others are optional. You can find a reference of all the attributes for each element on websites like [W3Schools](https://www.w3schools.com/html/html_attributes.asp) or [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes).

## HTML Document Structure

A typical HTML document has the following structure:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Title of the document</title>
</head>
<body>
  The content of the document......
</body>
</html>
```

The `<!DOCTYPE html>` declaration defines the document type and the HTML version. It is required for all HTML documents.

The `<html>` element is the root element of the HTML document. It contains two child elements: `<head>` and `<body>`.

The `<head>` element contains meta information about the document, such as its title, character encoding, style sheets, scripts, etc.

The `<body>` element contains the visible content of the document, such as headings, paragraphs, images, links, forms, etc.

## HTML Headings

HTML headings are defined with the `<h1>` to `<h6>` tags. They are used to create titles or subtitles for the content.

```html
<h1>This is a heading</h1>
<h2>This is a subheading</h2>
<h3>This is a sub-subheading</h3>
<h4>This is a sub-sub-subheading</h4>
<h5>This is a sub-sub-sub-subheading</h5>
<h6>This is a sub-sub-sub-sub-subheading</h6>
```

The `<h1>` element defines the most important heading, while the `<h6>` element defines the least important heading. The browser will display the headings with different sizes, depending on their level.

## HTML Paragraphs

HTML paragraphs are defined with the `<p>` tag. They are used to create blocks of text that are separated by a blank line or a margin.

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

The browser will automatically add some white space (a margin) before and after each paragraph.

## HTML Links

HTML links are defined with the `<a>` tag. They are used to create hyperlinks that allow the user to navigate from one page to another, or to access other resources on the web.

```html
<a href="https://www.w3schools.com">This is a link</a>
```

The `href` attribute specifies the URL of the linked resource. The text between the start and end tags is the link text, which is displayed by the browser and can be clicked by the user.

## HTML Images

HTML images are defined with the `<img>` tag. They are used to embed images into the web page.

```html
<img src="image.jpg" alt="Image description" width="300" height="200">
```

The `src` attribute specifies the URL of the image file. The `alt` attribute provides an alternative text for the