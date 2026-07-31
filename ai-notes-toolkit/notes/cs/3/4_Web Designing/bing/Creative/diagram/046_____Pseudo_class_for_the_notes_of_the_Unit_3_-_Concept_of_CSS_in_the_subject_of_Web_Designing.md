### Pseudo class

- A pseudo class is a keyword that is added to a selector to specify a special state of the selected element(s).
- Pseudo classes can be used to style elements based on user interaction, document structure, form input, or other criteria.
- Pseudo classes are preceded by a colon (`:`) and can be combined with other selectors, such as element, class, or id selectors.
- Some examples of pseudo classes are:

  - `:hover`: selects an element when the user's pointer is over it.
  - `:visited`: selects a link that has been visited by the user.
  - `:first-child`: selects an element that is the first child of its parent.
  - `:checked`: selects an input element that is checked or selected.

- The syntax of pseudo classes is:

  ```css
  selector:pseudo-class {
    property: value;
  }
  ```

- For example, the following CSS rule will change the color of a link to red when the user hovers over it:

  ```css
  a:hover {
    color: red;
  }
  ```

- Pseudo classes can be chained together to create more specific selectors. For example, the following CSS rule will select the first paragraph of a section that is the first child of its parent:

  ```css
  section:first-child p:first-child {
    font-weight: bold;
  }
  ```

- Pseudo classes are different from pseudo elements, which are keywords that create virtual elements that can be styled as part of the document. Pseudo elements are preceded by two colons (`::`) and can be used to style parts of an element, such as the first line, the first letter, or the content before or after the element. For example, the following CSS rule will insert a quotation mark before the content of a blockquote element:

  ```css
  blockquote::before {
    content: '"';
  }
  ```