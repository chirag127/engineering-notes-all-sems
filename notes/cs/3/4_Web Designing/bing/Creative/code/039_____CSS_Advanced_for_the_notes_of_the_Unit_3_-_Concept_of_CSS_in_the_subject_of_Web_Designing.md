Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on the topic of CSS Advanced for Unit 3 - Concept of CSS.

### CSS Advanced

- CSS stands for Cascading Style Sheets, which is a language that defines how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of web content.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the `style` attribute of an HTML element, and affects only that element.
  - Internal CSS is written inside the `<style>` tag in the `<head>` section of an HTML document, and affects all the elements in that document.
  - External CSS is written in a separate file with the `.css` extension, and is linked to an HTML document using the `<link>` tag in the `<head>` section. External CSS can affect multiple HTML documents that share the same style sheet.
- CSS follows a set of rules or syntax to specify the style properties and values for each HTML element. The basic syntax of CSS is:

  ```css
  selector {
    property: value;
  }
  ```

  - A selector is a pattern that matches one or more HTML elements, such as a tag name, an id, a class, or a combination of them.
  - A property is a style attribute that can be applied to an HTML element, such as `color`, `font-size`, `width`, or `border`.
  - A value is a specific setting for a property, such as `red`, `16px`, `50%`, or `solid`.
  - A semicolon (;) is used to separate multiple property-value pairs within a selector.
  - A curly brace ({}) is used to enclose the property-value pairs for a selector.

- CSS can use various units to specify the values for length, width, height, font-size, margin, padding, border, and other properties. Some of the common units are:
  - Pixels (px): A pixel is a dot on the screen, and is the most commonly used unit for web design. One pixel is equal to 1/96th of an inch.
  - Percentages (%): A percentage is a relative unit that is based on the size of the parent element or the viewport (the visible area of the browser window). For example, `width: 50%` means half of the parent element's width, and `font-size: 150%` means 1.5 times the parent element's font size.
  - Em (em): An em is a relative unit that is based on the font size of the current element. For example, `font-size: 2em` means twice the current element's font size, and `margin: 1em` means a margin equal to the current element's font size.
  - Rem (rem): A rem is a relative unit that is based on the font size of the root element, which is usually the `<html>` element. For example, `font-size: 2rem` means twice the root element's font size, and `margin: 1rem` means a margin equal to the root element's font size.
  - Viewport units (vw, vh, vmin, vmax): Viewport units are relative units that are based on the dimensions of the viewport. For example, `width: 50vw` means half of the viewport's width, and `height: 100vh` means the full height of the viewport. Vmin and vmax are the smaller and larger of the viewport's width and height, respectively.

- CSS can use various selectors to target specific HTML elements based on their attributes, relationships, states, or pseudo-elements. Some of the common selectors are:
  - Element selector: An element selector matches all the HTML elements with the same tag name, such as `p`, `h1`, or `div`.
  - Id selector: An id selector matches the HTML element with a specific id attribute, which is unique within a document. An id selector is written with a hash (#) symbol followed by the id value, such as `#header`, `#main`, or `#footer`.
  - Class selector: A class selector matches the HTML elements with a specific class attribute, which can be shared by multiple elements within a document. A class selector is written with a dot (.) symbol followed by the class value, such as `.red`, `.large`, or `.center`.
  - Attribute selector: An attribute selector matches the HTML elements with a specific attribute or attribute value,