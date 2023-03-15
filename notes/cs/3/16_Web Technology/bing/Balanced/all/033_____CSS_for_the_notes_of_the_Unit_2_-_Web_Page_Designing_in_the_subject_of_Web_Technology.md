# CSS

CSS stands for Cascading Style Sheets. It is a language that is used to style and layout web pages. CSS can control the appearance of HTML elements, such as fonts, colors, backgrounds, borders, margins, padding, etc. CSS can also create effects, such as transitions, animations, transformations, and filters.

## CSS Syntax

A CSS rule consists of a selector and a declaration block. A selector is a way of selecting an HTML element or a group of elements. A declaration block is a set of declarations that define the style of the selected element(s). A declaration is a pair of a property and a value, separated by a colon and enclosed in curly braces.

For example, the following CSS rule selects all paragraphs (`<p>` elements) and sets their font size to 20 pixels and their color to red:

```css
p {
  font-size: 20px;
  color: red;
}
```

## CSS Selectors

There are many types of selectors in CSS, such as:

- Element selectors: select elements by their tag name, e.g. `p`, `h1`, `div`, etc.
- Class selectors: select elements by their class attribute, e.g. `.container`, `.button`, `.error`, etc. A class can be applied to multiple elements and an element can have multiple classes.
- ID selectors: select elements by their id attribute, e.g. `#header`, `#logo`, `#footer`, etc. An id must be unique in a document and an element can have only one id.
- Attribute selectors: select elements by their attributes or attribute values, e.g. `[href]`, `[type="text"]`, `[title~="flower"]`, etc.
- Pseudo-class selectors: select elements based on their state or position, e.g. `:hover`, `:focus`, `:first-child`, `:nth-of-type(2n)`, etc.
- Pseudo-element selectors: select parts of elements, such as the first letter, the first line, or the content before or after the element, e.g. `::first-letter`, `::first-line`, `::before`, `::after`, etc.
- Combinators: combine two or more selectors to create more specific selections, e.g. `p + p`, `div > p`, `ul li`, `h1 ~ p`, etc.

## CSS Specificity

Specificity is a way of determining which CSS rule has more priority over another when there is a conflict. Specificity is calculated based on the type and number of selectors in a rule. The following order of precedence is used:

- Inline styles: styles that are applied directly to an element using the `style` attribute have the highest specificity.
- ID selectors: selectors that use the id attribute have the second highest specificity.
- Class, attribute, and pseudo-class selectors: selectors that use the class, attribute, or pseudo-class have the third highest specificity.
- Element and pseudo-element selectors: selectors that use the tag name or pseudo-element have the lowest specificity.
- Universal selector (`*`), combinators (`+`, `>`, `~`, ` `), and negation pseudo-class (`:not()`) have no effect on specificity.

If two rules have the same specificity, the one that comes later in the source code wins. If the rules are in different style sheets, the one that is imported last wins. The only way to override a rule with higher specificity is to use the `!important` keyword, which should be used sparingly and only as a last resort.

## CSS Inheritance

Inheritance is a way of passing down style properties from parent elements to child elements. Some properties, such as `color`, `font-family`, and `text-align`, are inherited by default, while others, such as `width`, `height`, and `border`, are not. To make a property inheritable, you can use the `inherit` value, which means the property will take the same value as its parent element. To prevent a property from being inherited, you can use the `initial` value, which means the property will take its default value.

## CSS Box Model

The box model is a way of describing how an element is sized and positioned on a web page. Every element is represented as a rectangular box, which has four parts:

- Content: the actual content of the element, such as text, images, etc.
- Padding: the space between the content and the border of the element.
- Border: the line that surrounds the padding and the content of the element.
- Margin: the space