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
  - Class selectors: These match elements by their class attribute, which can be used to assign a common style to a group of elements. Class selectors start with a dot, followed by the class name, such as `.red`, `.large`, `.container`, etc.
  - ID selectors: These match elements by their id attribute, which is used to identify a unique element on the page. ID selectors start with a hash sign, followed by the id name, such as `#logo`, `#header`, `#footer`, etc.
  - Attribute selectors: These match elements by their attributes or attribute values, such as `[href]`, `[src="logo.png"]`, `[type="checkbox"]`, etc.
  - Pseudo-class selectors: These match elements based on their state or position, such as `:hover`, `:focus`, `:first-child`, `:nth-child(2n)`, etc.
  - Pseudo-element selectors: These match parts of elements, such as `::before`, `::after`, `::first-line`, `::first-letter`, etc.
  - Combinators: These combine two or more selectors to create more specific selectors, such as `p + p`, `div > p`, `ul li`, `h1 ~ p`, etc.

- CSS specificity: This is a measure of how specific a selector is, and determines which rule takes precedence when multiple rules apply to the same element. The specificity of a selector is calculated based on the number of different types of selectors it contains, such as:

  - Inline styles: These are styles that are defined directly in the HTML element using the style attribute, such as `<p style="color: red;">`. These have the highest specificity and override any other rules.
  - ID selectors: These have the second highest specificity and override any other rules except inline styles.
  - Class selectors, attribute selectors, and pseudo-class selectors: These have the same specificity and override any other rules except inline styles and ID selectors.
  - Element selectors and pseudo-element selectors: These have the lowest specificity and are overridden by any other rules.

  The specificity of a selector is expressed as a four-digit number, where each digit represents the number of selectors of each type. For example:

  - `p` has a specificity of 0,0,0,1
  - `.red` has a specificity of 0,0,1,0
  - `#logo` has a specificity of 0,1,0,0
  - `p.red` has a specificity of 0,0,1,1
  - `p#logo` has a specificity of 0,1,0,1
  - `p.red#logo` has a specificity of 0,1,1,1

  The higher the specificity, the more priority the rule has. If two selectors have the same specificity, the one that comes later in the code wins.

- CSS inheritance: This is a mechanism that allows some CSS properties to be passed from parent elements to child elements, such as `color`, `font-family`, `font-size`, etc. This helps to maintain a consistent style throughout the document and avoid repetition. However, not all properties are inherited, such as `background`, `border`, `margin`, `padding`, etc