### Grouping

In CSS, grouping refers to the practice of selecting multiple elements and applying the same styles to all of them. This can be done in several ways:

1. **Grouping Selectors:** Multiple selectors can be grouped together by separating them with a comma. The styles defined within the curly braces will be applied to all the elements selected by the selectors. For example:
```css
h1, h2, h3 {
  color: blue;
}
```
This will apply the color blue to all `h1`, `h2`, and `h3` elements.

2. **Class and ID Selectors:** Classes and IDs can be used to group elements together. A class can be applied to multiple elements, and all elements with the same class will have the same styles applied to them. An ID, on the other hand, is unique and can only be applied to one element. For example:
```css
.my-class {
  color: red;
}
```
This will apply the color red to all elements with the class `my-class`.

3. **Descendant Selectors:** Descendant selectors can be used to select elements that are descendants of another element. This can be useful for grouping elements together that are within a specific container. For example:
```css
div p {
  font-size: 18px;
}
```
This will apply a font size of 18px to all `p` elements that are descendants of a `div` element.

Grouping can be a powerful tool in CSS, allowing you to apply styles to multiple elements at once, making your code more efficient and easier to maintain. It is important to use grouping effectively to ensure that your styles are applied correctly and consistently across your web page.