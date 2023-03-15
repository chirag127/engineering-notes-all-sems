# Working with Text

- Text is the most common element of HTML documents. It can be formatted using various HTML tags and attributes.
- HTML tags are keywords enclosed in angle brackets (< and >) that define the structure and meaning of the text. For example, `<p>` is a tag that indicates a paragraph, and `</p>` is a tag that indicates the end of a paragraph.
- HTML attributes are additional information that modify the behavior or appearance of a tag. They are written inside the opening tag, after the tag name, and consist of a name and a value separated by an equal sign. For example, `<p align="center">` is a tag with an attribute named `align` and a value of `center`, which means the paragraph will be centered on the page.
- HTML tags and attributes are case-insensitive, but it is a good practice to write them in lowercase for consistency and readability.
- HTML tags can be nested, which means one tag can contain another tag inside it. For example, `<p><b>This is bold text</b></p>` is a paragraph tag that contains a bold tag that contains some text. The inner tag is called the child tag, and the outer tag is called the parent tag. The child tag inherits the properties of the parent tag, unless it overrides them with its own attributes or styles.
- HTML tags can be classified into two types: block-level and inline-level. Block-level tags create a new line before and after themselves, and occupy the entire width of the page. Inline-level tags do not create a new line, and only occupy the space needed by their content. For example, `<p>` is a block-level tag, and `<b>` is an inline-level tag.
- Some common block-level tags are:

  - `<h1>` to `<h6>`: headings of different sizes, from largest (`<h1>`) to smallest (`<h6>`).
  - `<p>`: paragraph of text.
  - `<div>`: a generic container for grouping other elements.
  - `<ul>`: an unordered list of items, marked with bullets.
  - `<ol>`: an ordered list of items, marked with numbers or letters.
  - `<li>`: a list item, used inside `<ul>` or `<ol>` tags.
  - `<pre>`: preformatted text, which preserves the spaces and line breaks as they are written in the HTML code.
  - `<blockquote>`: a quotation from another source, usually indented and styled differently from the rest of the text.
  - `<hr>`: a horizontal rule, which creates a line across the page.

- Some common inline-level tags are:

  - `<b>`: bold text.
  - `<i>`: italic text.
  - `<u>`: underlined text.
  - `<em>`: emphasized text, usually rendered as italic.
  - `<strong>`: strong text, usually rendered as bold.
  - `<span>`: a generic container for applying styles or attributes to a part of the text.
  - `<a>`: a hyperlink to another web page or resource, which has an attribute named `href` that specifies the URL of the destination. For example, `<a href="https://www.google.com">Google</a>` creates a link to Google's website.
  - `<img>`: an image, which has an attribute named `src` that specifies the URL of the image file. For example, `<img src="logo.png">` displays the image named logo.png on the page. The `<img>` tag also has optional attributes such as `alt`, `width`, and `height` that provide alternative text, width, and height for the image, respectively.
  - `<br>`: a line break, which creates a new line without starting a new paragraph.