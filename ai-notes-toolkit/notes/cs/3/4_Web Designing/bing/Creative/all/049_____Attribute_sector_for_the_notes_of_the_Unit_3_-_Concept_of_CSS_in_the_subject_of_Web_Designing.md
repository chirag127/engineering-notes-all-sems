# Attribute selector for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- An attribute selector in CSS is used to select any HTML elements with some specific attribute value or attribute .
- Attribute selectors can be used to style elements based on the presence or absence of an attribute, or based on the exact or partial match of an attribute value .
- Attribute selectors are written inside square brackets, followed by the attribute name and optionally a value .
- For example, `[href]` selects all elements that have an `href` attribute, regardless of its value. `[type="text"]` selects all elements that have a `type` attribute with the exact value of `"text"`.
- There are different types of attribute selectors, depending on the operator used to compare the attribute value  :
  - `[attr]` matches elements that have the specified attribute, regardless of its value.
  - `[attr=value]` matches elements that have the specified attribute with the exact value of `value`.
  - `[attr~=value]` matches elements that have the specified attribute with a value that contains the word `value` as a whole word, separated by spaces.
  - `[attr|=value]` matches elements that have the specified attribute with a value that is exactly `value` or starts with `value` followed by a hyphen.
  - `[attr^=value]` matches elements that have the specified attribute with a value that begins with `value`.
  - `[attr$=value]` matches elements that have the specified attribute with a value that ends with `value`.
  - `[attr*=value]` matches elements that have the specified attribute with a value that contains `value` as a substring.
- Attribute selectors can be combined with other selectors, such as type, class, or id selectors, to create more specific rules .
- For example, `a[href^="https"]` selects all anchor elements that have an `href` attribute that starts with `"https"`. `input[type="checkbox"]:checked` selects all checked checkbox inputs.
- Attribute selectors are case-sensitive, unless the attribute value is in quotes .
- For example, `[type=text]` and `[type="text"]` are equivalent, but `[type=Text]` and `[type="Text"]` are not.