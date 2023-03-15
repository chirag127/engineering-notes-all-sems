Hello, I am Sydney, your AI assistant. I can help you with your notes on JS Events for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing. Here is the content in markdown format:

# JS Events

- JS events are actions or occurrences that happen in the web browser that can be detected and handled by JS code.
- JS events can be triggered by user interactions, such as clicking a button, moving the mouse, typing a key, etc., or by browser actions, such as loading a page, resizing a window, etc.
- JS events can be used to create dynamic and interactive web pages, such as changing the content, style, or behavior of an element based on user input or browser state.
- To use JS events, we need to follow three steps:
  - Select an element that we want to attach an event to, such as a button, a link, a form, etc.
  - Specify an event type that we want to listen for, such as `click`, `mouseover`, `keydown`, etc.
  - Define a function that will run when the event occurs, also known as an event handler or a callback function.
- There are two ways to attach an event handler to an element:
  - Using the HTML `on` attribute, such as `<button onclick="alert('Hello')">Click Me</button>`
  - Using the JS `addEventListener()` method, such as `button.addEventListener('click', function() {alert('Hello')});`
- The HTML `on` attribute is a simple and direct way to attach an event handler, but it has some drawbacks, such as:
  - It mixes HTML and JS code, which makes the code less readable and maintainable.
  - It can only attach one event handler per event type per element, which limits the functionality and flexibility of the code.
  - It can be overwritten by other JS code, which can cause unexpected behavior or errors.
- The JS `addEventListener()` method is a more modern and recommended way to attach an event handler, as it has some advantages, such as:
  - It separates HTML and JS code, which makes the code more readable and maintainable.
  - It can attach multiple event handlers per event type per element, which allows the code to have more functionality and flexibility.
  - It can be removed by using the `removeEventListener()` method, which gives the code more control and efficiency.
- When an event occurs, the browser creates an object that contains information about the event, such as the type, the target, the coordinates, the key code, etc. This object is called the event object, and it is passed as a parameter to the event handler function.
- The event object can be accessed by using the `event` keyword or by naming the parameter in the event handler function, such as `function(event) {...}` or `function(e) {...}`
- The event object has many properties and methods that can be used to manipulate the event or the element that triggered it, such as:
  - `event.type` returns the type of the event, such as `click`, `mouseover`, `keydown`, etc.
  - `event.target` returns the element that triggered the event, such as the button, the link, the form, etc.
  - `event.clientX` and `event.clientY` return the horizontal and vertical coordinates of the mouse pointer relative to the browser window when the event occurred.
  - `event.keyCode` returns the code of the key that was pressed when the event occurred, such as 13 for Enter, 27 for Escape, etc.
  - `event.preventDefault()` prevents the default action of the event, such as following a link, submitting a form, etc.
  - `event.stopPropagation()` stops the event from bubbling up to the parent elements, which can prevent unwanted behavior or interference from other event handlers.
- JS events can be categorized into different types, such as:
  - Mouse events, such as `click`, `dblclick`, `mouseover`, `mouseout`, `mousedown`, `mouseup`, `mousemove`, etc., that are triggered by mouse actions.
  - Keyboard events, such as `keydown`, `keyup`, `keypress`, etc., that are triggered by keyboard actions.
  - Form events, such as `submit`, `reset`, `change`, `focus`, `blur`, etc., that are triggered by form elements or actions.
  - Window events, such as `load`, `unload`, `resize`, `scroll`, etc., that are triggered by browser actions or states.
  - Custom events, such as `createEvent()`, `initEvent()`, `dispatchEvent()`, etc., that are created and triggered by JS code.