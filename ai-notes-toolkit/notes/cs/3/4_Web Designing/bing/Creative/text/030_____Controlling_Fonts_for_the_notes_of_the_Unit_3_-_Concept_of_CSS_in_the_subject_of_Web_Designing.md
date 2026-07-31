### Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text content.
- CSS provides various properties to control the font family, size, style, weight, variant, and decoration of the text elements.
- The `font-family` property specifies the name of the font or a list of font names to be used for the text. The browser will use the first available font in the list. For example:

```css
p {
  font-family: Arial, Helvetica, sans-serif;
}
```

- The `font-size` property specifies the size of the font in different units, such as pixels, points, ems, percentages, etc. The default font size is 16 pixels. For example:

```css
h1 {
  font-size: 36px;
}
```

- The `font-style` property specifies the style of the font, such as normal, italic, or oblique. For example:

```css
em {
  font-style: italic;
}
```

- The `font-weight` property specifies the weight or boldness of the font, such as normal, bold, bolder, lighter, or a numeric value from 100 to 900. For example:

```css
strong {
  font-weight: bold;
}
```

- The `font-variant` property specifies whether the text should be displayed in small-caps or normal. For example:

```css
p {
  font-variant: small-caps;
}
```

- The `text-decoration` property specifies the decoration of the text, such as none, underline, overline, line-through, or blink. For example:

```css
a {
  text-decoration: none;
}
```

- The `font` property is a shorthand property that combines the font-family, font-size, font-style, font-weight, and font-variant properties in one declaration. For example:

```css
p {
  font: italic small-caps bold 14px Arial, Helvetica, sans-serif;
}
```