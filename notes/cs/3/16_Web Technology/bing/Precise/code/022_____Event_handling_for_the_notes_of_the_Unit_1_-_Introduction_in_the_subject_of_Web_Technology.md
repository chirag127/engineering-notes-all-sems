### Event handling

Event handling is a process that deals with the events that occur in a web page. An event is an action that occurs as a result of user interaction or a change in the state of the system. Some common events include:

1. Clicking on a button or a link
2. Moving the mouse over an element
3. Submitting a form
4. Pressing a key on the keyboard
5. Resizing the window

Event handling involves defining event listeners that specify the actions to be taken when an event occurs. These actions can include updating the content of the page, displaying a message, or sending data to the server.

Event listeners can be attached to specific elements on the page, or to the document object to handle events that occur anywhere on the page. Event listeners can be defined using JavaScript, and can be attached to elements using the `addEventListener()` method.

Here is an example of an event listener that displays an alert message when a button is clicked:

```javascript
var button = document.getElementById('myButton');
button.addEventListener('click', function() {
    alert('Button clicked!');
});
```

In this example, the `addEventListener()` method is used to attach a `click` event listener to the `button` element. When the button is clicked, the anonymous function defined as the second argument to the `addEventListener()` method is executed, and an alert message is displayed.

Event handling is an important concept in web development, as it allows developers to create dynamic and interactive web pages that respond to user actions. It is a fundamental part of the Document Object Model (DOM) and is used extensively in modern web applications.