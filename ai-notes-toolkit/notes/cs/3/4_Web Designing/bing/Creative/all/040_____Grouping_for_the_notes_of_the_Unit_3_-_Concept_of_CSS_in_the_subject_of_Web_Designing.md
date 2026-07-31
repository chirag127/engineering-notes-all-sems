Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Web Designing. Here is the content for the topic of Grouping for the notes of the Unit 3 - Concept of CSS.

# Grouping

- Grouping is a technique in CSS that allows applying the same style rules to multiple elements or selectors.
- Grouping reduces the repetition and redundancy of code, and makes it easier to maintain and update.
- Grouping can be done in two ways: by using a comma (,) or by using a descendant selector (space).

## Grouping by using a comma

- To group selectors by using a comma, simply list the selectors separated by commas, and then write the style rules inside curly braces.
- For example, to apply the same color and font-size to the `<h1>`, `<h2>`, and `<h3>` elements, we can write:

```css
h1, h2, h3 {
  color: blue;
  font-size: 24px;
}
```

- This is equivalent to writing three separate rules, one for each element:

```css
h1 {
  color: blue;
  font-size: 24px;
}

h2 {
  color: blue;
  font-size: 24px;
}

h3 {
  color: blue;
  font-size: 24px;
}
```

- Grouping by using a comma can be done for any type of selectors, such as element selectors, class selectors, id selectors, attribute selectors, pseudo-class selectors, and pseudo-element selectors.

## Grouping by using a descendant selector

- To group selectors by using a descendant selector, simply write the ancestor element followed by a space and then the descendant element, and then write the style rules inside curly braces.
- For example, to apply the same color and font-weight to all the `<p>` elements that are inside a `<div>` element, we can write:

```css
div p {
  color: green;
  font-weight: bold;
}
```

- This is equivalent to writing a separate rule for each `<p>` element that is inside a `<div>` element:

```css
<div>
  <p style="color: green; font-weight: bold;">This is a paragraph inside a div.</p>
</div>

<div>
  <p style="color: green; font-weight: bold;">This is another paragraph inside a div.</p>
</div>
```

- Grouping by using a descendant selector can be done for any type of selectors, as long as there is a parent-child relationship between them.