Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of margin properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing.

# Margin properties

- The margin properties in CSS are used to create space around elements, outside of any defined borders.
- The margin properties can be set for all four sides of an element, or for each side individually.
- The margin properties are:

  - `margin`: a shorthand property that sets the margin for all four sides of an element.
  - `margin-top`: sets the margin for the top side of an element.
  - `margin-right`: sets the margin for the right side of an element.
  - `margin-bottom`: sets the margin for the bottom side of an element.
  - `margin-left`: sets the margin for the left side of an element.

- The margin properties can take different values, such as:

  - A length value, such as `px`, `em`, `rem`, `vw`, `vh`, etc. For example, `margin: 10px;` sets a 10-pixel margin for all four sides of an element.
  - A percentage value, relative to the width of the containing element. For example, `margin: 5%;` sets a 5% margin for all four sides of an element.
  - The keyword `auto`, which lets the browser calculate the margin for an element. For example, `margin: auto;` centers an element horizontally within its container.
  - The keyword `inherit`, which inherits the margin value from the parent element. For example, `margin: inherit;` applies the same margin as the parent element to the current element.

- The margin properties can also be used to create negative space, by using negative values. For example, `margin: -10px;` reduces the space around an element by 10 pixels on all four sides.

- The margin properties can affect the layout of an element and its surrounding elements, by creating space between them or overlapping them. For example, if two elements have a positive margin, they will be pushed apart by the margin. If two elements have a negative margin, they will overlap by the margin.

- The margin properties can also collapse, which means that if two adjacent elements have margins, the larger margin value will be applied and the smaller one will be ignored. For example, if an element has a `margin-bottom: 20px;` and the next element has a `margin-top: 10px;`, the total margin between them will be 20 pixels, not 30 pixels. Margin collapsing only occurs for vertical margins, not horizontal margins.