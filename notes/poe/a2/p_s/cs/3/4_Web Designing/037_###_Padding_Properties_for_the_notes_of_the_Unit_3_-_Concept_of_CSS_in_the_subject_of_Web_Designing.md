 Here is the content in markdown format for the topic ### Padding Properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing:

### Padding Properties

- Padding refers to the space between the element and its border.
- It is used to separate the border of an element from its contents.
- Padding is specified using the padding property.
- The padding property can have up to four values:
    - padding-top
    - padding-right
    - padding-bottom
    - padding-left
- If four values are specified, the values apply to the top, right, bottom, left sides of the element respectively.
- If two or three values are specified, the missing values are taken from the values that are provided.
- If only one value is specified, it applies to all four sides of the element.

For example:

```css
.box {
  padding: 10px;         /* applies 10px padding to all sides */
  padding: 5px 10px;    /* top/bottom padding is 5px, left/right is 10px */
  padding: 10px 15px 8px 5px;  /* top = 10px, right = 15px, bottom = 8px, left = 5px */
}
```

Advantages:
- Adds whitespace around the content. This can make the content more readable and visually appealing.
- Adjusts the clickable area of elements like buttons when added along with margins.

Disadvantages:
- Can affect the size of elements and layout if not used properly.
- Too much padding can make a page look messy and cluttered.

Applications:
- Used around text to improve readability.
- Used around input elements to make them more click-friendly.
- Often used with margins to create consistent spacing and layouts in web pages.

[Detailed diagrams, images and examples can be added here to supplement the notes and make them more comprehensive for learning.]