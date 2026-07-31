Hello, I am Sydney, your AI assistant. I can help you with your notes on CSS for the Unit 2 - Web Page Designing in the subject of Web Technology. Here is the content I have generated for you:

# CSS

CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page. CSS can control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of HTML elements.

## CSS Syntax

A CSS rule-set consists of a selector and a declaration block:

```css
selector {
  property: value;
  property: value;
}
```

- The selector specifies which HTML element(s) to style.
- The declaration block contains one or more declarations separated by semicolons.
- Each declaration consists of a property and a value, separated by a colon.
- The property is the name of the CSS attribute to modify, such as color, font-size, or width.
- The value is the value to assign to the property, such as red, 16px, or 50%.

## CSS Selectors

CSS selectors are used to select the HTML elements that you want to style. There are different types of selectors, such as:

- Element selector: selects all elements of a specific type, such as `p` or `h1`.
- Class selector: selects all elements that have a specific class attribute, such as `.intro` or `.highlight`. The class selector is preceded by a dot (`.`).
- ID selector: selects a single element that has a specific id attribute, such as `#logo` or `#footer`. The id selector is preceded by a hash (`#`).
- Attribute selector: selects all elements that have a specific attribute or attribute value, such as `[href]` or `[src="logo.png"]`.
- Pseudo-class selector: selects elements based on their state or position, such as `:hover` or `:first-child`.
- Pseudo-element selector: selects a part of an element, such as `::before` or `::after`.
- Combinator selector: combines two or more selectors to create a more specific selector, such as `p.intro` or `div > p`.
- Universal selector: selects all elements on a page, denoted by an asterisk (`*`).

## CSS How To

There are three ways to insert CSS into an HTML document:

- Inline style: use the `style` attribute inside an HTML element to apply CSS to that element only, such as `<p style="color: red;">This is a paragraph.</p>`.
- Internal style sheet: use the `<style>` element inside the `<head>` section of an HTML document to apply CSS to the whole document, such as:

```html
<head>
  <style>
    p {
      color: blue;
    }
  </style>
</head>
```

- External style sheet: use the `<link>` element inside the `<head>` section of an HTML document to link to an external CSS file, such as:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

The external CSS file should have the `.css` extension and contain only CSS rules.

## CSS Box Model

The CSS box model is a concept that describes how every HTML element is represented as a rectangular box, with the following properties:

- Content: the text, images, or other content inside the element.
- Padding: the space between the content and the border of the element.
- Border: the line that surrounds the element.
- Margin: the space between the border of the element and the adjacent elements.

The total width and height of an element are calculated by adding the content, padding, border, and margin values. For example, if an element has a content width of 100px, a padding of 10px, a border of 5px, and a margin of 20px, the total width of the element is 170px (100 + 2*10 + 2*5 + 2*20).

The CSS properties that control the box model are:

- `width` and `height`: set the width and height of the content area of the element.
- `padding`: set the width of the padding area of the element. You can use `padding-top`, `padding-right`, `padding-bottom`, and `padding-left` to set the padding for each side individually, or use the shorthand `padding` property to set all four sides at once, such as `padding: 10px 20px 30px 40px;`.
- `border`: set the width, style, and color of the border of the element. You can use `