# Introduction for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS allows web developers to separate the presentation of a web page from its content. This makes it easier to maintain, update and reuse the style of a web page.
- CSS can control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the appearance of a web page.
- CSS can also create animations, transitions, transformations, and other effects on web elements.
- CSS can be applied to a web page in three ways: inline, internal, and external.
  - Inline CSS is written inside the HTML element using the `style` attribute. It affects only that element and has the highest priority.
  - Internal CSS is written inside the `<style>` tag in the `<head>` section of the HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the `.css` extension and linked to the HTML document using the `<link>` tag in the `<head>` section. It affects all the elements in the document and any other documents that link to the same file. It has the lowest priority.
- CSS follows a set of rules or syntax to define the style of a web element. A CSS rule consists of a selector and a declaration block. A selector specifies which element or elements to apply the style to. A declaration block contains one or more declarations that define the style properties and values. A declaration consists of a property and a value, separated by a colon and ending with a semicolon. For example:

```css
/* This is a CSS comment */
p { /* This is a selector for all <p> elements */
  color: blue; /* This is a declaration that sets the text color to blue */
  font-size: 16px; /* This is another declaration that sets the font size to 16 pixels */
} /* This is the end of the declaration block */
```

- CSS can use various units to specify the values of the style properties. Some of the common units are:
  - Pixels (px): A pixel is a dot on the screen. It is an absolute unit that does not depend on the screen resolution or size. One pixel is equal to 1/96 of an inch.
  - Percentages (%): A percentage is a relative unit that depends on the parent element or the viewport. For example, `width: 50%` means half of the parent element's width or half of the viewport's width.
  - Em (em): An em is a relative unit that depends on the font size of the current element. One em is equal to the current font size. For example, if the font size is 16px, then 1em is equal to 16px and 2em is equal to 32px.
  - Rem (rem): A rem is a relative unit that depends on the font size of the root element, which is usually the `<html>` element. One rem is equal to the root font size. For example, if the root font size is 16px, then 1rem is equal to 16px and 2rem is equal to 32px.
  - Viewport units (vw, vh, vmin, vmax): Viewport units are relative units that depend on the size of the viewport, which is the visible area of the browser window. One vw is equal to 1% of the viewport's width. One vh is equal to 1% of the viewport's height. One vmin is equal to the smaller of vw or vh. One vmax is equal to the larger of vw or vh. For example, if the viewport's width is 800px and height is 600px, then 1vw is equal to 8px, 1vh is equal to 6px, 1vmin is equal to 6px, and 1vmax is equal to 8px.