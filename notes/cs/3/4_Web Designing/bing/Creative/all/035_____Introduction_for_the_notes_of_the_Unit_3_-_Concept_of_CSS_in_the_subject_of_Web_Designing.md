# Introduction for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS allows web developers to separate the presentation of a web page from its content. This makes it easier to maintain, update and reuse the style of a web page.
- CSS can control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the appearance of a web page.
- CSS can also create animations, transitions, transformations, and other effects on web elements.
- CSS can be applied to a web page in three ways: inline, internal, and external.
  - Inline CSS is written inside the style attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the style element in the head section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the .css extension and linked to an HTML document using the link element in the head section. It affects all the elements in the linked document and has the lowest priority.
- CSS follows a set of rules or syntax to define the style of a web element. A CSS rule consists of a selector and a declaration block. A selector specifies which element or elements to apply the style to. A declaration block contains one or more declarations that define the style properties and values for the selector.
  - For example, the following CSS rule applies a red color and a 24px font size to all the h1 elements in a web page:

  ```css
  h1 {
    color: red;
    font-size: 24px;
  }
  ```

  - In this rule, h1 is the selector and the curly braces {} enclose the declaration block. Inside the declaration block, color and font-size are the properties and red and 24px are the values. Each declaration ends with a semicolon (;).
- CSS supports various types of selectors, such as element selectors, class selectors, id selectors, attribute selectors, pseudo-class selectors, and pseudo-element selectors. These selectors can be combined or nested to create more specific or complex selectors.
  - For example, the following CSS rule applies a blue color and an underline to all the links that have the class name "important" in a web page:

  ```css
  a.important {
    color: blue;
    text-decoration: underline;
  }
  ```

  - In this rule, a.important is a combined selector that matches all the a elements that have the class attribute value "important". The dot (.) is used to connect the element selector and the class selector.
- CSS also supports various units to specify the values of the style properties, such as pixels (px), percentages (%), ems (em), rems (rem), points (pt), and viewport units (vw, vh, vmin, vmax). These units can be relative or absolute depending on how they are calculated.
  - For example, the following CSS rule applies a 50% width and a 10px margin to a div element in a web page:

  ```css
  div {
    width: 50%;
    margin: 10px;
  }
  ```

  - In this rule, 50% is a relative unit that means half of the parent element's width, while 10px is an absolute unit that means 10 pixels.