# Creating Style Sheet for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the appearance of web elements.
- CSS can be applied to web pages in three ways: inline, internal, and external.
  - Inline CSS is written inside the `style` attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the `<style>` tag in the `<head>` section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the `.css` extension and linked to an HTML document using the `<link>` tag in the `<head>` section. It affects all the elements in the linked document and has the lowest priority.
- CSS uses selectors to target specific elements or groups of elements on a web page. Selectors can be based on element names, classes, ids, attributes, pseudo-classes, pseudo-elements, or combinations of these.
- CSS uses properties and values to define the style rules for the selected elements. Properties are the aspects of the appearance that can be modified, such as `color`, `font-size`, `width`, etc. Values are the specific settings for the properties, such as `red`, `16px`, `50%`, etc.
- CSS uses curly braces `{}` to enclose the style rules for each selector. Each property-value pair is written on a separate line and ends with a semicolon `;`. For example:

```css
/* This is a comment in CSS */
h1 {
  color: blue; /* The text color of h1 elements is blue */
  font-family: Arial; /* The font family of h1 elements is Arial */
}
p {
  color: green; /* The text color of p elements is green */
  font-style: italic; /* The font style of p elements is italic */
}
```

- CSS can be used to create various effects and animations on web pages, such as transitions, transforms, filters, keyframes, etc. These features can enhance the user experience and interactivity of web pages.