# Pseudo class for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- A pseudo-class is a keyword that can be added to a selector to specify a special state or condition of the selected element(s).
- For example, the pseudo-class `:hover` can be used to change the style of an element when the user moves the mouse over it, such as changing its color or background.
- The syntax of a pseudo-class is a colon (`:`) followed by the pseudo-class name, such as `a:hover` or `p:first-child`.
- Pseudo-classes can be combined with other selectors, such as element selectors, class selectors, or attribute selectors, to create more specific and dynamic rules.
- Some common pseudo-classes are:

  - `:link` - selects unvisited links
  - `:visited` - selects visited links
  - `:active` - selects the active link (the one being clicked)
  - `:focus` - selects the element that has focus (such as an input field)
  - `:first-child` - selects the first child element of its parent
  - `:last-child` - selects the last child element of its parent
  - `:nth-child(n)` - selects the nth child element of its parent, where n can be a number, a keyword, or a formula
  - `:nth-last-child(n)` - selects the nth child element of its parent, counting from the last one
  - `:first-of-type` - selects the first element of its type among its siblings
  - `:last-of-type` - selects the last element of its type among its siblings
  - `:nth-of-type(n)` - selects the nth element of its type among its siblings
  - `:nth-last-of-type(n)` - selects the nth element of its type among its siblings, counting from the last one
  - `:empty` - selects the elements that have no children (including text nodes)
  - `:not(selector)` - selects the elements that do not match the given selector
  - `:checked` - selects the checked elements (such as checkboxes or radio buttons)
  - `:disabled` - selects the disabled elements (such as buttons or inputs)
  - `:enabled` - selects the enabled elements (such as buttons or inputs)
  - `:root` - selects the root element of the document (usually the `<html>` element)
  - `:target` - selects the element that is the target of the current URL fragment (such as `#section1`)
  - `:lang(language)` - selects the elements that have a language attribute that matches the given language code (such as `lang="en"`)