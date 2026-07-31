### Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text content.
- CSS provides several properties to control the font of a text element, such as its family, size, weight, style, decoration, and more.
- To use a font in CSS, you need to specify the `font-family` property, which can take one or more font names as values. For example:

```css
p {
  font-family: Arial, Helvetica, sans-serif;
}
```

- The `font-family` property can also take a generic font family name, such as `serif`, `sans-serif`, `monospace`, `cursive`, or `fantasy`, which are mapped to specific fonts by the browser. For example:

```css
h1 {
  font-family: fantasy;
}
```

- To use a custom font that is not installed on the user's system, you need to load the font resource from a URL using the `@font-face` rule. For example:

```css
@font-face {
  font-family: "MyFont";
  src: url("myfont.woff2") format("woff2");
}

div {
  font-family: "MyFont";
}
```

- The `font-size` property sets the size of the font, which can be specified in various units, such as pixels, points, ems, rems, percentages, or viewport units. For example:

```css
p {
  font-size: 16px;
}

h1 {
  font-size: 2em;
}

span {
  font-size: 50%;
}
```

- The `font-weight` property sets the weight or thickness of the font, which can be specified as a keyword, such as `normal`, `bold`, `lighter`, or `bolder`, or as a numeric value, such as `100`, `200`, `300`, and so on, up to `900`. For example:

```css
p {
  font-weight: normal;
}

strong {
  font-weight: bold;
}

em {
  font-weight: 300;
}
```

- The `font-style` property sets the style or slant of the font, which can be specified as a keyword, such as `normal`, `italic`, or `oblique`. For example:

```css
p {
  font-style: normal;
}

i {
  font-style: italic;
}

q {
  font-style: oblique;
}
```

- The `text-decoration` property sets the decoration or embellishment of the text, such as `underline`, `overline`, `line-through`, or `none`. For example:

```css
p {
  text-decoration: none;
}

a {
  text-decoration: underline;
}

del {
  text-decoration: line-through;
}
```

- The `line-height` property sets the height of a line of text, which affects the vertical spacing between lines. It can be specified as a unitless number, a length, or a percentage. For example:

```css
p {
  line-height: 1.5;
}

h1 {
  line-height: 50px;
}

span {
  line-height: 120%;
}
```

- The `font` property is a shorthand property that can set multiple font-related properties in one declaration. It can take values for `font-style`, `font-variant`, `font-weight`, `font-size`, `line-height`, and `font-family`. For example:

```css
p {
  font: italic small-caps bold 16px/1.5 Arial, Helvetica, sans-serif;
}
```

- The `font-variant` property sets the variant or alternative style of the font, such as `normal`, `small-caps`, `all-small-caps`, `petite-caps`, `all-petite-caps`, `unicase`, or `titling-caps`. For example:

```css
p {
  font-variant: normal;
}

h1 {
  font-variant: small-caps;
}

span {
  font-variant: unicase;
}
```

- The `font-feature-settings` property allows you to access advanced typographic features of a font, such as ligatures, kerning, alternates, fractions, etc. It takes a list of feature tags and values, which are specific to each font. For example:

```css
p {
  font-feature-settings: "liga" 1, "kern" 1, "frac" 1;
}
```

- The `font