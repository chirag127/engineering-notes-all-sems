### List in Web Page Designing

- A list is a collection of items that are related in some way and displayed in a specific order.
- Lists are useful for organizing and presenting information in a web page, such as menus, steps, categories, etc.
- There are three types of lists in web page designing: ordered lists, unordered lists, and definition lists.

#### Ordered lists
- An ordered list is a list that displays the items in a numerical or alphabetical order.
- An ordered list is created using the `<ol>` tag, and each item is enclosed in a `<li>` tag.
- The `<ol>` tag has an attribute called `type` that can be used to specify the style of the numbering or lettering, such as `1`, `a`, `A`, `i`, or `I`.
- The `<ol>` tag also has an attribute called `start` that can be used to set the starting value of the numbering or lettering, such as `start="5"`.
- The `<ol>` tag can be nested inside another `<ol>` tag to create sublists with different styles of numbering or lettering.
- Example of an ordered list:

<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item
  <ol type="a">
  <li>First subitem</li>
  <li>Second subitem</li>
  </ol>
</li>
<li>Fourth item</li>
</ol>

- Output:

1. First item
2. Second item
3. Third item
   a. First subitem
   b. Second subitem
4. Fourth item

#### Unordered lists
- An unordered list is a list that displays the items in no particular order, usually with bullet points or other symbols.
- An unordered list is created using the `<ul>` tag, and each item is enclosed in a `<li>` tag.
- The `<ul>` tag has an attribute called `type` that can be used to specify the style of the bullet points or symbols, such as `disc`, `circle`, `square`, or an image URL.
- The `<ul>` tag can be nested inside another `<ul>` tag to create sublists with different styles of bullet points or symbols.
- Example of an unordered list:

<ul>
<li>First item</li>
<li>Second item</li>
<li>Third item
  <ul type="circle">
  <li>First subitem</li>
  <li>Second subitem</li>
  </ul>
</li>
<li>Fourth item</li>
</ul>

- Output:

- First item
- Second item
- Third item
  - First subitem
  - Second subitem
- Fourth item

#### Definition lists
- A definition list is a list that displays the items as terms and definitions, usually in a two-column format.
- A definition list is created using the `<dl>` tag, and each term is enclosed in a `<dt>` tag, and each definition is enclosed in a `<dd>` tag.
- The `<dl>` tag can be styled using CSS to change the appearance of the terms and definitions, such as alignment, indentation, font, color, etc.
- Example of a definition list:

<dl>
<dt>HTML</dt>
<dd>Hypertext Markup Language, a standard language for creating web pages.</dd>
<dt>CSS</dt>
<dd>Cascading Style Sheets, a language for adding style and layout to web pages.</dd>
<dt>JavaScript</dt>
<dd>A scripting language for adding interactivity and functionality to web pages.</dd>
</dl>

- Output:

HTML
: Hypertext Markup Language, a standard language for creating web pages.

CSS
: Cascading Style Sheets, a language for adding style and layout to web pages.

JavaScript
: A scripting language for adding interactivity and functionality to web pages.