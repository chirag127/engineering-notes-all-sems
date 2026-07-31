Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Display for the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content in markdown format:

# Display

- The display property in CSS specifies how an element is displayed on the web page.
- It can control the layout of multiple elements by setting their display value to block, inline, inline-block, flex, grid, or none.
- The default display value for most elements is block or inline.

## Block-level Elements

- A block-level element always starts on a new line and takes up the full width available.
- Examples of block-level elements are `<div>`, `<h1>`-`<h6>`, `<p>`, `<form>`, `<header>`, `<footer>`, `<section>` etc.
- Block-level elements can contain other block-level or inline elements.
- Block-level elements can have a specified width and height, margin, padding, and border.

## Inline Elements

- An inline element does not start on a new line and only takes up as much width as necessary.
- Examples of inline elements are `<span>`, `<a>`, `<img>`, `<button>`, `<input>`, `<label>` etc.
- Inline elements can only contain other inline elements or text.
- Inline elements cannot have a specified width and height, margin-top, margin-bottom, padding-top, or padding-bottom. They can have margin-left, margin-right, padding-left, and padding-right.

## Inline-block Elements

- An inline-block element is a hybrid of block and inline elements. It behaves like an inline element, but it can have a specified width and height, margin, padding, and border like a block element.
- Examples of inline-block elements are `<img>`, `<button>`, `<input>`, `<label>` etc.
- Inline-block elements can contain other block-level or inline elements.
- Inline-block elements respect the vertical-align property.

## Flex Elements

- A flex element is a block-level element that can change its size and order to fit the available space in its container.
- A flex element can have one or more child elements, called flex items, that can be arranged in different directions, alignments, and sizes.
- A flex element can be created by setting the display property to flex or inline-flex on the container element.
- A flex element can have various properties to control the layout of its flex items, such as flex-direction, flex-wrap, justify-content, align-items, align-content, flex-grow, flex-shrink, flex-basis, order, align-self etc.

## Grid Elements

- A grid element is a block-level element that can create a two-dimensional grid layout for its child elements, called grid items.
- A grid element can have one or more rows and columns, and can define the size, position, and alignment of its grid items.
- A grid element can be created by setting the display property to grid or inline-grid on the container element.
- A grid element can have various properties to control the layout of its grid items, such as grid-template-columns, grid-template-rows, grid-template-areas, grid-auto-columns, grid-auto-rows, grid-auto-flow, grid-column-gap, grid-row-gap, grid-gap, grid-column-start, grid-column-end, grid-row-start, grid-row-end, grid-area, justify-items, align-items, justify-content, align-content, justify-self, align-self etc.

## None Elements

- A none element is an element that is not displayed on the web page. It is completely removed from the document flow and does not take up any space.
- A none element can be created by setting the display property to none on the element.
- A none element can be useful for hiding or showing elements based on certain conditions, such as media queries, user interactions, or JavaScript events.