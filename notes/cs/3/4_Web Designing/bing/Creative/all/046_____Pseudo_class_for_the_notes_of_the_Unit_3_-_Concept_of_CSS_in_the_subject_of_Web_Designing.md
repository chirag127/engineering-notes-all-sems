# Pseudo-class for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- A pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s) .
- For example, the pseudo-class `:hover` can be used to select a button when a user's pointer hovers over the button and this selected button can then be styled .
- Pseudo-classes enable you to target an element when it's in a particular state, as if you had added a class for that state to the DOM .
- Pseudo-classes can be used to style elements based on various criteria, such as their position, their type, their interaction, their validity, their language, etc .
- The syntax of pseudo-classes is: `selector:pseudo-class { property: value; }` .
- For example, the following CSS rule applies a blue color to the first paragraph of a document: `p:first-of-type { color: blue; }` .
- Some common pseudo-classes are:

  - `:link` and `:visited` for styling links based on their visited state .
  - `:hover`, `:active`, and `:focus` for styling elements based on their interaction state .
  - `:first-child`, `:last-child`, `:nth-child()`, and `:nth-last-child()` for styling elements based on their position among their siblings .
  - `:first-of-type`, `:last-of-type`, `:nth-of-type()`, and `:nth-last-of-type()` for styling elements based on their position among their siblings of the same type .
  - `:not()` for styling elements that do not match a given selector .
  - `:empty` and `:blank` for styling elements that have no content or only whitespace .
  - `:enabled`, `:disabled`, and `:read-only` for styling form elements based on their state .
  - `:checked`, `:indeterminate`, and `:default` for styling form elements based on their value .
  - `:valid`, `:invalid`, and `:required` for styling form elements based on their validity .
  - `:root` for styling the root element of the document .
  - `:target` for styling the element that is the target of the current URL fragment .
  - `:lang()` for styling elements based on their language .

- Pseudo-classes are not the same as pseudo-elements, which act as if you had added a whole new element to the DOM, and enable you to style that .
- For example, the pseudo-element `::before` and `::after` enable you to insert content into the document using CSS .
- The syntax of pseudo-elements is: `selector::pseudo-element { property: value; }` .
- For example, the following CSS rule adds a quotation mark before and after each paragraph: `p::before { content: "\""; } p::after { content: "\""; }` .
- Some common pseudo-elements are:

  - `::before` and `::after` for inserting content before and after an element .
  - `::first-line` and `::first-letter` for styling the first line and the first letter of an element .
  - `::selection` for styling the part of an element that is selected by the user .
  - `::marker` for styling the marker of a list item .
  - `::placeholder` for styling the placeholder text of an input element .
  - `::backdrop` for styling the backdrop of a fullscreen element .

- Pseudo-classes and pseudo-elements can be combined with other selectors to create more specific and complex rules .
- For example, the following CSS rule applies a red color to the first letter of the first paragraph of a document: `p:first-of-type::first-letter { color: red; }` .
- Pseudo-classes and pseudo-elements are part of the CSS standard and are supported by most modern browsers [