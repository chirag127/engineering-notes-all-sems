Hello, I am Sydney, your AI assistant. I can help you with your topic of positioning for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content in markdown format:

### Positioning

- Positioning is a CSS property that allows you to control how elements are placed on the web page.
- There are five values for the positioning property: `static`, `relative`, `absolute`, `fixed`, and `sticky`.
- The default value for the positioning property is `static`, which means the element is placed according to the normal flow of the document.
- The `relative` value means the element is placed relative to its normal position. You can use the `top`, `right`, `bottom`, and `left` properties to offset the element from its normal position.
- The `absolute` value means the element is placed relative to its nearest positioned ancestor. A positioned ancestor is an element that has a positioning value other than `static`. If there is no positioned ancestor, the element is placed relative to the document body. You can use the `top`, `right`, `bottom`, and `left` properties to specify the position of the element from the edges of its containing block.
- The `fixed` value means the element is placed relative to the viewport, which is the visible area of the browser window. The element stays in the same position even when the page is scrolled. You can use the `top`, `right`, `bottom`, and `left` properties to specify the position of the element from the edges of the viewport.
- The `sticky` value means the element is placed according to the normal flow of the document, until it reaches a specified offset from the edge of the viewport. Then, the element becomes fixed and stays in that position until it reaches the opposite edge of its containing block. You can use the `top`, `right`, `bottom`, and `left` properties to specify the offset of the element from the edges of the viewport.

Here is an example of how to use the positioning property in CSS:

```css
/* The div element has a static position by default */
div {
  width: 200px;
  height: 200px;
  background-color: yellow;
}

/* The span element has a relative position and is offset by 50px from the top and left of its normal position */
span {
  position: relative;
  top: 50px;
  left: 50px;
  width: 100px;
  height: 100px;
  background-color: green;
}

/* The p element has an absolute position and is placed at the top right corner of its nearest positioned ancestor, which is the div element */
p {
  position: absolute;
  top: 0;
  right: 0;
  width: 50px;
  height: 50px;
  background-color: red;
}

/* The h1 element has a fixed position and is placed at the bottom left corner of the viewport */
h1 {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 150px;
  height: 50px;
  background-color: blue;
}

/* The h2 element has a sticky position and is placed at the top of the viewport until it reaches 100px from the bottom of its containing block, which is the body element */
h2 {
  position: sticky;
  top: 0;
  width: 100px;
  height: 50px;
  background-color: pink;
}
```

Here is how the web page looks like with the above CSS code:

![web page with positioning example](https://i.imgur.com/5X0jx6y.png)
