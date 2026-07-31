# Attribute selector for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- An attribute selector in CSS is used to select any HTML elements with some specific attribute value or attribute .
- Attribute selectors can be used to style elements based on the presence or absence of an attribute, or based on the exact or partial value of an attribute .
- Attribute selectors are written inside square brackets, followed by the attribute name and optionally a value .
- There are different types of attribute selectors, depending on the operator used to compare the attribute value with the given value  .
  - `[attr]` selects elements that have the `attr` attribute, regardless of its value.
  - `[attr=value]` selects elements that have the `attr` attribute with the exact value `value`.
  - `[attr~=value]` selects elements that have the `attr` attribute with a value that contains the word `value` separated by spaces.
  - `[attr|=value]` selects elements that have the `attr` attribute with a value that is exactly `value` or starts with `value` followed by a hyphen.
  - `[attr^=value]` selects elements that have the `attr` attribute with a value that starts with `value`.
  - `[attr$=value]` selects elements that have the `attr` attribute with a value that ends with `value`.
  - `[attr*=value]` selects elements that have the `attr` attribute with a value that contains the substring `value`.
- Attribute selectors can be combined with other selectors, such as type, class, or id selectors, to increase specificity or selectivity .
- Attribute selectors can be useful for styling elements based on their semantic meaning, state, or data .
- For example, the following CSS rule will select all `a` elements that have the `href` attribute starting with `https` and apply a green color to them:

```css
a[href^="https"] {
  color: green;
}
```