# CSS Color

- The color property in CSS is used to set the color of HTML elements, such as text, background, and borders  .
- The color property accepts a <color> value, which can be defined in various ways, such as keywords, hexadecimal values, RGB values, HSL values, etc .
- The color property also sets the currentcolor value, which can be used as an indirect value on other properties that accept a <color> value, such as border-color, outline-color, etc.
- The color property is inherited by default, which means that the child elements will inherit the color value from their parent element, unless specified otherwise .
- The color property can be used with the :visited and :link pseudo-classes to style the color of visited and unvisited links, respectively .
- The color property can be used with the opacity property to create transparent colors.

Some examples of using the color property are:

```css
/* Using a keyword */
p {
  color: blue;
}

/* Using a hexadecimal value */
h1 {
  color: #FF0000;
}

/* Using an RGB value */
div {
  color: rgb(0, 255, 0);
}

/* Using an HSL value */
span {
  color: hsl(120, 100%, 50%);
}

/* Using the currentcolor value */
a {
  color: purple;
  border: 2px solid currentcolor;
}

/* Using the opacity property */
div {
  color: rgba(255, 255, 0, 0.5);
  opacity: 0.8;
}
```