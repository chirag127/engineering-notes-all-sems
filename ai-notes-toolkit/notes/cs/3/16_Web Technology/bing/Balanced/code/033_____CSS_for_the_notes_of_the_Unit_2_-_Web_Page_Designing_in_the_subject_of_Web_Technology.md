# CSS

CSS stands for Cascading Style Sheets. It is a language that is used to style and layout web pages. CSS can control the appearance of HTML elements, such as fonts, colors, backgrounds, borders, margins, padding, etc. CSS can also create effects, such as transitions, animations, transformations, and filters. CSS can be applied to web pages in different ways, such as inline, internal, external, or imported.

## CSS Syntax

A CSS rule consists of a selector and a declaration block. A selector is used to select the HTML elements that you want to style. A declaration block contains one or more declarations, which are separated by semicolons. A declaration consists of a property and a value, which are separated by a colon. For example:

```css
p {
  color: red;
  font-size: 20px;
}
```

This rule selects all `<p>` elements and sets their color to red and their font size to 20 pixels.

## CSS Selectors

CSS selectors are used to target specific HTML elements or groups of elements. There are different types of selectors, such as:

- Element selectors: select elements by their tag name, such as `p`, `h1`, `div`, etc.
- Class selectors: select elements by their class attribute, which can be shared by multiple elements. Class selectors start with a dot, such as `.example`.
- ID selectors: select elements by their id attribute, which must be unique in a document. ID selectors start with a hash, such as `#example`.
- Attribute selectors: select elements by their attributes or attribute values, such as `[href]`, `[type="text"]`, `[title~="example"]`, etc.
- Pseudo-class selectors: select elements based on their state or position, such as `:hover`, `:first-child`, `:nth-of-type(2n)`, etc.
- Pseudo-element selectors: select parts of elements, such as `::before`, `::after`, `::first-line`, `::first-letter`, etc.
- Combinators: combine two or more selectors to create more specific selections, such as `p + p`, `div > p`, `ul li`, `p.example`, etc.

## CSS Specificity

CSS specificity is a measure of how specific a selector is. The more specific a selector is, the higher its priority in applying the style to the matched elements. The specificity of a selector is calculated based on the following rules:

- Each type of selector has a different weight: ID selectors have the highest weight, followed by class, attribute, and pseudo-class selectors, followed by element and pseudo-element selectors.
- The specificity of a selector is the sum of the weights of its components. For example, `#example` has a specificity of 100, `.example` has a specificity of 10, and `p` has a specificity of 1.
- If two selectors have the same specificity, the one that comes later in the style sheet wins.
- Inline styles have the highest specificity, followed by external and internal style sheets.
- The `!important` keyword can override any specificity, except for another `!important` rule with a higher specificity.

## CSS Inheritance

CSS inheritance is a mechanism that allows some properties to be passed from parent elements to their children. For example, if you set the color property of the `<body>` element, all the text elements inside the body will inherit the same color, unless you specify a different color for them. Inheritance can help you avoid repeating the same style declarations for multiple elements. However, not all properties are inherited by default. You can use the `inherit` value to force a property to inherit from its parent, or the `initial` value to reset a property to its default value.