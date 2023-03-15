# Unit 3 - Concept of CSS

CSS stands for Cascading Style Sheets. It is a language that is used to style and layout web pages. CSS can control the appearance of various elements on a web page, such as font, color, size, spacing, alignment, background, border, animation, and more. CSS can also make web pages responsive to different devices and screen sizes by using media queries and flexible grids.

Some of the main concepts of CSS are:

- CSS rules: A CSS rule consists of a selector and a declaration block. The selector specifies which element or elements the rule applies to. The declaration block contains one or more declarations, each of which consists of a property and a value. For example, `p {color: blue;}` is a CSS rule that applies to all `<p>` elements and sets their text color to blue.
- CSS inheritance: CSS inheritance is a mechanism that allows some CSS properties to be passed from parent elements to child elements. For example, if you set the font-family property on the `<body>` element, all the text elements inside the body will inherit the same font-family, unless you override it with a more specific rule.
- CSS specificity: CSS specificity is a measure of how specific a selector is, and how it affects the priority of applying CSS rules. The more specific a selector is, the higher its specificity value, and the more likely it is to override other rules with lower specificity values. For example, an ID selector has a higher specificity than a class selector, and a class selector has a higher specificity than a tag selector.
- CSS cascade: CSS cascade is a process that determines the final value of a CSS property for an element, based on the order and importance of the CSS rules that match the element. The cascade follows these steps:

  - Find all the CSS rules that apply to the element, based on the selector matching.
  - Sort the rules by their source (user agent, user, or author) and importance (normal or !important).
  - Sort the rules by their specificity, with more specific rules overriding less specific ones.
  - Sort the rules by their order of appearance, with later rules overriding earlier ones.
- CSS box model: CSS box model is a concept that describes how the size and layout of an element are calculated. Every element is represented as a rectangular box, which has four edges: content edge, padding edge, border edge, and margin edge. The box model defines the following properties:

  - Content area: The area where the element's content (text, images, etc.) is displayed. The width and height of the content area are determined by the content-width and content-height properties, or by the element's intrinsic size if not specified.
  - Padding area: The area around the content area that provides some space between the content and the border. The width and height of the padding area are determined by the padding-top, padding-right, padding-bottom, and padding-left properties.
  - Border area: The area around the padding area that displays the element's border. The width and height of the border area are determined by the border-top-width, border-right-width, border-bottom-width, and border-left-width properties, and the style and color of the border are determined by the border-style and border-color properties.
  - Margin area: The area around the border area that provides some space between the element and its surrounding elements. The width and height of the margin area are determined by the margin-top, margin-right, margin-bottom, and margin-left properties.

  The total width and height of an element's box are calculated by adding the widths and heights of the content, padding, border, and margin areas. The box-sizing property can change how the box model works, by making the content area include the padding and border areas, or by making the border area include the margin area.