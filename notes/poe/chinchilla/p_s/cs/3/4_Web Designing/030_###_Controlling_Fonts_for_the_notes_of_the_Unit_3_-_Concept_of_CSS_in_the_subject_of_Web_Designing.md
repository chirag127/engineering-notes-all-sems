### Controlling Fonts for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

When it comes to web designing, fonts play a significant role in the overall look and feel of the website. The good news is that CSS provides a wide range of options for controlling fonts on web pages. In this section, we will explore the various ways to control fonts in CSS.

#### Font Family
The font-family property is used to set the font for an element. Here, you can specify a list of fonts to be used in case the browser does not support the first font. For example,
 
```css
p{
  font-family: Arial, Helvetica, sans-serif;
}
```
This code snippet sets the font for all paragraph elements to Arial. If Arial is not available, it will try to use Helvetica. If Helvetica is not available, it will use any sans-serif font.

#### Font Size
The font-size property is used to set the size of the font. It can be set in various units such as pixels, em, rem, etc. For example,

```css
p{
  font-size: 16px;
}
```

This code sets the font size of all paragraph elements to 16 pixels.

#### Font Style
The font-style property is used to set the style of the font. It can be set to normal, italic, or oblique. For example,

```css
p{
  font-style: italic;
}
```
This code sets the font style of all paragraph elements to italic.

#### Font Weight
The font-weight property is used to set the weight of the font. It can be set to normal, bold, bolder, lighter, or a numeric value. For example,

```css
p{
  font-weight: bold;
}
```
This code sets the font weight of all paragraph elements to bold.

#### Text Decoration
The text-decoration property is used to set the decoration of the text. It can be set to underline, overline, line-through, or none. For example,

```css
a{
  text-decoration: underline;
}
```
This code sets the text decoration of all anchor elements to underline.

#### Text Transform
The text-transform property is used to set the case of the text. It can be set to uppercase, lowercase, capitalize, or none. For example,

```css
h1{
  text-transform: uppercase;
}
```
This code sets the case of all h1 elements to uppercase.

In conclusion, controlling fonts in CSS is an essential part of web designing. By using the various font properties provided by CSS, one can easily change the look and feel of the website.