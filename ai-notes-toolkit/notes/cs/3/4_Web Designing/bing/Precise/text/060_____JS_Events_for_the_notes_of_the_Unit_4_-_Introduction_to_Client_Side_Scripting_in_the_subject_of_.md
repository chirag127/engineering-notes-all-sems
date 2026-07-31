### JS Events

JavaScript events are actions that occur in the browser, such as a user clicking a button or a page loading, that can be detected by JavaScript code. These events can be used to trigger specific actions or functions in the code.

Here are some common JavaScript events:

1. **click**: This event is triggered when a user clicks on an element.
2. **mouseover**: This event is triggered when the user moves the mouse over an element.
3. **keydown**: This event is triggered when the user presses a key on the keyboard.
4. **load**: This event is triggered when the page has finished loading.
5. **submit**: This event is triggered when a form is submitted.

These events can be attached to specific elements using event listeners. An event listener is a function that is called when the specified event occurs on the specified element. For example, to attach a click event listener to a button, the following code can be used:

```javascript
var button = document.getElementById('myButton');
button.addEventListener('click', function() {
    // code to be executed when the button is clicked
});
```

This code selects the button element with the id `myButton` and attaches a click event listener to it. When the button is clicked, the function specified as the second argument to the `addEventListener` method is called.

JavaScript events and event listeners provide a powerful way to add interactivity to web pages and create dynamic user experiences. They are an essential part of client-side scripting and are covered in detail in Unit 4 of the Web Designing course.