### Pseudo class for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- A pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s) .
- For example, the pseudo-class `:hover` can be used to select a button when a user's pointer hovers over the button and this selected button can then be styled .
- Pseudo-classes enable you to target an element when it's in a particular state, as if you had added a class for that state to the DOM .
- Pseudo-classes can be used to style elements based on various criteria, such as their position, their type, their interaction, their validity, their language, etc .
- Some common pseudo-classes are:
  - `:first-child` - selects the first child element of a parent element .
  - `:last-child` - selects the last child element of a parent element .
  - `:nth-child(n)` - selects the nth child element of a parent element, where n can be a number, a keyword, or a formula .
  - `:link` - selects unvisited links .
  - `:visited` - selects visited links .
  - `:active` - selects the active link, i.e., the link that is being clicked .
  - `:focus` - selects the element that has focus, i.e., the element that can be interacted with by keyboard or mouse .
  - `:checked` - selects the checked elements, such as checkboxes or radio buttons .
  - `:disabled` - selects the disabled elements, such as buttons or inputs .
  - `:enabled` - selects the enabled elements, i.e., the opposite of `:disabled` .
  - `:required` - selects the elements that have the `required` attribute .
  - `:optional` - selects the elements that do not have the `required` attribute .
  - `:valid` - selects the elements that have valid values according to their type .
  - `:invalid` - selects the elements that have invalid values according to their type .
  - `:lang(lang)` - selects the elements that have a `lang` attribute with the specified value .
- Pseudo-classes can be combined with other selectors, such as element selectors, class selectors, id selectors, attribute selectors, etc .
- Pseudo-classes can also be chained together, such as `:first-child:hover` or `:nth-child(2n):checked` .
- Pseudo-classes are written with a colon (`:`) before the keyword, such as `:hover` or `:first-child` .
- Pseudo-classes are different from pseudo-elements, which act as if you had added a whole new element to the DOM, and enable you to style that .
- The syntax of pseudo-classes is:

```css
selector:pseudo-class {
  property: value;
}
```

- For example, the following CSS rule will make the first paragraph of a document red when the user hovers over it:

```css
p:first-child:hover {
  color: red;
}
```

- References:
  - : Pseudo-classes - CSS: Cascading Style Sheets | MDN - Mozilla
  - : Pseudo-classes and pseudo-elements - Learn web development | MDN - Mozilla
  - : CSS Pseudo-classes - W3Schools