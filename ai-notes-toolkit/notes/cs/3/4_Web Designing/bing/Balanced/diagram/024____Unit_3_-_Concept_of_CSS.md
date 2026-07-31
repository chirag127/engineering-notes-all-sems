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
  - Attribute selectors: These match elements by their attributes, such as `[href]`, `[type="text"]`, `[title~="flower"]`, etc. An attribute selector is enclosed in square brackets (`[]`).
  - Pseudo-class selectors: These match elements based on their state or position, such as `:hover`, `:first-child`, `:checked`, etc. A pseudo-class selector is preceded by a colon (`:`).
  - Pseudo-element selectors: These match parts of elements, such as `::before`, `::after`, `::first-line`, etc. A pseudo-element selector is preceded by two colons (`::`).

- CSS specificity: CSS specificity is a measure of how specific a selector is, and how it affects the priority of the rules. The more specific a selector is, the higher its specificity, and the more likely it is to override other rules that apply to the same element. The specificity of a selector is calculated based on the following order of precedence:

  - Inline styles: These are styles that are defined directly in the HTML element using the `style` attribute. They have the highest specificity and override any other rules.
  - ID selectors: These have the second highest specificity and override any other rules except inline styles.
  - Class selectors, attribute selectors, and pseudo-class selectors: These have the same specificity and override any other rules except inline styles and ID selectors.
  - Element selectors and pseudo-element selectors: These have the lowest specificity and are overridden by any other rules.

- CSS inheritance: CSS inheritance is a mechanism that allows some properties to be inherited from the parent element to the child element. For example, if the parent element has a font size of 20 pixels, the child element will also have the same font size, unless it is explicitly defined otherwise. Not all properties are inherited, and some properties can be prevented from inheriting by using the `inherit` or `initial` values.

- CSS cascade: CSS cascade is a process that determines how conflicting rules are resolved. When multiple rules apply to the same element, the cascade follows these steps to decide which rule has the highest priority:

  - Importance: Rules that are marked as `!important` have the highest priority and override any other rules.
  - Origin: Rules that are defined by the user (such as in the browser settings) have a higher priority than rules that are defined by the author (such as in the external or internal style sheets) or by the user agent (such as in the default browser styles).
  - Specificity: Rules that have a higher specificity have a higher priority than rules that have a lower specificity.
  - Order: Rules that are defined later in the source code have a higher priority than rules that are defined earlier.