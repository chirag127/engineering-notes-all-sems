### Grouping

In CSS, grouping is a technique used to apply the same style to multiple elements. This can be achieved in two ways:

1. **Grouping Selectors**: Multiple selectors can be grouped together by separating them with a comma. The style defined for the grouped selectors will be applied to all the elements selected by those selectors. For example, to apply the same style to `h1` and `h2` elements, the selectors can be grouped as follows:
```css
h1, h2 {
  color: blue;
}
```

2. **Class and ID Selectors**: Another way to group elements is by using class and ID selectors. A class selector selects all elements with the same class attribute value, while an ID selector selects a single element with a specific ID attribute value. For example, to apply the same style to multiple `div` elements, a class selector can be used as follows:
```css
.div-group {
  background-color: yellow;
}
```
Then, the `div` elements can be grouped by assigning them the same class attribute value:
```html
<div class="div-group">Div 1</div>
<div class="div-group">Div 2</div>
```