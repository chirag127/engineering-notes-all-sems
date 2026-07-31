# CSS Id and Class

- CSS id and class are two types of selectors that can be used to apply styles to specific elements in an HTML document.
- A selector is a pattern that matches one or more elements in the document tree.
- A CSS id selector matches an element that has a specific id attribute value. The syntax for an id selector is a hash sign (#) followed by the id value, for example: `#header`.
- A CSS class selector matches an element that has a specific class attribute value. The syntax for a class selector is a dot (.) followed by the class value, for example: `.red`.
- An element can have multiple class values, separated by spaces, for example: `<p class="red bold">This is a paragraph.</p>`. To match an element that has multiple class values, use multiple class selectors, for example: `.red.bold`.
- An element can have only one id value, which must be unique in the document, for example: `<h1 id="header">This is a heading.</h1>`. To match an element that has a specific id and class value, use a combination of id and class selectors, for example: `#header.red`.
- CSS id and class selectors can be used to target specific elements for styling, such as changing the color, font, size, layout, etc. of the matched elements.
- CSS id and class selectors can also be used to create relationships between elements, such as grouping, nesting, inheritance, specificity, etc. For example, an id selector can be used to identify the parent element of a group of elements, and a class selector can be used to apply a common style to the child elements. For example: `#container .item {display: inline-block;}`. This rule applies the display property to all elements that have the class `item` and are inside the element that has the id `container`.
- CSS id and class selectors are case-sensitive, meaning that `#Header` and `#header` are different selectors, and `.Red` and `.red` are different selectors. It is recommended to use lowercase letters for consistency and readability.