# Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text content.
- CSS provides several properties to control the fonts of an element, such as `font-family`, `font-size`, `font-style`, `font-weight`, `font-variant`, and `font`.
- The `font-family` property specifies the name of the font to use for an element. It can take one or more comma-separated values, which are either generic names (such as `serif`, `sans-serif`, `monospace`, etc.) or specific font names (such as `Arial`, `Times New Roman`, `Courier New`, etc.).
- The `font-size` property specifies the size of the font to use for an element. It can take either an absolute value (such as `12px`, `16pt`, `1cm`, etc.) or a relative value (such as `small`, `medium`, `large`, `x-large`, etc.).
- The `font-style` property specifies the style of the font to use for an element. It can take one of the following values: `normal`, `italic`, or `oblique`.
- The `font-weight` property specifies the weight or boldness of the font to use for an element. It can take one of the following values: `normal`, `bold`, `bolder`, `lighter`, or a numeric value from 100 to 900.
- The `font-variant` property specifies the variant of the font to use for an element. It can take one of the following values: `normal` or `small-caps`.
- The `font` property is a shorthand property that combines the `font-family`, `font-size`, `font-style`, `font-weight`, and `font-variant` properties in one declaration. The order of the values is as follows: `font-style font-variant font-weight font-size/line-height font-family`. The `line-height` property specifies the height of a line of text, and is optional. The `font-family` property is mandatory, while the others are optional. If any of the optional properties are omitted, the default values are used.

- Here are some examples of using the font properties in CSS:

```css
/* Using the font-family property */
p {
  font-family: Arial, Helvetica, sans-serif;
}

/* Using the font-size property */
h1 {
  font-size: 36px;
}

/* Using the font-style property */
em {
  font-style: italic;
}

/* Using the font-weight property */
strong {
  font-weight: bold;
}

/* Using the font-variant property */
span {
  font-variant: small-caps;
}

/* Using the font property */
div {
  font: italic small-caps bold 24px/1.5 Georgia, serif;
}
```