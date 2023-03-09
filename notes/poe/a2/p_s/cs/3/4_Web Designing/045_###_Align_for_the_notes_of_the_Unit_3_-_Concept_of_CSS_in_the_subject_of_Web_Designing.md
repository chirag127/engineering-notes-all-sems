 Here are the notes for the topic ### Align for Unit 3 - Concept of CSS in Web Designing:

1. Align refers to the positioning of elements in a Web page using CSS. It controls the layout structure of a Web page.
2. The main types of alignment in CSS are:
- Horizontal alignment: Left, Right, Center
- Vertical alignment: Top, Bottom, Center
3. Horizontal alignment can be achieved using the `text-align` property for inline elements and `margin` or `float` properties for block level elements.
4. Vertical alignment can be achieved using the `vertical-align` property for inline elements and `margin` property for block level elements.
5. The `float` property is used to float an element to the left or right of its container, allowing text and other elements to wrap around it. It is commonly used for image galleries or to create entire web page layouts.
6. The `clear` property is used to specify which sides of an element other floating elements are not allowed. It is used to prevent overlapping of floating elements.

**Examples:**
```css
h1 {
  text-align: center; /* Centers the h1 horizontally */
}

img {
  float: left; /* Floats the image to the left */
  margin-right: 10px; /* Adds margin to the right of image */
}

div {
  clear: both; /* Clears both left and right floats */
}
```

**Advantages:** Provides structure and arrangement to web pages. Aligns page elements properly enhancing the visual appeal and usability.

**Disadvantages:** May sometimes lead to unintended overlapping or empty spaces if not implemented correctly.

**Applications:** Used in almost all web pages to design the layout and structure content properly. Employed in UI/UX design to arrange elements attractively.