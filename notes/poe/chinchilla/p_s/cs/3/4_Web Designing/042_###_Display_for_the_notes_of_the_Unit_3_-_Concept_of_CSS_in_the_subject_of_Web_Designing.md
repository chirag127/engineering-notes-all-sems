### Display for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

CSS, short for Cascading Style Sheets, is a vital part of web designing. CSS is used to style the HTML structure of a webpage to improve its appearance and layout. In this unit, we will delve deeper into the concept of display in CSS.

### Display Property

The display property in CSS is used to determine the type of box model that an HTML element should follow. The display property can be set to a variety of values, including:

- `block`: This is the default value for most HTML elements. Block elements take up the full width of their parent container and create a new line after the element.

- `inline`: Inline elements only take up the necessary width of their content and do not create a new line after the element.

- `inline-block`: This value is a combination of the previous two values. Inline-block elements take up the necessary width of their content but can also have padding and margins applied to them.

- `none`: This value hides the element completely and removes it from the document flow.

### Advantages of the Display Property

- The display property allows for greater control over the layout and appearance of a webpage.

- It allows for different elements to be displayed in different ways, which can improve the overall design of the webpage.

- It can be used to create responsive web designs that adapt to different screen sizes and devices.

### Disadvantages of the Display Property

- Using the display property incorrectly can cause layout issues and make the webpage difficult to navigate.

- Different display values can have different effects on the accessibility of the webpage, so it is important to choose the appropriate value for each element.

### Example

```html
<div class="container">
  <p>This is a paragraph</p>
  <span>This is a span element</span>
</div>
```

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

p {
  background-color: pink;
  padding: 10px;
}

span {
  background-color: lightblue;
  padding: 10px;
}
```

In this example, the container is set to `display: flex`, which allows the child elements (the paragraph and span) to be centered both vertically and horizontally within the container.

### Applications

The display property is used extensively in web designing to create a visually appealing and functional website. It is especially useful for creating responsive designs that adapt to different devices and screen sizes.

In conclusion, the display property is an important concept in CSS that allows web designers to have greater control over the layout and appearance of their webpages. Understanding the different values of the display property and their effects is crucial to creating a well-designed and accessible website.