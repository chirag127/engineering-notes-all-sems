### JS Events for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

JavaScript events are actions that a user or a browser can take while interacting with a website. These events can trigger JavaScript code to perform specific actions on a webpage. Here are some important points to remember about JS events:

- JS events can be categorized into three types: user interface (UI) events, keyboard events, and mouse events. UI events include actions like clicking a button or selecting a checkbox, while keyboard events include actions like typing on a keyboard. Mouse events include actions like hovering over an element or clicking on it.

- Event listeners are used to detect when a specific event occurs on a webpage. An event listener is a piece of code that waits for a specific event to occur, and then executes a block of code in response to that event. Event listeners can be added to HTML elements using JavaScript.

- The `addEventListener()` method is used to add an event listener to an HTML element. This method takes two parameters: the type of event to listen for, and the function to execute when that event occurs. For example, to add an event listener for a button click, you would use the following code:

  ```javascript
  const button = document.querySelector('button');
  button.addEventListener('click', function() {
    // code to execute when button is clicked
  });
  ```

- The `removeEventListener()` method is used to remove an event listener from an HTML element. This method takes the same parameters as `addEventListener()`. For example, to remove an event listener for a button click, you would use the following code:

  ```javascript
  const button = document.querySelector('button');
  function handleClick() {
    // code to execute when button is clicked
  }
  button.addEventListener('click', handleClick);
  // later on...
  button.removeEventListener('click', handleClick);
  ```

- Event propagation is the process by which an event is propagated through the DOM tree. There are two types of event propagation: bubbling and capturing. Bubbling is the default propagation method and occurs when an event is first handled by the innermost element and then propagated outward to its parent elements. Capturing occurs when an event is first handled by the outermost element and then propagated inward to its child elements.

- Event delegation is a technique for handling events on multiple elements using a single event listener. With event delegation, you add an event listener to a parent element and then check which child element was clicked inside the event listener. This technique can be useful for dynamically generated content or for optimizing performance.

By understanding JavaScript events, you can create dynamic and interactive webpages that respond to user actions in real-time. With the right knowledge and practice, you can become proficient in using JS events to create engaging user experiences on the web.