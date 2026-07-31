### Grouping

In CSS, grouping refers to the practice of selecting multiple elements and applying the same styles to all of them. This can be done in several ways:

1. **Grouping Selectors:** Multiple selectors can be grouped together by separating them with a comma. The styles defined within the curly braces will be applied to all the elements selected by the grouped selectors. For example:
```css
h1, h2, h3 {
  color: blue;
}
```
In the above example, the color blue is applied to all `h1`, `h2`, and `h3` elements.

2. **Class and ID Selectors:** Classes and IDs can be used to group elements together. A class can be applied to multiple elements, and all elements with the same class will have the same styles applied to them. An ID, on the other hand, is unique and can only be applied to one element. For example:
```css
.my-class {
  color: red;
}
```
In the above example, all elements with the class `my-class` will have the color red applied to them.

3. **Inheritance:** Inheritance is another way to group elements together. Child elements will inherit certain styles from their parent elements. For example, if the color property is set on a parent element, all child elements will inherit that color unless otherwise specified. For example:
```css
body {
  color: green;
}
```
In the above example, all child elements of the `body` element will inherit the color green.

Grouping can be a powerful tool in CSS, allowing you to apply styles to multiple elements at once and helping to keep your code organized and maintainable. It is important to use grouping effectively and efficiently to achieve the desired results.