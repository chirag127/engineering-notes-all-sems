# Floating

- Floating is a CSS property that allows an element to be placed on the left or right side of its container, allowing text and inline elements to wrap around it.
- Floating removes the element from the normal flow of the page, but it still remains a part of the flow (unlike absolute positioning).
- Floating can be used for positioning and layout on web pages, such as letting an image float to one side and letting text wrap around it .
- Floating can have one of the following values:
  - `left` - The element floats to the left of its container
  - `right` - The element floats to the right of its container
  - `none` - The element does not float (will be displayed just where it occurs in the text). This is the default value.
  - `inherit` - The element inherits the float value of its parent element
- Floating can be cleared by using the `clear` property, which specifies what elements can float beside the cleared element and on which side.
- Clearing can have one of the following values:
  - `left` - The element is not allowed to have any floating elements on its left side
  - `right` - The element is not allowed to have any floating elements on its right side
  - `both` - The element is not allowed to have any floating elements on either side
  - `none` - The element is allowed to have floating elements on both sides. This is the default value.
  - `inherit` - The element inherits the clear value of its parent element
- Floating can be used to create various layouts, such as columns, sidebars, image galleries, etc.
- Floating can also be used to create drop caps, which are the first letters of a paragraph that are enlarged and floated to the left.
- Floating can be combined with other CSS properties, such as `margin`, `padding`, `border`, `width`, `height`, etc., to create different effects and styles.