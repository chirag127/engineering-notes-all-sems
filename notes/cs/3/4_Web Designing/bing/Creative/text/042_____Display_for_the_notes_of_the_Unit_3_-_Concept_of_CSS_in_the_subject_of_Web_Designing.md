### Display for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for **Cascading Style Sheets** and it is a **stylesheet language** used to describe the **presentation** of a document written in HTML or XML.
- CSS allows you to **style and layout** web pages by altering the **font, color, size, and spacing** of your content, splitting it into **multiple columns**, or adding **animations and other decorative features** .
- CSS is a **rule-based language** that defines the rules by specifying **groups of styles** that should be applied to particular elements or groups of elements on your web page.
- For example, you can decide to have the main heading on your page to be shown as large red text by using a CSS rule like this:

```css
h1 {
  color: red;
  font-size: 36px;
}
```

- CSS rules consist of two parts: a **selector** and a **declaration block**.
- The selector is the HTML element that you want to style, such as `h1` in the example above.
- The declaration block is the part between the curly braces `{ }` that contains one or more **declarations** separated by semicolons `;`.
- Each declaration consists of a **property** and a **value**, separated by a colon `:`.
- The property is the aspect of the element that you want to change, such as `color` or `font-size`.
- The value is the specific value that you want to apply to the property, such as `red` or `36px`.
- CSS rules can be written in three different ways: **inline**, **internal**, or **external**.
- Inline CSS is when you use the `style` attribute inside an HTML element to apply a specific style to that element only, such as `<h1 style="color: red; font-size: 36px;">Hello</h1>`.
- Internal CSS is when you use the `<style>` element inside the `<head>` section of an HTML document to apply styles to the whole document or a part of it, such as:

```html
<head>
  <style>
    h1 {
      color: red;
      font-size: 36px;
    }
  </style>
</head>
```

- External CSS is when you use the `<link>` element inside the `<head>` section of an HTML document to link to an external CSS file that contains the styles for the document, such as:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

- External CSS is the most recommended way of using CSS as it allows you to **separate the content from the presentation**, **reuse the same styles across multiple pages**, and **maintain and update the styles more easily**.