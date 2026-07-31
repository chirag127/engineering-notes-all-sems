Hello, I am Sydney, your AI assistant. I can help you with your notes on web designing. Here is the content for the topic of creating page layout and site designs using CSS.

### Creating page layout and site designs using CSS

- CSS stands for Cascading Style Sheets, which is a language that defines how HTML elements are displayed on a web page.
- CSS can be used to create various page layouts and site designs, such as grid, flexbox, columns, responsive, and fluid layouts.
- A page layout is the arrangement of the content and the structure of a web page, such as the header, footer, navigation, main content, sidebar, etc.
- A site design is the overall look and feel of a website, such as the color scheme, typography, images, icons, etc.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the style attribute of an HTML element, and affects only that element.
  - Internal CSS is written inside the style element in the head section of an HTML document, and affects all the elements in that document.
  - External CSS is written in a separate file with the .css extension, and is linked to an HTML document using the link element in the head section. External CSS can affect multiple HTML documents that share the same style sheet.
- CSS has a syntax that consists of three parts: selector, property, and value.
  - A selector is the name of an HTML element, a class, an id, or a pseudo-class that specifies which element(s) to apply the style to.
  - A property is the name of a style attribute, such as color, font-size, margin, etc.
  - A value is the value assigned to a property, such as red, 16px, 10px, etc.
  - A CSS rule is a combination of a selector and one or more property-value pairs, separated by a colon and enclosed in curly braces, such as `p {color: red; font-size: 16px;}`.
- CSS has a concept of specificity, which determines which rule has more priority when there are conflicting rules for the same element. Specificity is calculated based on the type and number of selectors used in a rule, such as element, class, id, and inline. The more specific a selector is, the higher its specificity value, and the more likely it is to override a less specific selector. For example, an id selector has a higher specificity than a class selector, and a class selector has a higher specificity than an element selector.
- CSS has a concept of inheritance, which means that some properties are passed down from parent elements to child elements, unless they are overridden by a more specific rule. For example, the color property is inherited by default, so if the body element has a color of blue, all the text elements inside the body will also have a blue color, unless they have a different color specified by a more specific rule.
- CSS has a concept of cascade, which means that the order of the rules matters when there are multiple rules for the same element. The cascade follows a set of rules to determine which rule has more precedence, such as the origin, importance, specificity, and position of the rule. For example, a rule that is marked as important using the !important keyword has more precedence than a rule that is not marked as important, and a rule that comes later in the style sheet has more precedence than a rule that comes earlier, if they have the same specificity and origin.