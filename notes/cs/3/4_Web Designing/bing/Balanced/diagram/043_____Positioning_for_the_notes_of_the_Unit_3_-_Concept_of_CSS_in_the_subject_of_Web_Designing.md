### Positioning

- Positioning is a concept in CSS that allows you to control how elements are laid out on a web page.
- Positioning can be used to create complex layouts, overlap elements, align elements, or create fixed or sticky elements that stay in place when scrolling.
- There are five values for the `position` property in CSS: `static`, `relative`, `absolute`, `fixed`, and `sticky`.
- `static` is the default value and means that the element is positioned according to the normal flow of the document.
- `relative` means that the element is positioned relative to its normal position, and can be offset using the `top`, `right`, `bottom`, or `left` properties.
- `absolute` means that the element is positioned relative to its closest positioned ancestor, or the document root if none exists, and can be placed anywhere using the `top`, `right`, `bottom`, or `left` properties.
- `fixed` means that the element is positioned relative to the viewport, and stays in the same place even when scrolling. It can also be placed anywhere using the `top`, `right`, `bottom`, or `left` properties.
- `sticky` means that the element is positioned according to the normal flow of the document, until it reaches a specified threshold (such as the top or bottom edge of the viewport), and then becomes fixed. It can also be offset using the `top`, `right`, `bottom`, or `left` properties.
- To use positioning effectively, you need to understand the concept of the **containing block**, which is the box that defines the layout of a positioned element. The containing block depends on the value of the `position` property and the context of the element.
- You also need to understand the concept of the **stacking context**, which is the order in which elements are rendered on the web page. The stacking context depends on the value of the `position` property, the `z-index` property, and other factors. The higher the `z-index` value, the closer the element is to the front.