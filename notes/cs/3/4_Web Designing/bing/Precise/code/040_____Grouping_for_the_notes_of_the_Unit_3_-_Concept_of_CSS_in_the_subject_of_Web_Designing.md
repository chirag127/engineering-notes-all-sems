### Grouping

In the context of CSS, grouping refers to the ability to apply the same style to multiple elements. This can be achieved in several ways:

1. **Grouping Selectors**: Multiple selectors can be grouped together by separating them with a comma. The style defined for the group will be applied to all the elements selected by the individual selectors. For example, to apply the same style to all `h1` and `h2` elements, the following CSS code can be used:
```css
h1, h2 {
  color: blue;
}
```

2. **Class Selector**: A class can be defined to group elements that share the same style. The class is defined using a period (`.`) followed by the class name. The style defined for the class will be applied to all the elements that have the class attribute set to the class name. For example, to apply the same style to all elements with the class `highlight`, the following CSS code can be used:
```css
.highlight {
  background-color: yellow;
}
```

3. **ID Selector**: An ID can be defined to group a single element that needs to be styled uniquely. The ID is defined using a hash (`#`) followed by the ID name. The style defined for the ID will be applied to the element that has the ID attribute set to the ID name. For example, to apply a unique style to an element with the ID `header`, the following CSS code can be used:
```css
#header {
  font-size: 24px;
}
```

Grouping allows for more efficient and organized CSS code, making it easier to maintain and update the styles of a website. It is an important concept to understand when working with CSS in web designing.