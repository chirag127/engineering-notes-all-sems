## Unit 3 - Concept of CSS

CSS stands for Cascading Style Sheets. It is a language that is used to style and format the appearance of HTML documents. CSS can control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of web pages.

Some of the main concepts of CSS are:

- CSS rules: A CSS rule consists of a selector and a declaration block. The selector specifies which HTML elements the rule applies to, and the declaration block contains one or more declarations that define how the elements should be styled. For example:

```css
p {
  color: blue;
  font-size: 16px;
}
```

This rule applies to all `<p>` elements and sets their text color to blue and their font size to 16 pixels.

- CSS properties and values: A CSS declaration consists of a property and a value, separated by a colon and followed by a semicolon. The property specifies what aspect of the element's style is being defined, and the value specifies how it should be defined. For example:

```css
color: blue;
```

This declaration sets the color property to the value blue.

- CSS selectors: A CSS selector is a pattern that matches one or more HTML elements. There are different types of selectors, such as:

  - Element selectors: These match elements by their tag name, such as `p`, `h1`, `div`, etc.
  - Class selectors: These match elements by their class attribute, such as `.red`, `.big`, `.container`, etc. A class selector is preceded by a dot (`.`).
  - ID selectors: These match elements by their id attribute, such as `#header`, `#main`, `#footer`, etc. An id selector is preceded by a hash (`#`).
  - Attribute selectors: These match elements by their attributes, such as `[href]`, `[type="text"]`, `[title~="example"]`, etc. An attribute selector is enclosed in square brackets (`[]`).
  - Pseudo-class selectors: These match elements based on their state or position, such as `:hover`, `:first-child`, `:nth-of-type(2n)`, etc. A pseudo-class selector is preceded by a colon (`:`).
  - Pseudo-element selectors: These match parts of elements, such as `::before`, `::after`, `::first-line`, `::first-letter`, etc. A pseudo-element selector is preceded by two colons (`::`).
  - Combinators: These combine two or more selectors to create more specific or complex selectors, such as `p + p`, `div > span`, `ul li`, `h1 ~ h2`, etc. Combinators are symbols that indicate the relationship between the selectors, such as `+` (adjacent sibling), `>` (child), ` ` (descendant), `~` (general sibling), etc.

- CSS specificity: CSS specificity is a measure of how specific a selector is, and how it affects the priority of the rules. The more specific a selector is, the higher its specificity, and the more likely it is to override other rules that apply to the same element. The specificity of a selector is calculated based on the following rules:

  - Each type of selector has a different weight or value, such as 1, 10, 100, or 1000.
  - Element selectors have a value of 1, class selectors have a value of 10, id selectors have a value of 100, and inline styles have a value of 1000.
  - Pseudo-class selectors have the same value as class selectors, and pseudo-element selectors have the same value as element selectors.
  - Attribute selectors have the same value as class selectors, except for the `[id]` attribute selector, which has the same value as the id selector.
  - The universal selector (`*`) and combinators (`+`, `>`, ` `, `~`) have no value and do not affect the specificity.
  - The specificity of a selector is the sum of the values of its components. For example, the selector `div#main p.red::first-letter` has a specificity of 112 (100 + 1 + 10 + 1).
  - If two selectors have the same specificity, the one that comes later in the style sheet or the HTML document wins.
  - The `!important` keyword can be added to a declaration to make it override any other declaration, regardless of specificity. However, this should be used sparingly and only as a last resort, as it can cause conflicts and maintenance issues.

- CSS inheritance: CSS inheritance is the mechanism by which some CSS properties are passed from parent