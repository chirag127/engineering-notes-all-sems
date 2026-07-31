### JS Events

JavaScript events are actions that occur in the browser, such as a user clicking a button or a page loading, that can be detected by JavaScript code. These events can be used to trigger specific actions or functions in the code, allowing for interactive and dynamic web pages.

Here are some common JavaScript events:

1. **click**: This event is triggered when a user clicks on an element, such as a button or a link.
2. **mouseover**: This event is triggered when the user moves their mouse over an element.
3. **keydown**: This event is triggered when the user presses a key on the keyboard.
4. **load**: This event is triggered when a page or an element, such as an image, has finished loading.
5. **submit**: This event is triggered when a form is submitted.

These events can be attached to elements using event listeners, which allow the code to specify which function should be called when the event occurs. For example, to attach a click event to a button, the code might look like this:

```javascript
var button = document.getElementById('myButton');
button.addEventListener('click', function() {
  // code to execute when the button is clicked
});
```

This is just a brief introduction to JavaScript events. There is much more to learn and explore in this topic.