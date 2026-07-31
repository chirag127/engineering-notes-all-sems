## Unit 3 - Concept of CSS

CSS stands for Cascading Style Sheets. It is a language that is used to describe the presentation of HTML elements, such as their colors, fonts, layouts, and animations. CSS can be applied to HTML elements in different ways, such as:

- Inline styles: These are written directly in the HTML element's `style` attribute, such as `<p style="color: red;">This is a paragraph.</p>`. Inline styles have the highest specificity, meaning they override any other CSS rules that apply to the same element.
- Internal styles: These are written in a `<style>` element inside the HTML document's `<head>` section, such as `<style>p {color: blue;}</style>`. Internal styles apply to the whole HTML document, unless they are overridden by inline styles or external styles.
- External styles: These are written in a separate file with the `.css` extension, such as `style.css`, and linked to the HTML document using a `<link>` element, such as `<link rel="stylesheet" href="style.css">`. External styles can be reused across multiple HTML documents, and they have the lowest specificity, meaning they can be overridden by inline styles or internal styles.

CSS rules consist of two parts: a selector and a declaration block. A selector is a pattern that matches one or more HTML elements, such as `p`, `.class`, `#id`, or `[attribute]`. A declaration block is a set of properties and values that define how the selected elements should look, such as `color: red;`, `font-size: 20px;`, or `display: flex;`. A declaration block is enclosed in curly braces `{}` and each property-value pair is separated by a semicolon `;`. For example, the following CSS rule applies a red color and a 20px font size to all paragraphs in the HTML document:

```css
p {
  color: red;
  font-size: 20px;
}
```

CSS can also use various features to create more complex and dynamic styles, such as:

- Classes and IDs: These are attributes that can be added to HTML elements to identify them uniquely or as part of a group, such as `<p class="intro" id="first-paragraph">This is a paragraph.</p>`. Classes and IDs can be used as selectors in CSS to target specific elements or groups of elements, such as `.intro` or `#first-paragraph`.
- Pseudo-classes and pseudo-elements: These are keywords that can be added to selectors to specify a certain state or part of an element, such as `:hover`, `:first-child`, `::before`, or `::after`. Pseudo-classes and pseudo-elements can be used to create effects such as changing the color of a link when the mouse hovers over it, or adding content before or after an element.
- Combinators and descendant selectors: These are symbols that can be used to combine multiple selectors to create more specific or complex patterns, such as `p + p`, `p > span`, or `div p`. Combinators and descendant selectors can be used to target elements based on their relationship to other elements, such as selecting the first paragraph after another paragraph, or selecting all spans that are direct children of paragraphs, or selecting all paragraphs that are inside a div.
- Media queries: These are expressions that can be used to apply different CSS rules depending on the characteristics of the device or the viewport, such as the width, height, orientation, or resolution. Media queries can be used to create responsive web design, which adapts the layout and appearance of the web page to different screen sizes and devices. For example, the following media query applies a different font size to paragraphs depending on the width of the viewport:

```css
@media (max-width: 600px) {
  p {
    font-size: 16px;
  }
}

@media (min-width: 601px) {
  p {
    font-size: 20px;
  }
}
```

CSS is a powerful and flexible language that can enhance the presentation and interactivity of web pages. By learning the basic concepts and features of CSS, you can create attractive and user-friendly web designs.