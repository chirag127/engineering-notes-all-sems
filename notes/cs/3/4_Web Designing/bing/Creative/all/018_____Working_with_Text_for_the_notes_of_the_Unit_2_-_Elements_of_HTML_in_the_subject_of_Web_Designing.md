# Working with Text

- Text is the most common element of HTML documents. It can be formatted using various HTML tags and attributes.
- HTML tags are keywords enclosed in angle brackets (< and >) that define the structure and meaning of the text. For example, `<p>` is a tag that indicates a paragraph, and `</p>` is a tag that indicates the end of a paragraph.
- HTML attributes are additional information that modify the behavior or appearance of a tag. They are written inside the opening tag, after the tag name, and consist of a name and a value separated by an equal sign. For example, `<p align="center">` is a tag with an attribute named `align` and a value of `center`, which means the paragraph will be centered on the page.
- HTML tags and attributes are case-insensitive, but it is a good practice to use lowercase letters for consistency and readability.
- HTML tags can be nested, which means one tag can contain another tag inside it. For example, `<p><b>This is bold text</b></p>` is a paragraph tag that contains a bold tag inside it, which makes the text bold. The inner tag must be closed before the outer tag, otherwise the HTML document will not be valid.
- HTML tags can be classified into two types: block-level and inline-level. Block-level tags create a new line and occupy the whole width of the page, such as `<p>`, `<h1>`, `<div>`, etc. Inline-level tags do not create a new line and only occupy the space needed by the content, such as `<b>`, `<a>`, `<span>`, etc.
- HTML provides various tags to format the text, such as headings, paragraphs, lists, tables, links, images, etc. Some of the common tags are:

  - `<h1>` to `<h6>`: These tags create headings of different sizes, from largest (`<h1>`) to smallest (`<h6>`). Headings are used to organize the content and make it easier to scan and understand.
  - `<p>`: This tag creates a paragraph, which is a block of text separated by a blank line or a margin from other blocks of text. Paragraphs are used to present the main ideas and details of the content.
  - `<br>`: This tag creates a line break, which is a new line without creating a new paragraph. Line breaks are used to separate lines of text within a paragraph or a block-level element. This tag does not have a closing tag, and it is written as `<br>` or `<br />`.
  - `<hr>`: This tag creates a horizontal rule, which is a horizontal line that separates sections of content. This tag does not have a closing tag, and it is written as `<hr>` or `<hr />`.
  - `<pre>`: This tag creates preformatted text, which preserves the spaces, tabs, and line breaks in the text as they are written in the HTML document. Preformatted text is used to display code, poetry, or any text that requires a fixed-width font and a specific layout.
  - `<b>`: This tag creates bold text, which makes the text thicker and darker. Bold text is used to emphasize or highlight important words or phrases in the content.
  - `<i>`: This tag creates italic text, which makes the text slanted to the right. Italic text is used to indicate titles, foreign words, or any text that needs a different style from the normal text.
  - `<u>`: This tag creates underlined text, which adds a horizontal line below the text. Underlined text is used to indicate links, misspelled words, or any text that needs a visual cue from the normal text.
  - `<s>`: This tag creates strikethrough text, which adds a horizontal line through the text. Strikethrough text is used to indicate deleted, outdated, or incorrect information in the content.
  - `<sub>`: This tag creates subscript text, which makes the text smaller and lower than the normal text. Subscript text is used to indicate chemical formulas, mathematical expressions, or any text that needs a lower position from the normal text.
  - `<sup>`: This tag creates superscript text, which makes the text smaller and higher than the normal text. Superscript text is used to indicate exponents, footnotes, or any text that needs a higher position from the normal text.
  - `<span>`: This tag creates a span of text, which is an inline-level element that does not have any specific meaning or style by itself. Span tags are used to group text together and apply styles or attributes to them using CSS or JavaScript.
  -