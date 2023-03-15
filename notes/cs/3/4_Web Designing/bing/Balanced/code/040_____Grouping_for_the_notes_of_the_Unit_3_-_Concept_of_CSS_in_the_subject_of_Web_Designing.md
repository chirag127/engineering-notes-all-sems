### Grouping for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that defines how HTML elements are displayed on a web page.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the `style` attribute of an HTML element. It affects only that element.
  - Internal CSS is written inside the `<style>` tag in the `<head>` section of an HTML document. It affects all the elements in that document.
  - External CSS is written in a separate file with the `.css` extension and linked to an HTML document using the `<link>` tag. It affects all the elements in that document and any other documents that link to it.
- CSS uses selectors to target HTML elements and apply styles to them. There are different types of selectors, such as element, class, id, attribute, pseudo-class, and pseudo-element selectors.
  - Element selectors match HTML elements by their tag name, such as `p`, `h1`, `div`, etc.
  - Class selectors match HTML elements by their class attribute, such as `.red`, `.big`, `.center`, etc. Multiple elements can have the same class.
  - Id selectors match HTML elements by their id attribute, such as `#logo`, `#header`, `#footer`, etc. Each element can have only one id, and each id can be used only once in a document.
  - Attribute selectors match HTML elements by their attributes, such as `[href]`, `[type="text"]`, `[alt="image"]`, etc.
  - Pseudo-class selectors match HTML elements based on their state, such as `:hover`, `:visited`, `:checked`, etc.
  - Pseudo-element selectors match parts of HTML elements, such as `::before`, `::after`, `::first-line`, `::first-letter`, etc.
- CSS uses properties and values to define the styles for HTML elements. There are many properties, such as `color`, `font-size`, `margin`, `padding`, `border`, `background`, `display`, `position`, etc. Each property has a set of possible values, such as `red`, `20px`, `auto`, `solid`, `none`, `block`, `absolute`, etc.
- CSS uses rules to group selectors and properties. A rule consists of a selector and a declaration block. A declaration block contains one or more declarations, each consisting of a property and a value, separated by a colon and ending with a semicolon. For example:

```css
/* This is a CSS rule */
p {
  /* This is a declaration block */
  color: blue; /* This is a declaration */
  font-size: 16px; /* This is another declaration */
}
```

- CSS follows a cascading order to determine which styles are applied to an HTML element. The order is based on three factors: specificity, inheritance, and source order.
  - Specificity is a measure of how specific a selector is. A more specific selector has a higher priority than a less specific one. The specificity of a selector is calculated based on the number of id, class, attribute, and element components it has. For example, `#logo` has a higher specificity than `.red`, which has a higher specificity than `p`.
  - Inheritance is a mechanism that allows some properties to be passed from parent elements to child elements. For example, if a `<div>` element has a `color` property, its child elements will inherit the same color, unless they have their own `color` property.
  - Source order is the order in which the CSS rules are written or loaded. If two selectors have the same specificity and affect the same element, the one that comes later in the source order will override the one that comes earlier. For example, if there are two rules for `p` elements, the second one will take precedence over the first one.

```css
/* This rule comes first */
p {
  color: blue;
}

/* This rule comes second */
p {
  color: red;
}
```

- CSS can be used to create various layouts and effects for web pages, such as grids, flexbox, columns, transitions, animations, transforms, filters, etc. These topics are covered in more detail in the following units.