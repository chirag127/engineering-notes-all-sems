### JS Events

JavaScript events are actions that occur in the browser, such as a user clicking a button or a page loading, that can be detected by JavaScript code. These events can be used to trigger specific actions or functions in the code.

Here are some common JavaScript events:

1. **click**: This event is triggered when the user clicks on an element.
2. **mouseover**: This event is triggered when the user moves the mouse over an element.
3. **keydown**: This event is triggered when the user presses a key on the keyboard.
4. **load**: This event is triggered when the page has finished loading.
5. **submit**: This event is triggered when a form is submitted.

JavaScript event listeners can be added to elements to specify what code should be executed when a specific event occurs. For example, the following code adds an event listener to a button that will execute a function when the button is clicked:

```javascript
var button = document.getElementById('myButton');
button.addEventListener('click', function() {
    // code to be executed when the button is clicked
});
```

Event listeners can also be added using the `on` event handler properties, such as `onclick` or `onmouseover`. For example, the following code adds an event listener to a button using the `onclick` property:

```javascript
var button = document.getElementById('myButton');
button.onclick = function() {
    // code to be executed when the button is clicked
};
```

These are some of the basics of JavaScript events and how they can be used to add interactivity to web pages. It is important to understand how events work and how to use them effectively in order to create dynamic and engaging web pages.