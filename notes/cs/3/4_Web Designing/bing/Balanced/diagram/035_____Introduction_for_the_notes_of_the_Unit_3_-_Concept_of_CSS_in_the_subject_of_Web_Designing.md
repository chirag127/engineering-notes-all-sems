### Introduction for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS allows web developers to separate the presentation of a web page from its content and structure. This makes it easier to maintain, update and reuse the web design.
- CSS can control various aspects of the web page appearance, such as fonts, colors, backgrounds, borders, margins, padding, alignment, layout, etc.
- CSS can also create dynamic effects, such as transitions, animations, transformations, filters, etc.
- CSS can be applied to HTML elements in three ways: inline, internal and external.
  - Inline CSS is written inside the style attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the style element in the head section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the .css extension and linked to the HTML document using the link element in the head section. It affects all the elements in the linked documents and has the lowest priority.
- CSS follows a set of rules or syntax to define the style of an HTML element. A CSS rule consists of a selector and a declaration block. A selector specifies which element or elements to apply the style to. A declaration block contains one or more declarations, each consisting of a property and a value, separated by a colon and enclosed in curly braces.
  - For example, the following CSS rule applies a red color and a 24px font size to all the h1 elements in the web page:

  ```css
  h1 {
    color: red;
    font-size: 24px;
  }
  ```
- CSS supports various types of selectors, such as element selectors, class selectors, id selectors, attribute selectors, pseudo-class selectors, pseudo-element selectors, etc. Selectors can be combined using combinators, such as descendant, child, adjacent sibling, general sibling, etc. Selectors can also be grouped using commas to apply the same style to multiple elements.
  - For example, the following CSS rule applies a blue color and an underline to all the links that have the class "active" or are visited by the user:

  ```css
  a.active, a:visited {
    color: blue;
    text-decoration: underline;
  }
  ```
- CSS supports various units of measurement, such as pixels, percentages, ems, rems, vh, vw, etc. Units can be used to specify the values of various properties, such as width, height, margin, padding, font-size, etc.
  - For example, the following CSS rule sets the width of the div element to 50% of the parent element's width and the height to 10% of the viewport's height:

  ```css
  div {
    width: 50%;
    height: 10vh;
  }
  ```
- CSS supports various values, such as keywords, colors, lengths, numbers, angles, etc. Values can be used to specify the values of various properties, such as color, background, border, transform, filter, etc.
  - For example, the following CSS rule rotates the img element by 45 degrees and applies a grayscale filter to it:

  ```css
  img {
    transform: rotate(45deg);
    filter: grayscale(100%);
  }
  ```
- CSS supports various properties, such as color, font-family, display, position, flex, grid, etc. Properties can be used to specify the style of various aspects of an HTML element, such as text, layout, box model, etc.
  - For example, the following CSS rule sets the display of the ul element to flex and aligns its items to the center:

  ```css
  ul {
    display: flex;
    align-items: center;
  }
  ```
- CSS supports various at-rules, such as @import, @media, @keyframes, etc. At-rules can be used to import other style sheets, apply conditional styles, define animations, etc.
  - For example, the following CSS rule imports another style sheet called "style.css" and applies it only when the screen width is less than 600px:

  ```css
  @import url("style.css") screen and (max-width: 600px);
  ```