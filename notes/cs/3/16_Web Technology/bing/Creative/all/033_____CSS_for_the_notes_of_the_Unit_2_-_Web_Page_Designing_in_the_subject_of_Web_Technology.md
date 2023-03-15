# CSS

CSS stands for Cascading Style Sheets. It is a language that is used to style and layout web pages. CSS can control the appearance of HTML elements, such as fonts, colors, backgrounds, borders, margins, padding, etc. CSS can also create effects, such as transitions, animations, transformations, and filters. CSS can also adapt the web page to different screen sizes and devices, using media queries and responsive design.

## CSS Syntax

A CSS rule consists of a selector and a declaration block. A selector is a way of selecting an HTML element or a group of elements that you want to style. A declaration block is a set of declarations enclosed by curly braces. A declaration is a property and a value, separated by a colon. A property is a CSS attribute that you want to change, such as color, font-size, or width. A value is the specific setting for the property, such as red, 16px, or 50%. A semicolon is used to separate declarations.

For example, the following CSS rule selects all the paragraphs (`<p>`) in the HTML document and sets their text color to red and their font size to 16 pixels:

```css
p {
  color: red;
  font-size: 16px;
}
```

## CSS How To

There are three ways of adding CSS to an HTML document:

- Inline style: You can use the `style` attribute inside an HTML element to apply CSS directly to that element. For example:

```html
<p style="color: blue; font-weight: bold;">This is a paragraph with inline style.</p>
```

- Internal style sheet: You can use the `<style>` element inside the `<head>` section of the HTML document to define CSS rules for the whole document. For example:

```html
<head>
  <style>
    h1 {
      color: green;
      text-align: center;
    }

    p {
      color: purple;
      font-family: Arial;
    }
  </style>
</head>
```

- External style sheet: You can use the `<link>` element inside the `<head>` section of the HTML document to link to an external CSS file. The CSS file should have the `.css` extension and should contain the CSS rules. For example:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

The external style sheet can be used by multiple HTML pages, which makes it easier to maintain and update the style of the website.

## CSS Selectors

CSS selectors are used to select the HTML elements that you want to style. There are different types of selectors, such as:

- Element selector: Selects all the elements of a specific type. For example, `p` selects all the paragraphs, `h1` selects all the headings of level 1, `div` selects all the division elements, etc.

- Class selector: Selects all the elements that have a specific class attribute. The class selector is preceded by a dot (`.`). For example, `.red` selects all the elements that have `class="red"`, `.big` selects all the elements that have `class="big"`, etc. You can also combine multiple classes, such as `.red.big` to select the elements that have both `class="red"` and `class="big"`.

- ID selector: Selects a single element that has a specific id attribute. The id selector is preceded by a hash (`#`). For example, `#intro` selects the element that has `id="intro"`, `#logo` selects the element that has `id="logo"`, etc. The id attribute should be unique in the HTML document.

- Attribute selector: Selects all the elements that have a specific attribute or a specific attribute value. The attribute selector is enclosed by square brackets (`[]`). For example, `[href]` selects all the elements that have the `href` attribute, `[src="logo.png"]` selects all the elements that have the `src` attribute with the value of `logo.png`, etc.

- Pseudo-class selector: Selects all the elements that are in a specific state or condition. The pseudo-class selector is preceded by a colon (`:`). For example, `:hover` selects all the elements that are being hovered over by the mouse pointer, `:checked` selects all the elements that are checked (such as checkboxes or radio buttons), `:first-child` selects all the elements that are the first child of their parent, etc.

- Pseudo-element selector: Selects a specific part of an