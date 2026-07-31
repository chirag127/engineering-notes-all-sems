Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of JS Events for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

### JS Events

- JS events are actions or occurrences that happen in the browser that can be detected and handled by JS code.
- JS events can be triggered by user interactions, such as clicking a button, moving the mouse, typing on the keyboard, etc.
- JS events can also be triggered by the browser, such as loading a page, resizing a window, scrolling a page, etc.
- JS events can be used to create dynamic and interactive web pages that respond to user actions or browser changes.
- To use JS events, we need to do three things:
  - Define an event handler function that contains the code to execute when the event occurs.
  - Select an element or elements that we want to attach the event to.
  - Register the event handler function to the selected element or elements using an event listener.
- An event handler function is a function that is defined by the programmer and named by the programmer. It can have any name, but it should be descriptive and follow the naming conventions of JS. For example:

```js
// An event handler function that changes the background color of the body element to a random color
function changeBackgroundColor() {
  // Generate a random hexadecimal color code
  var randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
  // Select the body element
  var body = document.querySelector("body");
  // Change the background color of the body element to the random color
  body.style.backgroundColor = randomColor;
}
```

- An event listener is a method that is used to register an event handler function to an element or elements. It takes two parameters: the name of the event and the name of the event handler function. For example:

```js
// Select the button element
var button = document.querySelector("button");
// Register the event handler function to the button element for the click event
button.addEventListener("click", changeBackgroundColor);
```

- The name of the event is a string that represents the type of event that we want to handle. For example, "click", "mouseover", "keydown", etc. The name of the event is case-sensitive and should not include the "on" prefix. For example, "onclick" is incorrect, but "click" is correct.
- The name of the event handler function is the name of the function that we defined earlier. It should not include the parentheses or any arguments. For example, "changeBackgroundColor()" is incorrect, but "changeBackgroundColor" is correct.
- The event listener method can be used to register multiple event handler functions to the same element for the same or different events. For example:

```js
// Select the button element
var button = document.querySelector("button");
// Register the event handler function to the button element for the click event
button.addEventListener("click", changeBackgroundColor);
// Register another event handler function to the button element for the mouseover event
button.addEventListener("mouseover", function() {
  // This is an anonymous function that changes the text color of the button element to white
  button.style.color = "white";
});
```

- The event listener method can also be used to register the same event handler function to multiple elements for the same or different events. For example:

```js
// Select all the paragraph elements
var paragraphs = document.querySelectorAll("p");
// Loop through each paragraph element
for (var i = 0; i < paragraphs.length; i++) {
  // Register the event handler function to each paragraph element for the click event
  paragraphs[i].addEventListener("click", function() {
    // This is an anonymous function that changes the text color of the clicked paragraph element to red
    this.style.color = "red";
  });
}
```

- The event listener method is the preferred way of registering event handler functions in modern JS. However, there is another way of registering event handler functions using HTML attributes. For example:

```html
<!-- This is a button element that has an onclick attribute that calls the changeBackgroundColor function -->
<button onclick="changeBackgroundColor()">Change Background Color</button>
```

- The HTML attribute method is not recommended because it mixes HTML and JS code, which makes the code less readable and maintainable. It also only allows one event handler function per element per event, which limits the functionality and flexibility of the code.