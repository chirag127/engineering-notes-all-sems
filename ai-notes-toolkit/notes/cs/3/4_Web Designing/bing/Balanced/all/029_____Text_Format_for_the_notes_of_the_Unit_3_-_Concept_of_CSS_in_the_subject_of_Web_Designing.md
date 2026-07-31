# Text Format for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, borders, backgrounds, and other aspects of the appearance of a web page.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the style attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the style element in the head section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the .css extension and linked to an HTML document using the link element in the head section. It affects all the elements in the linked document and has the lowest priority.
- CSS uses selectors to target HTML elements and apply styles to them. There are different types of selectors, such as element, class, id, attribute, pseudo-class, and pseudo-element selectors.
- CSS uses properties and values to define the styles for the selected elements. There are many properties and values in CSS, such as color, font-family, font-size, margin, padding, border, display, position, etc.
- CSS uses the box model to describe the layout of an HTML element. The box model consists of four parts: content, padding, border, and margin.
  - Content is the actual text or image inside the element.
  - Padding is the space between the content and the border of the element.
  - Border is the line that surrounds the element.
  - Margin is the space between the border of the element and the adjacent elements.
- CSS uses the cascade to determine the final style of an element. The cascade is the process of combining multiple sources of CSS rules and resolving any conflicts among them. The cascade follows these steps:
  - Find all the CSS rules that apply to the element, based on the selectors and the source order.
  - Sort the rules by their specificity, which is a measure of how precise the selector is. The more specific the selector, the higher the specificity. The specificity is calculated based on the following order: inline styles, id selectors, class selectors, attribute selectors, pseudo-class selectors, element selectors, and universal selector.
  - Apply the rules in the order of their specificity, from lowest to highest. If two rules have the same specificity, the one that comes later in the source order wins.
  - If there are still conflicts, apply the importance, which is a keyword that can be added to a CSS rule to give it more weight. The importance can be either normal or !important. The !important rules override the normal rules, regardless of their specificity or source order.