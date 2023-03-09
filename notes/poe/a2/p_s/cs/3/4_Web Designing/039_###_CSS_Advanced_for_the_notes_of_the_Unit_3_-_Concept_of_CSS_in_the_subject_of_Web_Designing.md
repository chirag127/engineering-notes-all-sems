 Here is the content in markdown format for the topic ### CSS Advanced for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing:

### CSS Advanced

1. CSS Selectors:
- CSS selectors are patterns used to select the HTML elements you want to style.
- Some advanced selectors are:
-- Child selectors: Selects elements that are direct children of another element. For example, `div > p` selects all `<p>` elements that are direct children of a `<div>`.
-- Adjacent sibling selector: Selects elements that are beside each other and have the same parent element. For example, `h1 + p` selects the first `<p>` element that is placed immediately after an `<h1>` element.
-- General sibling selector: Selects elements that are siblings but not necessarily adjacent. For example, `h1 ~ p` selects all `<p>` elements that are siblings of an `<h1>` element.

2. CSS Specificity:
- When there are multiple CSS rules applied to an element, the rule with the highest specificity wins and is applied.
- Specificity is calculated using the following order:
-- Inline styles
-- IDs
-- Classes, attributes, and pseudo-classes
-- Elements and pseudo-elements

3. CSS Inheritance:
- CSS inheritance allows child elements to inherit styles from their parent elements.
- Not all CSS properties inherit by default. Properties such as color and font-family inherit, but properties like background-color and border do not.
- Inheritance can be overridden by defining more specific styles.

[Detailed examples and diagrams for the above points can be added here.]

Advantages:
- Allows efficient styling of websites by reusing styles.
- Maintains consistency in websites.

Disadvantages:
- Can cause unwanted inheritance of styles leading to unpredictability.
- Can lead to larger CSS files and slower performance if not used properly.

Applications:
- Commonly used in CSS frameworks like Bootstrap to define common styles for elements.
- Useful for theming websites by defining a common parent element with inherited styles.