# JS Events

JavaScript events are actions that occur in the browser, such as a user clicking a button or a page loading, that can be detected by JavaScript code. These events can be used to trigger specific actions or functions in the code.

Here are some common JavaScript events:

- **click**: This event is triggered when a user clicks on an element.
- **mouseover**: This event is triggered when the user moves the mouse over an element.
- **keydown**: This event is triggered when the user presses a key on the keyboard.
- **load**: This event is triggered when a page or an element has finished loading.
- **submit**: This event is triggered when a form is submitted.

JavaScript event listeners can be added to elements to specify what actions should be taken when a specific event occurs. For example, an event listener can be added to a button to specify what should happen when the button is clicked.

Here is an example of adding an event listener to a button:

```javascript
const button = document.querySelector('button');

button.addEventListener('click', () => {
  console.log('The button was clicked');
});
```

In this example, an event listener is added to the button element to listen for the `click` event. When the button is clicked, the function specified in the second argument of the `addEventListener` method is called, and the message `'The button was clicked'` is logged to the console.

These are some of the basics of JavaScript events and how they can be used to add interactivity to web pages. There is much more to learn about events and event handling in JavaScript, and it is an important topic to understand when working with client-side scripting in web design.