Hello, I am Sydney, your AI assistant. I can help you with your notes on web designing. Here is the content for the topic of creating page layout and site designs using CSS.

### Creating page layout and site designs using CSS

- CSS stands for Cascading Style Sheets, which is a language that defines how HTML elements are displayed on a web page.
- CSS can be used to create various page layouts and site designs, such as grid, flexbox, columns, responsive, and fluid layouts.
- Page layout is the arrangement of the content and elements on a web page, such as text, images, navigation, and footer.
- Site design is the overall look and feel of a website, such as color scheme, typography, graphics, and animation.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the style attribute of an HTML element, and affects only that element.
  - Internal CSS is written inside the style element in the head section of an HTML document, and affects all the elements in that document.
  - External CSS is written in a separate file with the .css extension, and is linked to an HTML document using the link element in the head section. External CSS affects all the HTML documents that are linked to it.
- CSS has a syntax that consists of three parts: selector, property, and value.
  - Selector is the name of the HTML element or a group of elements that are targeted by the CSS rule.
  - Property is the aspect of the element that is to be styled, such as color, font-size, or margin.
  - Value is the specific setting for the property, such as red, 20px, or 10%.
  - A CSS rule is written as selector { property: value; }, and can have one or more properties and values separated by semicolons.
- CSS has a concept of specificity, which determines which CSS rule has higher priority when there are conflicting rules for the same element.
  - Specificity is calculated based on the type and number of selectors used in a CSS rule, such as element, class, id, or pseudo-class selectors.
  - The more specific a selector is, the higher its specificity value, and the higher its priority.
  - If two selectors have the same specificity value, the one that comes later in the source code has higher priority.
  - Inline CSS has the highest specificity, followed by id selectors, class selectors, element selectors, and universal selector (*).
  - Specificity can be overridden by using the !important keyword after a value, which makes that value the highest priority regardless of the specificity of the selector.
- CSS has a concept of inheritance, which means that some properties are passed down from parent elements to child elements, unless they are overridden by a more specific rule.
  - Inheritance allows for consistent styling of elements without having to repeat the same CSS rules for every element.
  - Some properties that are inherited by default are color, font-family, font-size, and text-align.
  - Some properties that are not inherited by default are background-color, border, margin, and padding.
  - Inheritance can be controlled by using the inherit or initial keywords as values for properties, which make the properties inherit or reset to their default values, respectively.