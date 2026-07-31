### Attribute selector for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- An attribute selector in CSS is used to select any HTML elements with some specific attribute value or attribute .
- Attribute selectors can be used to style elements based on the presence or absence of an attribute, or based on the exact or partial value of an attribute .
- Attribute selectors are written inside square brackets, followed by the attribute name and optionally a value  .
- For example, `[type="text"]` selects all elements with a `type` attribute that has the exact value of `"text"`.
- There are different types of attribute selectors, depending on the operator used to compare the attribute value  :
  - `[attr]` matches elements that have the `attr` attribute, regardless of its value.
  - `[attr=value]` matches elements that have the `attr` attribute with the exact value of `value`.
  - `[attr~=value]` matches elements that have the `attr` attribute with a value that contains the word `value` separated by spaces.
  - `[attr|=value]` matches elements that have the `attr` attribute with a value that is exactly `value` or starts with `value` followed by a hyphen.
  - `[attr^=value]` matches elements that have the `attr` attribute with a value that starts with `value`.
  - `[attr$=value]` matches elements that have the `attr` attribute with a value that ends with `value`.
  - `[attr*=value]` matches elements that have the `attr` attribute with a value that contains `value` as a substring.
- Attribute selectors can be combined with other selectors, such as type, class, or ID selectors, to create more specific rules  .
- For example, `a[href^="https"]` selects all anchor elements that have an `href` attribute that starts with `"https"`.
- Attribute selectors can also be modified by adding a case-sensitivity flag (`i` or `s`) after the value to indicate whether the comparison should be case-insensitive or case-sensitive, respectively  .
- For example, `[lang|="en" i]` matches elements that have a `lang` attribute with a value that is exactly `"en"` or starts with `"en"` followed by a hyphen, regardless of the case of the letters.