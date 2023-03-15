### Border properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- The border properties in CSS are used to style the borders of an element, such as its width, color, style, and radius.
- The border properties can be applied to any element that can have a border, such as `<div>`, `<p>`, `<table>`, `<img>`, etc.
- The border properties can be specified for each side of an element (top, right, bottom, left) or for all sides at once using the shorthand property `border`.
- The border properties are:

  - `border-width`: Specifies the width of the border, either in pixels (px), ems (em), percentages (%), or predefined values (thin, medium, thick).
  - `border-color`: Specifies the color of the border, either in hexadecimal values (#RRGGBB), RGB values (rgb(r, g, b)), RGBA values (rgba(r, g, b, a)), HSL values (hsl(h, s, l)), HSLA values (hsla(h, s, l, a)), or predefined color names (red, blue, green, etc.).
  - `border-style`: Specifies the style of the border, either in predefined values (none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset) or custom values using images (url(image)).
  - `border-radius`: Specifies the radius of the corners of the border, either in pixels (px), ems (em), percentages (%), or predefined values (0, 50%, 100%). The radius can be specified for each corner (top-left, top-right, bottom-left, bottom-right) or for all corners at once using the shorthand property `border-radius`.

- Some examples of using the border properties are:

  - To create a solid red border of 5 pixels around a paragraph, use:

    ```css
    p {
      border-width: 5px;
      border-color: red;
      border-style: solid;
    }
    ```

  - To create a dashed blue border of 3 ems on the right side of a div, use:

    ```css
    div {
      border-right-width: 3em;
      border-right-color: blue;
      border-right-style: dashed;
    }
    ```

  - To create a rounded border of 50% radius with a gradient color, use:

    ```css
    div {
      border-width: 10px;
      border-style: solid;
      border-radius: 50%;
      border-image: linear-gradient(to right, yellow, green, blue);
    }
    ```