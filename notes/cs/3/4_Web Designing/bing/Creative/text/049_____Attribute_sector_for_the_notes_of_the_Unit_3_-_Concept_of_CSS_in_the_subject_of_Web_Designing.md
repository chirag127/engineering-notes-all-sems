### Attribute selector for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- An attribute selector in CSS is used to select any HTML elements with some specific attribute value or attribute .
- Attribute selectors can be used to style elements based on the presence or absence of an attribute, or based on the exact or partial match of an attribute value .
- Attribute selectors are written inside square brackets, followed by the attribute name and optionally a value .
- There are six types of attribute selectors in CSS  :

  - `[attr]`: This selector matches elements that have the specified attribute, regardless of its value.
  - `[attr=value]`: This selector matches elements that have the specified attribute with the exact value.
  - `[attr~=value]`: This selector matches elements that have the specified attribute with a value that contains the word `value` as a whole word, separated by spaces.
  - `[attr|=value]`: This selector matches elements that have the specified attribute with a value that is exactly `value` or starts with `value` followed by a hyphen (-).
  - `[attr^=value]`: This selector matches elements that have the specified attribute with a value that begins with `value`.
  - `[attr$=value]`: This selector matches elements that have the specified attribute with a value that ends with `value`.
  - `[attr*=value]`: This selector matches elements that have the specified attribute with a value that contains `value` as a substring.

- Attribute selectors can be combined with other selectors, such as type, class, or ID selectors, to create more specific rules  .
- Attribute selectors can be useful for styling elements based on their attributes, such as links, forms, images, or data  .
- Attribute selectors have a lower specificity than class or ID selectors, but a higher specificity than type selectors .
- Attribute selectors are supported by all modern browsers, but some older browsers may not support some of the newer types .