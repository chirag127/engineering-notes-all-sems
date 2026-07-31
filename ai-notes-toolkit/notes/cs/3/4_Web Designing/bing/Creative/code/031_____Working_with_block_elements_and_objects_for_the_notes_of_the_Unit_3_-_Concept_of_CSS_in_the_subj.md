Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of working with block elements and objects for the unit 3 - concept of CSS in the subject of web designing.

```markdown
### Working with block elements and objects

- Block elements are HTML elements that occupy the entire width of their parent container and create a new line before and after themselves. Examples of block elements are `<div>`, `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, etc.
- Block elements can be styled using CSS properties such as `width`, `height`, `margin`, `padding`, `border`, `background`, `display`, `position`, `float`, `clear`, etc.
- Block elements can contain other block elements or inline elements as their children. Inline elements are HTML elements that occupy only the space required by their content and do not create a new line. Examples of inline elements are `<span>`, `<a>`, `<img>`, `<strong>`, `<em>`, `<input>`, `<button>`, etc.
- Inline elements can be styled using CSS properties such as `color`, `font`, `text`, `line-height`, `vertical-align`, `border`, `background`, `padding`, etc. However, they cannot have `width`, `height`, `margin-top`, or `margin-bottom` properties, as they are determined by the parent block element.
- Inline elements can only contain other inline elements or text as their children. They cannot contain block elements.
- To change the default display behavior of an HTML element, the `display` property can be used. The possible values of the `display` property are:
  - `block`: The element behaves like a block element and occupies the entire width of its parent container.
  - `inline`: The element behaves like an inline element and occupies only the space required by its content.
  - `inline-block`: The element behaves like an inline element, but can have `width`, `height`, `margin`, and `padding` properties like a block element.
  - `none`: The element is not displayed and does not affect the layout of other elements.
  - `flex`: The element behaves like a block element and its children are laid out in a flexible way according to the `flex` properties.
  - `grid`: The element behaves like a block element and its children are laid out in a grid according to the `grid` properties.
  - `table`, `table-row`, `table-cell`, etc.: The element behaves like a table element or a part of a table and its children are laid out in a tabular way according to the `table` properties.
- Block elements can also be positioned using the `position` property. The possible values of the `position` property are:
  - `static`: The element is positioned according to the normal flow of the document and does not affect the position of other elements.
  - `relative`: The element is positioned according to the normal flow of the document, but can be offset from its original position using the `top`, `right`, `bottom`, and `left` properties. The offset does not affect the position of other elements.
  - `absolute`: The element is positioned relative to its nearest positioned ancestor (an element with a `position` value other than `static`) or the document body if there is no such ancestor. The element can be placed anywhere using the `top`, `right`, `bottom`, and `left` properties. The element is removed from the normal flow of the document and may overlap with other elements.
  - `fixed`: The element is positioned relative to the viewport (the visible area of the browser window) and does not move when the page is scrolled. The element can be placed anywhere using the `top`, `right`, `bottom`, and `left` properties. The element is removed from the normal flow of the document and may overlap with other elements.
  - `sticky`: The element is positioned according to the normal flow of the document, but sticks to a specified position within the viewport when the page is scrolled. The element can be placed using the `top`, `right`, `bottom`, and `left` properties, which specify the offset from the edge of the viewport. The element is removed from the normal flow of the document only when it is sticking and may overlap with other elements.
```