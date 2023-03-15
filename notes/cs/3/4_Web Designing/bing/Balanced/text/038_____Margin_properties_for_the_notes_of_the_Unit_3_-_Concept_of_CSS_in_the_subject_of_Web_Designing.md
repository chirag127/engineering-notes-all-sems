### Margin properties

- The CSS margin properties are used to create space around elements, outside of any defined borders.
- With CSS, you have full control over the margins. There are properties for setting the margin for each side of an element (top, right, bottom, and left).
- The margin property is a shorthand for four subproperties: margin-top, margin-right, margin-bottom, and margin-left.
- Each subproperty can have a length value (in px, pt, cm, etc.), an auto value (the browser calculates the margin), an initial value (sets the margin to its default value), or an inherit value (inherits the margin from its parent element) .
- The margin property can also have one, two, three, or four values, depending on how many sides you want to specify.
  - One value: applies to all four sides (e.g., margin: 10px;)
  - Two values: applies to top and bottom, and right and left sides (e.g., margin: 10px 20px;)
  - Three values: applies to top, right and left, and bottom sides (e.g., margin: 10px 20px 30px;)
  - Four values: applies to top, right, bottom, and left sides (e.g., margin: 10px 20px 30px 40px;)
- The margin property can also use negative values, which can create overlapping elements.
- The top and bottom margins of elements are sometimes collapsed into a single margin that is equal to the largest of the two margins. This does not happen on horizontal (left and right) margins.
- The margin property can be used to center an element by setting the left and right margins to auto.
- The margin property can also be used to create space between columns of elements by using the margin-right and margin-left subproperties.